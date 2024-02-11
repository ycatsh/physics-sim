<h2 align="center">Physics Simulation</h2>  


Modelling and simulating physics via [C++](https://isocpp.org/) and [Python](https://www.python.org/) to explore and better understand the beauty of the physical world.

<br>

## N-body Simulation
Approximating Gravity in C++ using the [Barnes-Hut Algorithm](https://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation). Using [Quadtrees](https://en.wikipedia.org/wiki/Quadtree), gravity for far off clusters of particles that are close together are grouped and treated like bigger particles for which gravity is applied (just an approximation). This allows for O(N logN) [time complexity](https://en.wikipedia.org/wiki/Time_complexity) making the simulation viable for huge number of particles.

### Run
1. The simulation is currently under development, however you can still run `N-body Simulation/bin/main.exe` to view the progress
<br>
<br>

## Projectile Motion
Projectile motion is a type of motion that occurs when an object moves in a [gravitational field](https://en.wikipedia.org/wiki/Gravitational_field). In this simulation, a particle's [trajectory](https://en.wikipedia.org/wiki/Trajectory) is modeled based on user-defined attributes. These attributes determine the behavior of the ball during its motion. The simulation calculates the ball's trajectory at intervals of 0.2 seconds slowing the simulation for better visibility.

### Run
1. In `Projectile Motion/` run `pip3 install -r requirements.txt` to install the dependencies
2. To start the simulation run the python file `main.py` with: `python3 main.py <initial_speed> <acceleration_due_to_gravity> <angle_of_projection>`

Note: It's ``pip`` and ``python`` on windows systems