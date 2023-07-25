#include <vector>
#include <memory>

struct Particle {
    float x, y;
    float dx, dy;
    float mass;
};

class Tree {
public:
    Tree(double x, double y, double width, double height);

    void insert(Particle particle);
    void calculate_mass();
    void calculate_gravity(Particle& particle);

private:
    double centerX, centerY;
    double half_w, half_h;
    double total_mass;
    Particle center_of_mass;
    std::vector<Particle> particles;
    std::unique_ptr<Tree> nw, ne, sw, se;
};