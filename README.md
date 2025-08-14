# This repository contains the code and data to reproduce Ozdogan et al [2025] paper[^1].

**<ins>Step 1:</ins>** Set up a free Google Earth Engine (GEE) account as described [here](https://courses.spatialthoughts.com/gee-sign-up.html).

**<ins>Step 2a:</ins>** Use the following javaScript (JS) code to produce Maha rice maps for the year(s) of interest.  The result will be a rice map at 30-meter pixels where pixel value = 1 means rice presence in the Maha season for that year:

https://code.earthengine.google.com/b2dddb2e452cceaea6bfb95adfd568d1

The resulting rice map images for 15 years [2010-2024] for the Maha season can be found here as a [GEE imageCollection asset](https://code.earthengine.google.com/?asset=projects/ee-ozdogan05/assets/srilanka/LK_maha_rice_v3). This is provided for convenience to the user.

**<ins>Step 2a:</ins>** Use the following javaScript (JS) code to produce Yala rice maps for the year(s) of interest. The result will be a rice map at 30-meter pixels where pixel value = 1 means rice presence in the Yala season for that year:

https://code.earthengine.google.com/4bf57d1de82df68bfe2a204fbd25fd70

The resulting rice map images for 15 years [2010-2024] for the Yala season can be found here as a [GEE imageCollection asset](https://code.earthengine.google.com/?asset=projects/ee-ozdogan05/assets/srilanka/LK_yala_rice_v3). This is provided for convenience to the user.

**<ins>Step 3a:</ins>** Extract variables used to estimate rice yield at the pixel level for the Maha season:

https://code.earthengine.google.com/5a0d66287b5d23e901890a855eae2eb6?noload=1

The result will be a set of CSV (comma separated values) formatted files that needs to be combined and used in a random forest (RF) algorithm. The current version will extract 15 years [2010-2024] CSV files [15 files] in a for loop. Note that these predictor values need to be matched with district-level yield data that can be obtained from Sri Lanka paddy yield statistics database. This is done outside of GEE and the resulting file is provided in this repository [LK_maha_yield_features_2010_2024.xlsx]. This dataset can also be found as a [GEE featureCollection asset](https://code.earthengine.google.com/?asset=projects/ee-ozdogan05/assets/srilanka/LK_maha_yield_features_2010_2024). This is provided for convenience to the user.

**<ins>Step 3b:</ins>** Extract variables used to estimate rice yield at the pixel level for the Maha season:

https://code.earthengine.google.com/879e0d3fc931a91d6a44b96bcace383d

The result will be a set of CSV (comma separated values) formatted files that needs to be combined and used in a random forest (RF) algorithm. The current version will extract 15 years [2010-2024] CSV files [15 files] in a for loop. Note that these predictor values need to be matched with district-level yield data that can be obtained from Sri Lanka paddy yield statistics database. This is done outside of GEE and the resulting file is provided in this repository [LK_yala_yield_features_2010_2024.xlsx]. This dataset can also be found as a [GEE featureCollection asset](https://code.earthengine.google.com/?asset=projects/ee-ozdogan05/assets/srilanka/LK_yala_yield_features_2010_2024). This is provided for convenience to the user.

**<ins>Step 4a:</ins>** Map rice yields at the pixel level for the Maha season using a RF algorithm trained with data extracted in Step 3 and merged with district level paddy statistics. The result is a rice yield image for the year of interest for the pixels identified as rice in Step 2 in units of kg/ha:

https://code.earthengine.google.com/5336ff81c688849ac648d0477a74c21f?noload=1

Note that Maha rice yield maps will occasionally have strong district effects due to one-hot-coding implemented in yield estimation algorithms. This is described in the accompanying paper.  To this end, there is an [alternate version](https://code.earthengine.google.com/e97d1a47f559e68d6862f4f2365ec8bd?noload=1) of the yield estimation algorithm that removes the district effect.

**<ins>Step 4b:</ins>** Map rice yields at the pixel level for the Yala season using a RF algorithm trained with data extracted in Step 3 and merged with district level paddy statistics. The result is a rice yield image for the year of interest for the pixels identified as rice in Step 2 in units of kg/ha:

https://code.earthengine.google.com/35444fd02cbf8762fc13a428e09a60aa

Note: Yala rice yield maps will occasionally have strong district effects due to one-hot-coding implemented in yield estimation algorithms. This is described in the accompanying paper.  To this end, there is an [alternate version](https://code.earthengine.google.com/f027e525b93163dac818dddcdfdd9389) of the yield estimation algorithm that removes the district effect.

# Examples

[Visualize a single year [2022] Maha rice map](https://code.earthengine.google.com/c0f8a5f93ec24b8bc878a69463226fa8).  Yellow colored pixels are rice detected fields and non-rice fields are transparent. 

[Visualize a single year [2022] Yala rice map](https://code.earthengine.google.com/e44ae9ee06764a8beb8a8d0058825fb1).  Yellow colored pixels are rice detected fields and non-rice fields are transparent. 

[Visualize 15 years [2010-2024] of Maha rice maps as frequency](https://code.earthengine.google.com/f55b935cda2568b65201eb02b7cd4764). Pixel values will range from 1 [1 year out of 15 years was detected as rice] to 15 [all 15 years were detected as rice]. Pixels are color coded from white [1 year out of 15] to red [15 years out of 15].

[Visualize 15 years [2010-2024] of Yala rice maps as frequency](https://code.earthengine.google.com/3dd90fb99c5304b91610e4c6059fab43). Pixel values will range from 1 [1 year out of 15 years was detected as rice] to 15 [all 15 years were detected as rice]. Pixels are color coded from white [1 year out of 15] to red [15 years out of 15].

# Data availability statement

The data used in this analysis is available in GEE and cane be accessed using the code editor and repository links provided above. Datasets outside of GEE are also provided in this repository.



[^1]: Özdoğan, M.; Wang, S.; Ghose, D.; Fraga, E.; Fernandes, A.; Verala, G. Field-Scale Rice Area and Yield Mapping in Sri Lanka with Optical Remote Sensing and Limited Training Data. Remote Sens. 2025, 17, x. https://doi.org/10.3390/xxxxx








