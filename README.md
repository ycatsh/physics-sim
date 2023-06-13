<h1 align="center">Physics Simulation</h1>  

![physics-simulation]()

Modelling and simulating physics via [C++](https://isocpp.org/) and [Python](https://www.python.org/) to explore and better understand the beauty of the physical world.


<<<<<<< HEAD
## N-body Simulation 
Approximating Gravity in C++ using the Barnes-Hut Algorithm. 

### How it works:
Using Quadtrees, gravity for far off clusters of particles that are close together is grouped and treated like a bigger particle for which gravity is applied (just an approximation). This allows for O(N logN) time complexity making the simulation viable for huge number of particles.

### Video:
(Under Development)

### Equations used:
(Under Development)


## Projectile Motion
Form of motion of an object in a gravitational field.

### How it works:
The ball is given attributes via the user in the terminal, these attributes relate to the trajectory of the ball which is simulated or rather modelled. To start, press space after entering in the values, the simulation is relative to every 0.2 second instead of 1, this makes it easier to see.

### Video:
https://user-images.githubusercontent.com/91330011/227477147-9281ee5e-3099-4814-8abe-5aa0d347ba84.mp4

### Equations used:
Relation between distance, speed, time: $d = {v}\times{t}$  
Displacement formula: $\Delta{x} = u\times t + \frac{a\times t^2}{2}$  
Componenent of velocity along x axis: $u_x = u\times\cos\theta$  
Componenent of velocity along y axis: $u_y = u\times\sin\theta$  
Maximum height of a projectile: $\frac{u^2\times\sin^2\theta}{2g}$  
Horizontal displacement of a projectile: $\frac{u^2\times\sin2\theta}{g}$  
Radian to degree formula: $\theta\times\frac{\pi}{180}$
=======
## N-body Simulation
Approximating Gravity in C++ using the [Barnes-Hut Algorithm](https://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation). Using [Quadtrees](https://en.wikipedia.org/wiki/Quadtree), gravity for far off clusters of particles that close together is grouped and treated like a bigger particle for which gravity is applied (just an approximation). This allows for O(N logN) [time complexity](https://en.wikipedia.org/wiki/Time_complexity) making the simulation viable for huge number of particles.


## Projectile Motion
Projectile motion is a type of motion that occurs when an object moves in a [gravitational field](https://en.wikipedia.org/wiki/Gravitational_field). In this simulation, a particle's [trajectory](https://en.wikipedia.org/wiki/Trajectory) is modeled based on user-defined attributes. These attributes determine the behavior of the ball during its motion. The simulation calculates the ball's trajectory at intervals of 0.2 seconds slowing the simulation for better visibility.
>>>>>>> b62fe0f (changed directory structure)


## Videos:


<<<<<<< HEAD
## Normal distribution
Demonstrates the central limit theorem, in particular that with sufficient sample size the binomial distribution approximates a normal distribution.

### How it works: 
The nails are arranged in Pascal's Triangle sequence, the balls are allowed to fall through it. When the fall is completed for a specific number of balls, we see normal probability distribution graph symbolized. 

### Video:
https://user-images.githubusercontent.com/91330011/227475569-ba88e0bc-ad5a-49cd-a33c-89d52cf143e7.mp4
=======
https://user-images.githubusercontent.com/91330011/227472574-c2f75694-eeff-4809-a760-864815338075.mp4
>>>>>>> b62fe0f (changed directory structure)
