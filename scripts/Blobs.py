"""
Blobs example

   Date          Who      What
----------  -----------  ---------------------------------------------
2019-05-15  John Minter  


"""
from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')
import os
from ij import IJ
from ij.plugin.filter import Analyzer

IJ.run("Blobs (25K)")
# invert LUT and pixel values to have dark blobs
IJ.run("Invert LUT")
IJ.run("Invert")
# run plugin on image
IJ.run("Classic Watershed", "input=blobs mask=None use min=0 max=150")
# apply LUT to facilitate result visualization
IJ.run("3-3-2 RGB")
# pre-process image with Gaussian blur
IJ.selectWindow("blobs.gif")
IJ.run("Gaussian Blur...", "sigma=3")
imp = IJ.getImage()
imp.setTitle("blobs-blur.gif")
# apply plugin on pre-processed image
IJ.run("Classic Watershed", "input=blobs-blur mask=None use min=0 max=150")
# apply LUT to facilitate result visualization
IJ.run("3-3-2 RGB")