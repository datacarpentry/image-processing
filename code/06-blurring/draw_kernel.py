"""
 * Python script to create an image of a Gaussian kernel.
 * Intended for lesson maintainers use only.
 * Outputs to `./fig/06_Gaussian_kernel.png`
 *
 * usage: python draw_kernel.py
"""

from astropy.convolution import Gaussian2DKernel
import matplotlib.pyplot as plt
import numpy as np

# Create an array containing the evalusation of a 
# Gaussian function with a standard deviation of 0.8
z = np.array(Gaussian2DKernel(0.8))

# Create co-ordinate matricies for x and y
x, y = np.meshgrid(np.arange(0, z.shape[0]), np.arange(0, z.shape[1]))

# Create vectors representations of x, y and z
x_long = np.reshape(x, z.shape[0]*z.shape[1])
y_long = np.reshape(y, z.shape[0]*z.shape[1])
z_long = np.reshape(z, z.shape[0]*z.shape[1])

# Plot the kernel as an image
plt.imshow(z, interpolation='none', origin='upper', vmin=0, vmax=0.25)

# Label each pixel with it's z value (the kernel evaluated at that point)
for i, label in enumerate(z_long):
    plt.text(x_long[i]-0.3, y_long[i], "{:.2f}".format(label), color='Red')

# Label axes
plt.xlabel('x [pixels]')
plt.ylabel('y [pixels]')
plt.colorbar()

# Save image
plt.savefig('./fig/06_Gaussian_kernel.png')