"""
Latex watershed example

   Date          Who      What
----------  -----------  ---------------------------------------------
2019-05-15  John Minter  Initial test. Inspired by this page:
                         https://imagej.net/Classic_Watershed
                         The image is a background-subtracted latex
                         image prepared using Gatan DigitalMicrograph
                         software. Fiji/ImageJ can read this file.

                         The script runs but the Gaussina blur is not working
                         as expected

"""
from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')
import os
from ij import IJ
from ij.plugin.filter import Analyzer

# a way to get rid of most windows
bCleanup = True

# median filter radius
rad = 3
strRadius = "radius=%i" % (rad)

# max intensity for dark latex particles 
maxIntensityLatex = 120
# size for the Gaussian Blur
gbSigma = 3
# base name for the processed blurred latex image
strName = "latex-blur"
# set the string for the Gaussian Blur
gbStr2 = "sigma=%i" % (gbSigma)
# saturated fraction
satFrac = 0.35
strFrac = "saturated=%f" % (satFrac)
# set the strings for processing the blurred latex image
strTitle = strName + ".dm3"
strWS2 = "input=%s mask=None use min=0 max=%i" % (strName, maxIntensityLatex)
print(strWS2)

# use the GIT_HOME variable
gitHome = os.environ['GIT_HOME']

# Image Path
strImgDir = gitHome + "/vitrified-latex-image-anaysis/data/"
strImgNam = "latex01-bks.dm3"
strCsvNam = "latex01-bks.csv"
strImgPath = strImgDir + strImgNam
strCsvPath = strImgDir + strCsvNam
print(strImgPath)

# start clean...
IJ.run("Close All")

# make sure we can write the latest results
exists = os.path.isfile(strCsvPath)
if exists:
	os.remove(strCsvPath)

IJ.open(strImgPath)
IJ.run("Median...", strRadius)
IJ.run("Enhance Contrast", strFrac)
Analyzer.setOption("ScaleConversions", True)
ori = IJ.getImage()
IJ.run("8-bit")
ori.setTitle(strName)
ori.show()

# make an image for the segmentation analysis
IJ.run("Duplicate...", "title=segment")
seg = IJ.getImage()
IJ.run(seg, "Gaussian Blur...", gbStr2)
IJ.run("8-bit")
seg = IJ.getImage()
print(seg.getTitle())

IJ.run("Classic Watershed", strWS2)
# seg.show()
IJ.run("3-3-2 RGB")





