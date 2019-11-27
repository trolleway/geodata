1. Do a overpass query, save results as .osm


```
[out:xml][timeout:25];
(
  relation["route"="trolleybus"](42,131,44,133);
);
out body;
>;
out meta qt;
```
2. 
```
osm2pgsql --slim --create --database gis --latlon export.osm
```
3. 
```
python ~/osmot/osmot.py --database gis --host localhost --user   --password 
```
4. 
```
ogr2ogr -f GeoJSON -overwrite  routes_with_refs.geojson  PG:"dbname=gis" "routes_with_refs"
ogr2ogr -f GeoJSON -overwrite  terminals_export.geojson  PG:"dbname=gis" "terminals_export"
```
