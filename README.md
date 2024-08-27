# Project Overview: Serving COGs on GeoServer

This project transitions current image files to Cloud Optimized GeoTIFFs (COGs) stored in the cloud, reducing storage costs and boosting access speeds. Integration with GeoServer will maintain Web Map Service (WMS) capabilities, ensuring continued usability. Image Mosaics will be implemented for seamless, detailed visualizations of large datasets. Additionally, SpatioTemporal Asset Catalog (STAC) integration will be explored to enhance metadata management and simplify data discovery.

---

## How to use this repository:

- Configuration and Setup:

  - GeoServer and database configuration tutorials are located in the `Setup/` directory.
  - For a more general overview, look at the `Example_Tutorial.md` file.

- Jupyter Notebooks (tutorials):

  - **The repository contains Jupyter notebooks that guide you through:**

  - For configuring an Image Mosaic, start with `GS_COG_Mosaic.ipynb` in the `ImageMosaics/` folder to configure a mosaic.
  - The implementation using a STAC-API using `GS_COG_STACAPI_Mosaic.ipynb`.


- Issues
  - View the common issues in the `Logs/` folder.

---

## Requirements

**Python** 3.8 or higher with:
- gdal
- pystac
- requests
  
**Java** 11 or higher

**GeoServer** Version 2.25.0 or higher
- COG Plugin
- STAC datastore plugin (optional)

---

Next Steps/ Improvements:
- Try with password protected HTTP / private S3
- Setup tutorials
- Sample data links
- Uploading conversion script

---
By Matt Graff @ GeoBC, Summer 2024