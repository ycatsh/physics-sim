#include <SFML/Graphics.hpp>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <random>
#include <vector>

using namespace std;

std::random_device rd;
std::mt19937 gen(rd());

std::uniform_int_distribution<> distx(100, 1800);
std::uniform_int_distribution<> disty(10, 900);
std::uniform_real_distribution<float> vel(-2.0f, 2.0f);
std::uniform_real_distribution<float> m(10.0f, 100.0f);

const float G = 0.001;


class Source {
    sf::CircleShape point;
    sf::Vector2f pos;
    float mass;

public:
    Source(float x, float y, float mass) {
        pos.x = x;
        pos.y = y;
        this->mass = mass;

        point.setPosition(pos);
        point.setFillColor(sf::Color::White);
        point.setRadius(3);
    }

    sf::Vector2f get_pos() {
        return pos;
    }

    float get_mass() {
        return mass;
    }

    void render(sf::RenderWindow& window) {
        window.draw(point);
    }
};


class Particle {
    sf::CircleShape point;
    sf::Vector2f pos;
    sf::Vector2f vel;
    float mass;

public:
    Particle(float x, float y, float dx, float dy, float mass) {
        pos.x = x;
        pos.y = y;
        vel.x = dx;
        vel.y = dy;
        this->mass = mass;

        point.setPosition(pos);
        point.setFillColor(sf::Color::White);
        point.setRadius(2);
    }

    sf::Vector2f get_pos() {
        return pos;
    }

    sf::Vector2f get_vel() {
        return vel;
    }

    float get_mass() {
        return mass;
    }
    
    bool is_collide_particles(Particle& particle){
        float dist = sqrt(pow((pos.x - particle.pos.x), 2) + pow((pos.y - particle.pos.y), 2));
        return dist <= 5.0f;
    }

    bool is_collide_source(Source& source){
        float dist = sqrt(pow((pos.x - source.get_pos().x), 2) + pow((pos.y - source.get_pos().y), 2));
        return dist <= 5.0f;
    }

    void update(std::vector<Source>& sources, std::vector<Particle>& particles) {
        std::vector<int> rem_particles;
        for (int i = 0; i < sources.size(); i++) {
            float sX = sources[i].get_pos().x - pos.x;
            float sY = sources[i].get_pos().y - pos.y;
            float s = sqrt(pow(sX, 2) + pow(sY, 2));

            float norm_x = (1.0f / s) * sX;
            float norm_y = (1.0f / s) * sY;

            float accl_x = norm_x * G * sources[i].get_mass() * mass / pow(s, 2);
            float accl_y = norm_y * G * sources[i].get_mass() * mass / pow(s, 2);

            vel.x += accl_x;
            vel.y += accl_y;

            if (is_collide_source(sources[i])){
                vel.x = 0;
                vel.y = 0;
            }
        }

        for (int i = 0; i < particles.size(); i++) {
            if (&particles[i] != this){
                float sX = particles[i].get_pos().x - pos.x;
                float sY = particles[i].get_pos().y - pos.y;
                float s = sqrt(pow(sX, 2) + pow(sY, 2));

                float norm_x = (1.0f / s) * sX;
                float norm_y = (1.0f / s) * sY;

                float accl_x = norm_x * G * mass * particles[i].get_mass() / pow(s, 2);
                float accl_y = norm_y * G * mass * particles[i].get_mass() / pow(s, 2);

                vel.x += accl_x;
                vel.y += accl_y;
            }

            if (&particles[i] != this && is_collide_particles(particles[i])){
                float combined_mass = mass + particles[i].get_mass();

                vel = ((mass * vel) + (particles[i].get_mass() * particles[i].get_vel())) / combined_mass;
                mass = combined_mass;
                

                rem_particles.push_back(i);
            }
        }

        for (int i = rem_particles.size() - 1; i >= 0; i--) {
            particles.erase(particles.begin() + rem_particles[i]);
        }       

        pos.x += vel.x;
        pos.y += vel.y;
    }


    void render(sf::RenderWindow& window) {
        point.setPosition(pos);
        window.draw(point);
    }
};

int main() {
    sf::RenderWindow window(sf::VideoMode(1920, 1080), "N-Body Simulation");
    window.setFramerateLimit(60);
    sf::Clock clock;

    float dt = 1.0f / 60.0f;

    std::vector<Source> sources;
    std::vector<Particle> particles;

    sf::Font font;
    font.loadFromFile("../fonts/font.ttf");

    sources.emplace_back(1920/2, 1080/2, 1000);

    for (int num = 0; num <= 100; num++) {
        int posX = distx(gen);
        int posY = disty(gen);
        float dx = vel(gen);
        float dy = vel(gen);
        float mass = m(gen);

        particles.emplace_back(posX, posY, dx, dy, mass);
    }

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        sf::Time time = clock.restart();
        float fps = 1.0f / time.asSeconds();

        std::ostringstream ss;
        ss << "FPS: " << std::fixed << std::setprecision(0) << std::round(fps);
        sf::Text fps_text;
        fps_text.setFont(font);
        fps_text.setString(ss.str());
        fps_text.setPosition(20, 1060);
        fps_text.setCharacterSize(20);

        window.clear();

        for (int i = 0; i < particles.size(); i++) {
            particles[i].render(window);
            particles[i].update(sources, particles);
        }

        for (Source& source: sources) {
            source.render(window);
        }

        window.draw(fps_text);
        window.display();
    }

    return 0;
}