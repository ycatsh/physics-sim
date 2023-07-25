#include "tree.h"
#include <memory>

#define _MAX_DEPTH 100

Tree::Tree(double x, double y, double width, double height)
    : centerX(x + width / 2.0), centerY(y + height / 2.0), half_w(width / 2.0), half_h(height / 2.0),
      total_mass(0.0), center_of_mass({0.0, 0.0, 0.0, 0.0}) {}

// insert particles into tree
void Tree::insert(Particle particle) {

}   

// calculate mass of quadrant
void Tree::calculate_mass() {

}

// calculate the force on particle from quadrant
void Tree::calculate_gravity(Particle& particle) {
    
}