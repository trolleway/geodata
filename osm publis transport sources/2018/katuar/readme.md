
1. Do a overpass query, save results as .osm


```
[out:xml][timeout:25];
(
  relation["route"="bus"](56.084,37.493,56.089,37.509);
);
out body;
>;
out meta qt;
```
2. 
```
osm2pgsql --slim --create --database gis --latlon ~/Загрузки/export.osm
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

