
```
osmconvert dump.osm.pbf -o=dump.o5m
osmfilter dump.o5m --parameter-file=filter.txt >filtered_dump.o5m
osmconvert filtered_dump.o5m -o=filtered_dump.pbf

ogr2ogr -progress -overwrite -oo CONFIG_FILE=osmconf.ini filtered_dump.gpkg filtered_dump.pbf 
```
