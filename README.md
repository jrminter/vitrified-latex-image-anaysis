# Image analysis of a vitrified latex using Fiji/ImageJ

## The specimen

The specimen was a soft polymer latex embedded in vitreous ice and imaged
by cryo-TEM. The objective is to subtract the background (the ice has thickness
fluctuations) and then segment each latex particle. We will use shape classifiers
(circularity and aspect ratio) to select the isolated particles.

## The script

The script was written in jython

## The issues

1. The particles are not redirected to the `processed` image as directed,
I do not see the error.

2. I'd like to split some of the overlaps using a watershed, but it
results in thin lines between the particle. I must be missing something. 

