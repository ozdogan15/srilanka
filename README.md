# This repository contains the code and data to reproduce Ozdogan et al [2025] paper<sup>*</sup>.

<ins>Step 1:</ins> Set up a free Google Earth Engine (GEE) account as described [here](https://courses.spatialthoughts.com/gee-sign-up.html).

<ins>Step 2a:</ins> Use the following javaScript (JS) code to produce Maha rice maps for the year(s) of interest.  The result will be a rice map at 30-meter pixels where pixel value = 1 means rice presence in the Maha season for that year:

https://code.earthengine.google.com/b2dddb2e452cceaea6bfb95adfd568d1

The resulting rice map images for 15 years [2010-2024] for the Maha season can be found here as a [GEE imageCollection asset](https://code.earthengine.google.com/?asset=projects/ee-ozdogan05/assets/srilanka/LK_maha_rice_v3). This is provided for convenience to the user.

<ins>Step 2a:</ins> Use the following javaScript (JS) code to produce Yala rice maps for the year(s) of interest. The result will be a rice map at 30-meter pixels where pixel value = 1 means rice presence in the Yala season for that year:

https://code.earthengine.google.com/4bf57d1de82df68bfe2a204fbd25fd70

The resulting rice map images for 15 years [2010-2024] for the Yala season can be found here as a [GEE imageCollection asset](https://code.earthengine.google.com/?asset=projects/ee-ozdogan05/assets/srilanka/LK_yala_rice_v3). This is provided for convenience to the user.

<ins>Step 3a:</ins> Extract variables used to estimate rice yield at the pixel level for the Maha season:

https://code.earthengine.google.com/5a0d66287b5d23e901890a855eae2eb6?noload=1

The result will be a set of CSV (comma separated values) formatted files that needs to be combined and used in a random forest (RF) algorithm. The current version will extract 15 years [2010-2024] CSV files [15 files] in a for loop. Note that these predictor values need to be matched with district-level yield data that can be obtained from Sri Lanka paddy yield statistics database. This is done outside of GEE and the resulting file is provided in this repository [LK_maha_yield_features_2010_2024.xlsx]. This dataset can also be found as a [GEE featureCollection asset](https://code.earthengine.google.com/?asset=projects/ee-ozdogan05/assets/srilanka/LK_maha_yield_features_2010_2024). This is provided for convenience to the user.

<ins>Step 3b:</ins> Extract variables used to estimate rice yield at the pixel level for the Maha season:

https://code.earthengine.google.com/879e0d3fc931a91d6a44b96bcace383d

The result will be a set of CSV (comma separated values) formatted files that needs to be combined and used in a random forest (RF) algorithm. The current version will extract 15 years [2010-2024] CSV files [15 files] in a for loop. Note that these predictor values need to be matched with district-level yield data that can be obtained from Sri Lanka paddy yield statistics database. This is done outside of GEE and the resulting file is provided in this repository [LK_yala_yield_features_2010_2024.xlsx]. This dataset can also be found as a [GEE featureCollection asset](https://code.earthengine.google.com/?asset=projects/ee-ozdogan05/assets/srilanka/LK_yala_yield_features_2010_2024). This is provided for convenience to the user.














