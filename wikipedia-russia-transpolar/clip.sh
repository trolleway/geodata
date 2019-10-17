#!/bin/bash

extract='/media/trolleway/46fa49bc-b42a-411f-99f6-4a24dbea79dd/home/trolleway/tmp/restrictions/RU-cit-20190914-ru-shape.zip'

ng_cutter -clipsrc extent3857.geojson -overwrite -f GPKG sea.gpkg -nlt MULTIPOLYGON /home/trolleway/openstreetmapdata/water-polygons-generalized-3857/water_polygons_z3.shp
ng_cutter -clipsrc extent3857.geojson -overwrite -f GPKG land.gpkg -nlt MULTIPOLYGON /home/trolleway/openstreetmapdata/land-polygons-generalized-3857/land_polygons_z3.shp

#ng_cutter -clipsrc /home/trolleway/geodata/wikipedia-russia-transpolar/zones_near_rail_10km.gpkg -overwrite -f GPKG places.gpkg   /vsizip/$extract/data/settlement-point.shp



