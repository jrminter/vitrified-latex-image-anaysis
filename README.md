# Image analysis of a vitrified latex using Fiji/ImageJ

## The specimen

The specimen was a soft polymer latex embedded in vitreous ice and imaged
by cryo-TEM. The objective is to subtract the background (the ice has thickness
fluctuations) and then segment each latex particle. We will use shape classifiers
(circularity and aspect ratio) to select the isolated particles.

## The scripts

The scripts are written in jython

## Current issues

I'm trying a watershed based on this [over-segmentation](https://imagej.net/Classic_Watershed)
example.

The watershed segmentation has a problem. I need to figure it out...

![Left: background subtracted, Middle: Gaussian Blur, Right: Classic Watershed Segmentation](issues/latex-montage.png)



