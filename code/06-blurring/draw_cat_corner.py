"""
 * Python script to create an image file based 
 * on a hard-coded matrix representing the blue 
 * channel of the corner of the cat image used 
 * in this lesson.
 * Intended for lesson maintainers use only.
 * Outputs to `./fig/06_cat_corner_blue.png`
 *
 * usage: python draw_kernel.py
"""

import matplotlib.pyplot as plt
import numpy as np

# Hard-coded array taken from lesson text
z = np.array(   [[68,  82, 71, 62, 100,  98,  61],
                [90,  67, 74, 78,  91,  85,  77,],
                [50,  53, 78, 82,  72,  95, 100,],
                [87,  89, 83, 86, 100, 116, 128,],
                [89, 108, 86, 78,  92,  75, 100,],
                [90,  83, 89, 73,  68,  29,  18,],
                [77, 102, 70, 57,  30,  30,  50,]])

# Create co-ordinate matricies for x and y
x, y = np.meshgrid(np.arange(0, z.shape[0]), np.arange(0, z.shape[1]))

# Create vectors representations of x, y and z
x_long = np.reshape(x, z.shape[0]*z.shape[1])
y_long = np.reshape(y, z.shape[0]*z.shape[1])
z_long = np.reshape(z, z.shape[0]*z.shape[1])

# Plot the data as an image
plt.imshow(z, interpolation='none', origin='upper', cmap='Blues_r')

# Label each pixel with it's z value
for i, label in enumerate(z_long):
    plt.text(x_long[i]-0.3, y_long[i], label, color='Red')

# Label axes
plt.xlabel('x [pixels]')
plt.ylabel('y [pixels]')
plt.colorbar()

# Save image
plt.savefig('./fig/06_cat_corner_blue.png')