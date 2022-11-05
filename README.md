# physics-sim
Modelling projectile motion via pygame and basic kinematic equations.

### Dependencies: 
``pygame``

### How it works:
The ball is given attributes via the user in the temrinal, these attributes relate to the trajectory of the ball which is simulated or rather modelled.  
To start, press space after entering in the values, the simulation is relative to every 0.2 second instead of 1, this makes it easier to see. 

### Physics used:
``S = D/t`` {S= speed, D= distance, t= time}  
``s = u*t + (a*t^2)/2`` {S= displacement, u= initial velocity, a= acceleration, t= time}  
``u along x = u*cosθ, along y = u*sinθ`` {θ= angle between the x axis and projection of the object}  
``[(u^2*sin^2(θ)]/2g`` {maximum height, g= acceleration due to gravity}

### Mathematics used: 
``rad = θ*(π/180)`` {Radians to degree measures}   
*and some basic trigonometry*

### Sample Simulation:
https://user-images.githubusercontent.com/91330011/200007132-23b73dec-9279-461f-83fe-f00a078d0dc0.mp4


