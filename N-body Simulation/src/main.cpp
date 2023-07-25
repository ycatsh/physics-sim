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
std::uniform_int_distribution<> dist(100, 1800);
std::uniform_real_distribution<float> vel(-5.0f, 5.0f);

const float G = 100;


class Source {
    sf::CircleShape point;
    sf::Vector2f pos;

public:
    Source(float x, float y) {
        pos.x = x;
        pos.y = y;

        point.setPosition(pos);
        point.setFillColor(sf::Color::White);
        point.setRadius(3);
    }

    sf::Vector2f get_pos() {
        return pos;
    }

    void render(sf::RenderWindow& window) {
        window.draw(point);
    }
};


class Particle {
    sf::CircleShape point;
    sf::Vector2f pos;
    sf::Vector2f vel;

public:
    Particle(float x, float y, float dx, float dy) {
        pos.x = x;
        pos.y = y;
        vel.x = dx;
        vel.y = dy;

        point.setPosition(pos);
        point.setFillColor(sf::Color::White);
        point.setRadius(2);
    }

    sf::Vector2f get_pos() {
        return pos;
    }

    void update(std::vector<Source>& sources, std::vector<Particle>& particles) {
        for (Source& source : sources) {
            float sX = source.get_pos().x - pos.x;
            float sY = source.get_pos().y - pos.y;
            float s = sqrt((sX * sX) + (sY * sY));

            float norm_x = (1.0f / s) * sX;
            float norm_y = (1.0f / s) * sY;

            float accl_x = norm_x * G * pow((1.0f / s), 2);
            float accl_y = norm_y * G * pow((1.0f / s), 2);

            vel.x += accl_x;
            vel.y += accl_y;
        }

        for (Particle& particle : particles) {
            if (&particle != this) {
                float sX = particle.get_pos().x - pos.x;
                float sY = particle.get_pos().y - pos.y;
                float s = sqrt((sX * sX) + (sY * sY));

                float norm_x = (1.0f / s) * sX;
                float norm_y = (1.0f / s) * sY;

                float accl_x = norm_x * G * pow((1.0f / s), 2);
                float accl_y = norm_y * G * pow((1.0f / s), 2);

                vel.x += accl_x;
                vel.y += accl_y;
            }
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

    std::vector<Source> sources;
    sources.emplace_back(1920/2, 1080/2);

    sf::Font font;
    font.loadFromFile("../fonts/font.ttf");

    std::vector<Particle> particles;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        sf::Time time = clock.getElapsedTime();
        float fps = 1.0f / time.asSeconds();
        clock.restart().asSeconds();

        std::ostringstream ss;
        ss << "FPS: " << std::fixed << std::setprecision(0) << std::round(fps);
        sf::Text fps_text;
        fps_text.setFont(font);
        fps_text.setString(ss.str());
        fps_text.setPosition(20, 1060);
        fps_text.setCharacterSize(20);

        window.clear();


        for (int i = 0; i < particles.size(); i++) {
            particles[i].update(sources, particles);
        }

        for (int i = 0; i < particles.size(); i++) {
            particles[i].render(window);
        }

        for (Source& source : sources) {
            source.render(window);
        }

        window.draw(fps_text);
        window.display();

        if (particles.size() < 2000) {
            int posX = dist(gen);
            int posY = dist(gen);

            float dx = vel(gen);
            float dy = vel(gen);

            particles.emplace_back(posX, posY, dx, dy);
        }
    }

    return 0;
}
