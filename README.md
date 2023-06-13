<h1 align="center">Physics Simulation</h1>  

![physics-simulation]()

Modelling and simulating physics via [C++](https://isocpp.org/) and [Python](https://www.python.org/) to explore and better understand the beauty of the physical world.


## N-body Simulation
Approximating Gravity in C++ using the [Barnes-Hut Algorithm](https://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation). Using [Quadtrees](https://en.wikipedia.org/wiki/Quadtree), gravity for far off clusters of particles that close together is grouped and treated like a bigger particle for which gravity is applied (just an approximation). This allows for O(N logN) [time complexity](https://en.wikipedia.org/wiki/Time_complexity) making the simulation viable for huge number of particles.


## Projectile Motion
Projectile motion is a type of motion that occurs when an object moves in a [gravitational field](https://en.wikipedia.org/wiki/Gravitational_field). In this simulation, a particle's [trajectory](https://en.wikipedia.org/wiki/Trajectory) is modeled based on user-defined attributes. These attributes determine the behavior of the ball during its motion. The simulation calculates the ball's trajectory at intervals of 0.2 seconds slowing the simulation for better visibility.


## Videos:

https://user-images.githubusercontent.com/91330011/227472574-c2f75694-eeff-4809-a760-864815338075.mp4

