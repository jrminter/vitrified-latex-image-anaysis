# ana_latex_.py
#
# Analyze an image of soft latex particles embedded in vitrified ice
#
#  Modifications
#   Date      Who  Ver                       What
# ----------  --- ------  -------------------------------------------------
# 2019-05-14  JRM 0.1.00  test particle sizing
#
from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')

import os
from ij import IJ
from ij.process import ImageProcessor
from ij.process.AutoThresholder import Method

# Setup paths
oriImgPath = "C:/Users/jrminter/Documents/git/vitrified-latex-image-anaysis/data/latex01.tif"
csvPath =  "C:/Users/jrminter/Documents/git/vitrified-latex-image-anaysis/data/latex01.csv"

# load & keep the original image
IJ.run("Close All")
IJ.open(oriImgPath)
impOri = IJ.getImage()
impOri.setTitle("original")
IJ.run(impOri, "Enhance Contrast", "saturated=0.35");
impOri.show()

# make an image for processing steps
IJ.run("Duplicate...", "title=processed")
impProc = IJ.getImage()
IJ.run("Subtract Background...", "rolling=50 light")
IJ.run("Median...", "radius=3")
IJ.run("Enhance Contrast", "saturated=0.35");
impProc.setTitle("processed")
impProc.show()

# make an image for the segmentation analysis
IJ.run("Duplicate...", "title=analyzed")
impAna = IJ.getImage()

# The macro recorder provided these two lines:
# IJ.setAutoThreshold(impAna, "Default");
# setOption("BlackBackground", false);

# I figured this out by using the Java Docs

ip = impAna.getProcessor()
ip.setAutoThreshold(Method.Default, False) 
IJ.run("Convert to Mask")

"""
Note that I tried to re-direct overlay to the processed image. 
It does not redirect. Where did I go wrong? Where did it go???
"""

IJ.run("Set Measurements...", "area mean centroid center perimeter fit shape display add redirect=processed decimal=3")
IJ.run(impAna, "Analyze Particles...", "display exclude summarize")
IJ.saveAs("Results", csvPath)
