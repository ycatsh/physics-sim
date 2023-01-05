# physics-sim

Modelling and simulating physics via python and pygame.

### Dependencies:

`pygame`

### Particle Physics

### Projectile Motion

Form of motion of an object in a gravitational field.

#### How it works:

The ball is given attributes via the user in the terminal, these attributes relate to the trajectory of the ball which is simulated or rather modelled. To start, press space after entering in the values, the simulation is relative to every 0.2 second instead of 1, this makes it easier to see.

#### Equations used:

$$d = {v}\times{t}$$

$$\Delta{x} = u\times t + \frac{a\times t^2}{2}$$

$$u_x = u\times\cos\theta$$

$$u_y = u\times\sin\theta$$

$$\frac{u^2\times\sin^2\theta}{2g}$$

$$\frac{u^2\times\sin2\theta}{g}$$

$$ rad = \theta\times\frac{\pi}{180}$$
