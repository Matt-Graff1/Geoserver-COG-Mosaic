# Tutorial: Converting Files to Cloud Optimized GeoTIFF (COG) and Serving Them via GeoServer

This tutorial will guide you through the process of converting old files to Cloud Optimized GeoTIFF (COG) format, uploading them to s3 object storage, gathering links to granules, and setting up a mosaic in GeoServer that you can access via WMS.

## 1. Convert Old Files to COG Format

First, you need to convert your old GeoTIFF files to the COG format. You can do this using the `COG_Conversion.py` tool.

## 2. Upload to S3 Object Storage

Then, upload the COGs to S3 and set the permissions to be 'public-read'. Get the HTTP urls and note them for later.

## 3. Use Jupyter Notebook

Take the HTTP urls of the COGs, and input them into `ImageMosaics/GS_COG_Mosaic.ipynb`. Then, follow the rest of the tutorial on the notebook.

## 4. Access the mosaic & test WMS features

Open your web browser and navigate to your GeoServer instance, usually at `http://localhost:8080/geoserver` or another URL specified by your setup.
- Enter your username and password to log in.

- Once logged in, look for the "Layer Preview" link in the left-hand sidebar under the "Data" section.
- Click on "Layer Preview" to open the list of available layers.
- In the Layer Preview page, you'll see a list of all the published layers.
- You can search for your layer by name or browse through the list to find it. 
- Next to your layer's name, you'll see several options for preview formats (e.g., `OpenLayers`, `KML`, `GeoJSON`, `image/png`).
- Click on the `OpenLayers` link to view the layer in an interactive web map.

You can test the **WMS** in a GIS application like QGIS or by simply opening the URL in a web browser.