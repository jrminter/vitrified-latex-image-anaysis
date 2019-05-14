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


IJ.run("Close All")
IJ.open(oriImgPath)
IJ.run("Subtract Background...", "rolling=50 light")
IJ.run("Median...", "radius=3")
impProc = IJ.getImage()
impProc.setTitle("processed")
IJ.run("Duplicate...", "title=analyzed")

# The macro recorder provided these two lines:
# IJ.setAutoThreshold(impAna, "Default");
# setOption("BlackBackground", false);

# I figured this out by using the Java Docs
impAna = IJ.getImage()
ip = impAna.getProcessor()
ip.setAutoThreshold(Method.Default, False) 
IJ.run("Convert to Mask")
# An older version with way too may features measure...
# IJ.run("Set Measurements...", "area mean modal min centroid center perimeter bounding fit shape integrated display add redirect=processed decimal=3")
#
# Note that I tried to re-direct overlay to the 'processed' image. It does not redirect. Where did I go wrong?
#
IJ.run("Set Measurements...", "area mean centroid center perimeter fit shape display add redirect=processed decimal=3")
IJ.run(impAna, "Analyze Particles...", "display exclude summarize")
IJ.saveAs("Results", csvPath)
