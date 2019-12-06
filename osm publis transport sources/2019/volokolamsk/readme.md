osm2pgsql version 0.94.0

1. Do a overpass query, save results as .osm


```
[out:xml][timeout:25];
(
  relation["route"="bus"]["ref"="5"](55.99907580276175,35.903938293457024,56.050992893606185,36.0087890625);
);
out body;
>;
out meta qt;
```
2. osm2pgsql --slim --create --database gis --latlon ~/Загрузки/export.osm
3. python ~/osmot/osmot.py --database gis --host localhost --user   --password 
4. 
```
ogr2ogr -f GeoJSON -overwrite  routes_with_refs.geojson  PG:"dbname=gis" "routes_with_refs"
ogr2ogr -f GeoJSON -overwrite  terminals_export.geojson  PG:"dbname=gis" "terminals_export"
```


