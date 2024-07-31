# Project Overview: Serving COGs on GeoServer

Our project aims to transition our current image files to Cloud Optimized GeoTIFFs (COGs) stored in the cloud. This move will reduce storage costs and enhance access speeds for users. By leveraging COGs, we aim to enable faster and more efficient data retrieval, improving the overall user experience.

To ensure continued accessibility and usability, we will integrate these COGs with GeoServer to provide Web Map Service (WMS) capabilities. This integration will maintain our existing service offerings while taking advantage of the cloud's scalability and efficiency.

Additionally, we will implement Image Mosaics through GeoServer, allowing users to view and interact with large, seamless mosaics of the image data. This functionality will support more comprehensive and detailed visualizations of geospatial data, enhancing the analytical capabilities available to our users.

As a forward-looking enhancement, we will explore integrating SpatioTemporal Asset Catalog (STAC) functionality. STAC will provide a robust framework for managing and cataloging geospatial assets, improving metadata management, and enabling easier discovery and access to the data.

```
│   README.md
│
├───Converting to COG
├───ImageMosaics
│       MODIS_COG_Mosaic.ipynb
│       NRSObjStore_COG_Mosaic.ipynb
│
├───Logs
│       Issues.ipynb
│       Startup_Log.md
│
└───Misc
        PostGIS_Setup.ipynb
```

***
Issues can be found in the Logs folder

2024-07-31 MG