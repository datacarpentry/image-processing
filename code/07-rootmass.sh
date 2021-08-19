#!/bin/bash
# Run the root density mass on all of the root system trail images.

# first, remove existing binary output images
rm data/*-binary.jpg

# then, execute the program on all the trail images
for f in data/07-trial-*.jpg
do
	python code/07-RootMass.py $f 1.5
done
