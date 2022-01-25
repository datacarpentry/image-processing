"""
 * Python script to figures for lesson 6.
 * Intended for lesson maintainers use only.
 *
 * usage: python make_figures.py
"""

from astropy.convolution import Gaussian2DKernel
import matplotlib.pyplot as plt
import numpy as np
import skimage.filters

# Make a Gaussian kernel image
# Outputs to `./fig/06_Gaussian_kernel.png`

# Create an array containing the evalusation of a 
# Gaussian function with a standard deviation of 0.8
sigma = 0.8
z_kern = np.array(Gaussian2DKernel(sigma))

# Create co-ordinate matricies for x and y
x, y = np.meshgrid(np.arange(0, z_kern.shape[0]), np.arange(0, z_kern.shape[1]))

# Create vectors representations of x, y and z
x_long = np.reshape(x, z_kern.shape[0]*z_kern.shape[1])
y_long = np.reshape(y, z_kern.shape[0]*z_kern.shape[1])
z_kern_long = np.reshape(z_kern, z_kern.shape[0]*z_kern.shape[1])

# Plot the kernel as an image
plt.imshow(z_kern, interpolation='none', origin='upper', vmin=0, vmax=0.25)

# Label each pixel with it's z value (the kernel evaluated at that point)
for i, label in enumerate(z_kern_long):
    plt.text(x_long[i]-0.3, y_long[i], "{:.2f}".format(label), color='Red')

# Label axes
plt.xlabel('x [pixels]')
plt.ylabel('y [pixels]')
plt.colorbar()

# Save image
plt.savefig('./fig/06_Gaussian_kernel.png')
plt.clf()

# -----------

# Create an image file based 
# on a hard-coded matrix representing the blue 
# channel of the corner of the cat image used 
# in this lesson.
# Outputs to `./fig/06_cat_corner_blue.png`

# Hard-coded array taken from lesson text
z_cat = np.array(   [[68,  82, 71, 62, 100,  98,  61],
                [90,  67, 74, 78,  91,  85,  77,],
                [50,  53, 78, 82,  72,  95, 100,],
                [87,  89, 83, 86, 100, 116, 128,],
                [89, 108, 86, 78,  92,  75, 100,],
                [90,  83, 89, 73,  68,  29,  18,],
                [77, 102, 70, 57,  30,  30,  50,]])

# Create co-ordinate matricies for x and y
x, y = np.meshgrid(np.arange(0, z_cat.shape[0]), np.arange(0, z_cat.shape[1]))

# Create vectors representations of x, y and z
x_long = np.reshape(x, z_cat.shape[0]*z_cat.shape[1])
y_long = np.reshape(y, z_cat.shape[0]*z_cat.shape[1])
z_cat_long = np.reshape(z_cat, z_cat.shape[0]*z_cat.shape[1])

# Plot the data as an image
plt.imshow(z_cat, interpolation='none', origin='upper', cmap='Blues_r')

# Label each pixel with it's z value
for i, label in enumerate(z_cat_long):
    plt.text(x_long[i]-0.3, y_long[i], label, color='Red')

# Label axes
plt.xlabel('x [pixels]')
plt.ylabel('y [pixels]')
plt.colorbar()

# Save image
plt.savefig('./fig/06_cat_corner_blue.png')
plt.clf()

# -----------

# Create an image file showing how matricies 
# are combined in convolution 
# Outputs to `./fig/06_combo.png`

# Build array of multiplications
eqn_array = np.char.add(z_cat.astype('str'), ' \\times ')
eqn_array = np.char.add(eqn_array, np.round(z_kern,3).astype(np.dtype('U4')))

# Make read as latex
eqn_array = np.char.add(eqn_array, '$')
eqn_array = np.char.add('$', eqn_array)

eqn_array_long = np.reshape(eqn_array, z_cat.shape[0]*z_cat.shape[1])

plt.plot()
# Label each pixel with it's z value
for i, label in enumerate(eqn_array_long):
    plt.text(x_long[i]-0.4, y_long[i]+0.1, label, color='Red', fontsize=7)
plt.xlim(-0.5, 6.5)
plt.ylim(6.5, -0.5)
plt.axes().set_aspect('equal')
plt.xlabel('x [pixels]')
plt.ylabel('y [pixels]')
plt.savefig('./fig/06_combo.png')
plt.clf()

# Sanity checks

blurred = skimage.filters.gaussian(z_cat, sigma=sigma, preserve_range=True)
print(blurred)
print(blurred[3,3])

mid_px = np.sum(np.multiply(z_cat, z_kern))
print(mid_px)

combo=''

for x,y in zip(z_cat.ravel(),z_kern.ravel()):
    combo += '%f \\times %f + ' % (x,y)

combo = combo[:-2] #remove trailing +

combo += '= %f' % mid_px