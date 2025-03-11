### METADATA
# author: Marco Dalla Vecchia @marcodallavecchia
# description: Simple blurring animation of simple image
# data-source: letterA.tif was created using ImageJ (https://imagej.net/ij/)
###

### INFO
# This script creates the animated illustration of blurring in episode 6
###

### USAGE
# The script requires the following Python packages:
# - numpy
# - scipy
# - matplotlib
# - tqdm
# Install them with
# $ conda install numpy scipy matplotlib tqdm
#
# The script can be executed with
# $ python create_blur_animation.py
# The output animation will be saved directly in the fig folder where the less markdown will pick it up
###

### POTENTIAL IMPROVEMENTS
# - Change colors for rectangular patches in animation
# - Ask for image input instead of hard-coding it
# - Ask for FPS as input
# - Ask for animation format output

# Import packages
import numpy as np
from scipy.ndimage import convolve
from matplotlib import pyplot as plt
from matplotlib import patches as p
from matplotlib.animation import FuncAnimation
from tqdm import tqdm

# Path to input and output images
data_path = "../../../data/"
fig_path = "../../../fig/"
input_file = data_path + "letterA.tif"
output_file = fig_path + "blur-demo.gif"

# Change here colors to improve accessibility
kernel_color = "tab:red"
center_color = "tab:olive"
kernel_size = 3

### ANIMATION FUNCTIONS
def init():
    """
    Initialization function
    - Set image array data
    - Autoscale image display
    - Set XY coordinates of rectangular patches
    """
    im.set_array(img_convolved)
    im.autoscale()
    k_rect.set_xy((-0.5, -0.5))
    c_rect1.set_xy((kernel_size / 2 - 1, kernel_size / 2 - 1))
    return [im, k_rect, c_rect1]

def update(frame):
    """
    Animation update function. For every frame do the following:
    - Update X and Y coordinates of rectangular patch for kernel
    - Update X and Y coordinates of rectangular patch for central pixel
    - Update blurred image frame
    """
    pbar.update(1)
    row = (frame % total_frames) // (img_pad.shape[0] - kernel_size + 1)
    col = (frame % total_frames) % (img_pad.shape[1] - kernel_size + 1)

    k_rect.set_x(col - 0.5)
    c_rect1.set_x(col + (kernel_size/2 - 1))
    k_rect.set_y(row - 0.5)
    c_rect1.set_y(row + (kernel_size/2 - 1))

    im.set_array(all_frames[frame])
    im.autoscale()

    return [im, k_rect, c_rect1]

# MAIN PROGRAM
if __name__ == "__main__":

    print("Creating blurred animation with kernel size:", kernel_size)

    # Load image
    img = plt.imread(input_file)

    ### HERE WE USE THE CONVOLVE FUNCTION TO GET THE FINAL BLURRED IMAGE
    # I chose a simple mean filter (equal kernel weights)
    kernel = np.ones(shape=(kernel_size, kernel_size)) / kernel_size ** 2 # create kernel
    # convolve the image i.e. apply mean filter
    img_convolved = convolve(img, kernel, mode='constant', cval=0) # pad borders with zero like below for consistency


    ### HERE WE CONVOLVE MANUALLY STEP-BY-STEP TO CREATE ANIMATION
    img_pad = np.pad(img, (int(np.ceil(kernel_size/2) - 1), int(np.ceil(kernel_size/2) - 1))) # Pad image to deal with borders
    new_img = np.zeros(img.shape, dtype=np.uint16) # this will be the blurred final image

    # add first frame with complete blurred image for print version of GIF
    all_frames = [img_convolved]

    # precompute animation frames and append to the list
    total_frames = (img_pad.shape[0] - kernel_size + 1) * (img_pad.shape[1] - kernel_size + 1) # total frames if by change image is not squared
    for frame in range(total_frames):
        row = (frame % total_frames) // (img_pad.shape[0] - kernel_size + 1) # row index
        col = (frame % total_frames) % (img_pad.shape[1] - kernel_size + 1) # col index
        img_chunk = img_pad[row : row + kernel_size, col : col + kernel_size] # get current image chunk inside the kernel
        new_img[row, col] = np.mean(img_chunk).astype(np.uint16) # calculate its mean -> mean filter
        all_frames.append(new_img.copy()) # append to animation frames list

    # We now have an extra frame
    total_frames += 1 

    ### FROM HERE WE START CREATING THE ANIMATION
    # Initialize canvas
    f, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))

    # Display the padded image -> this one won't change during the animation
    ax1.imshow(img_pad, cmap='gray')
    # Initialize the blurred image -> this is the first frame with already the final result
    im = ax2.imshow(img_convolved, animated=True, cmap='gray')

    # Define rectangular patches to identify moving kernel
    k_rect = p.Rectangle((-0.5,-0.5), kernel_size, kernel_size, linewidth=2, edgecolor=kernel_color, facecolor='none', alpha=0.8) # kernel rectangle
    c_rect1 = p.Rectangle(((kernel_size/2 - 1), (kernel_size/2 - 1)), 1, 1, linewidth=2, edgecolor=center_color, facecolor='none') # central pixel rectangle
    # Add them to the figure
    ax1.add_patch(k_rect)
    ax1.add_patch(c_rect1)

    # Fix limits to the right image (without padding) is the same size as the left image (with padding)
    ax2.set(
        ylim=((img_pad.shape[0] - kernel_size / 2), -kernel_size / 2), 
        xlim=(-kernel_size / 2, (img_pad.shape[1] - kernel_size / 2))
    )

    # We don't need to see the ticks
    ax1.axis("off")
    ax2.axis("off")

    # Create progress bar to visualize animation progress
    pbar = tqdm(total=total_frames)

    ### HERE WE CREATE THE ANIMATION
    # Use FuncAnimation to create the animation
    ani = FuncAnimation(
        f, update, 
        frames=range(total_frames), 
        interval=50, # we could change the animation speed
        init_func=init,
        blit=True
    )

    # Export animation
    plt.tight_layout()
    ani.save(output_file)
    pbar.close()
    print("Animation exported")
