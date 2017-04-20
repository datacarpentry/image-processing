#!/bin/bash
# Run the root density mass on all of the root system trail images.

# first, remove existing mask output images
rm *-mask.jpg

# then, execute the program on all the trail images
for f in trial-*.jpg
do
	python RootMass.py $f 7
done
