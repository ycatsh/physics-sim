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
std::uniform_int_distribution<> dist(1, 100);
std::uniform_real_distribution<float> vel(2.0f, 3.0f);

class Source {
    sf::CircleShape point;
    sf::Vector2f pos;
    float gravity;

public:
    Source(float x, float y, float gravity) {
        pos.x = x;
        pos.y = y;
        this->gravity = gravity;

        point.setPosition(pos);
        point.setFillColor(sf::Color::White);
        point.setRadius(3);
    }

    float get_gravity() {
        return gravity;
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

    void update(Source &point) {
        float sX = point.get_pos().x - pos.x;
        float sY = point.get_pos().y - pos.y;
        float s = sqrt((sX * sX) + (sY * sY));

        float norm_x = (1.0f / s) * sX;
        float norm_y = (1.0f / s) * sY;

        float accl_x = norm_x * point.get_gravity() * pow((1.0f / s), 2);
        float accl_y = norm_y * point.get_gravity() * pow((1.0f / s), 2);

        vel.x += accl_x;
        vel.y += accl_y;
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

    Source source(960, 540, 10000);

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
            particles[i].update(source);
            particles[i].render(window);
        }

        source.render(window);
        window.draw(fps_text);

        window.display();

        if (particles.size() < 20000) {
            int posX = dist(gen);
            int posY = dist(gen);

            float dx = vel(gen);
            float dy = vel(gen);

            particles.emplace_back(posX, posY, dx, dy);
        }
    }

    return 0;
}
