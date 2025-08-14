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

# Additional instructions on how to recreate figures in the manuscript
The image and tabular data generated using the GEE scripts above will need to be further processed in a GIS software to convert from exported format to color figure format to reproduce the figures in the manuscript.  Two example are provided here.

<ins>Example 1: </ins>Steps to recreate Figure 9 in the manuscript.  This figure shows the Maha 2021/2022 rice map of Sri Lanka derived from remote sensing. The red-colored locations are individual image pixels (fields) identified as rice following the methodology described in the text. Also shown are the district boundaries drawn in lighter black lines.

1. Download Sri Lanka District Boundaries
First, you need to get the vector data for Sri Lanka's districts. Navigate to the [GADM download page](https://gadm.org/download_country.html). Select Sri Lanka from the "Country" dropdown menu. Choose GeoPackage as the format. This is a modern, single-file format that's easy to work with. Click the Download button. Save the .gpkg file to a known location on your computer.

2. Add Your Layers to QGIS
Open QGIS. Locate the Browser Panel, which is typically on the left side of the screen. In the Browser Panel, navigate to the folder where you saved the GADM GeoPackage file and your rice field GeoTIFF image (from Step 2 above). Drag and drop both files directly into the Layers Panel (the panel below the Browser, where layer names appear). You should now see both layers displayed in the main map window. Don't worry about the colors yet. QGIS will assign random or default colors.

3. Colorize the Rice Field Raster (GeoTIFF)
This is the core step where you'll assign red to the rice fields and make the background transparent (or white). In the Layers Panel, right-click on your rice field GeoTIFF layer and select Properties. In the Properties window, go to the Symbology tab on the left. At the top, click the dropdown menu for Render type and change it from Singleband gray to Paletted/Unique Values. A new panel will appear below. Click the green Classify button at the bottom. QGIS will scan your image and find all the unique pixel values. You should see two rows appear: one for the value 0 and one for the value 1. To change the color for the background: Double-click the color swatch next to the value 0. In the color picker window, you can either select white or, for better results, make it transparent by dragging the Opacity slider all the way to 0%. Click OK. To change the color for the rice fields: Double-click the color swatch next to the value 1. Select a bright red color and click OK. (Optional) You can make your map legend clearer by double-clicking in the Label column for the value 1 and typing a description like Rice Planted Fields. Click Apply to see your changes and then OK to close the window. Your map should now show red areas representing the rice fields against a transparent or white background.

4. Style the District Boundaries
Finally, let's style the district boundary layer so it acts as a clear overlay without hiding the data underneath. In the Layers Panel, drag the Sri Lanka districts layer above your rice field raster layer. This ensures the boundaries are drawn on top. Right-click the district layer and select Properties. Go to the Symbology tab. Click on Simple Fill. This will open up the fill and outline options. For Fill color, click the dropdown and select Transparent Fill. For Stroke color (the outline), choose a distinct color like black or dark gray. Adjust the Stroke width to a suitable thickness, such as 0.5 Millimeters, so the lines are clear but not overpowering. Click Apply and then OK.

You're all done! Your map should now clearly display the Sri Lankan district boundaries with the areas of rice cultivation highlighted in red.

<ins>Example 2: </ins>Steps to recreate Figure 6 in the manuscript. Figure 6 contains patial patterns of the summed rice index from various parts of Sri Lanka. In general, hues of dark blue indicate a high rice index associated with rice presence, while colors of green, yellow, and red indicate the presence of non-rice crops and other land cover types. Attention is drawn to examples with a large contrast of rice fields (dark blue hues) juxtaposed against non-rice areas (green to yellow to red hues). *Note that these instructions will only generate a single panel of an arbitrary location as an illustration of Figure 6 panels. The process can be repeated to produce other panels for this figure.*

1. Run [this GEE](https://code.earthengine.google.com/d424339e61466f3aa6ff071987a5f6f4) script to export a single year [2020] Rsum image for an example location in Sri Lanka.
   
2. Add Your GeoTIFF image to QGIS. The image would have been generated from bullet 1 above. First, open QGIS and add your raster image to the project. Open a new or existing QGIS project. Locate your GeoTIFF file in the Browser Panel. Drag and drop the file into the Layers Panel or directly onto the map canvas. The image will likely appear in grayscale.

3. Open the Symbology Panel. Next, you'll access the layer styling options where you can change how the raster is displayed. In the Layers Panel, right-click on your GeoTIFF layer. Select Properties from the context menu. In the new window that opens, click on the Symbology tab on the left.

4. Set the Render Type. You need to switch from the default grayscale renderer to one that allows for color gradients. At the top of the Symbology panel, click the dropdown menu for Render type. Change the selection from Singleband gray to Singleband pseudocolor.

5. Create the Custom Color Ramp. This is where you'll define your specific Red -> Yellow -> Dark Blue color scheme. Look for the Color ramp setting. Click the dropdown arrow next to the default color bar. From the menu, select Create New Color Ramp. In the Color ramp type dropdown, choose Gradient. You will now define the "stops" for your gradient. By default, you have two stops: one at the beginning (0.0) and one at the end (1.0). Set the starting color (Red): Click on the first stop (the square marker on the left). Click the Color box and select a bright red. Set the ending color (Dark Blue): Click on the second stop (the square marker on the right). Click the Color box and select a dark blue. Add the middle color (Yellow): Double-click in the middle of the gradient bar. A new stop will appear. Select this new stop, click the Color box, and choose a bright yellow. You can drag this stop left or right to position the yellow exactly where you want it in the transition. For your 0-3 range, leaving it in the center (position 0.5000) is a good starting point. Click OK to save your new gradient.

6. Apply the Color Ramp to Your Data. Finally, apply your newly created color ramp to the values in your GeoTIFF. Back in the main Symbology panel, ensure your new Red-Yellow-Blue ramp is selected. Click the Classify button at the bottom. QGIS will read the values from your raster (from 0 to 3) and apply the full extent of your color ramp to that range. Click Apply to see your changes on the map. Click OK to close the Properties window.

Your GeoTIFF image should now be colorized, with lower values appearing in red, transitioning through yellow for the middle values, and ending with dark blue for the highest values.

# Data availability statement

The data used in this analysis is available in GEE and can be accessed using the code editor and repository links provided above. Datasets outside of GEE are also provided in this repository.



[^1]: Özdoğan, M.; Wang, S.; Ghose, D.; Fraga, E.; Fernandes, A.; Verala, G. Field-Scale Rice Area and Yield Mapping in Sri Lanka with Optical Remote Sensing and Limited Training Data. Remote Sens. 2025, 17, x. https://doi.org/10.3390/xxxxx








