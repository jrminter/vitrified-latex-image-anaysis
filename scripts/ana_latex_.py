"""ana_latex_.py

Analyze an image of soft latex particles embedded in vitrified ice

  Modifications
    Date      Who  Ver                       What
  ----------  --- ------  -------------------------------------------------
  2019-05-14  JRM 0.1.00  test particle sizing
  2019-05-15  JRM 0.1.10  Changes after suggestions from Bio7 and my own
                          web searches :) Note the use of the GIT_HOME 
                          environment variable... Looking at thse results
                          applying shape classifiers on the results will
                          be required.
"""

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')

import os
from ij import IJ
from ij import WindowManager
from ij.process import ImageProcessor
from ij.process.AutoThresholder import Method

# a way to get rid of most windows
bCleanup = True

# Setup paths

gitHome = os.environ['GIT_HOME']
print(gitHome)

oriImgPath = gitHome + "/vitrified-latex-image-anaysis/data/latex01.tif"
csvPath =  gitHome + "/vitrified-latex-image-anaysis/data/latex01.csv"

# make sure we can write the latest results
exists = os.path.isfile(csvPath)
if exists:
	os.remove(csvPath)

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

ip = impAna.getProcessor()
ip.setAutoThreshold(Method.Default, False) 
IJ.run("Convert to Mask")

IJ.run("Set Measurements...", "area mean centroid center perimeter fit shape display add redirect=processed decimal=3")
# suggestion by Bio7
IJ.run(impAna, "Analyze Particles...", "display exclude summarize add")
IJ.run(impProc, "From ROI Manager", "")

IJ.selectWindow("Results")
IJ.saveAs("Results", csvPath)

if bCleanup:
	impOri.close()
	impAna.close()
	IJ.selectWindow("Summary")
	IJ.run("Close")
	IJ.selectWindow("ROI Manager")
	IJ.run("Close");
