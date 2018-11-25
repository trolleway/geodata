osm2pgsql version 0.94.0

1. Do a overpass query, save results as .osm
Нужно убрать маршруты по М4, потому что они нигде не останавливаются

```
[out:xml][timeout:25];
(
  relation["route"="bus"]["ref"!="991"]["ref"!="804"]["ref"!="833"]["ref"!="349"]["ref"!="601"]["ref"!="1039"]["ref"!="1040"]["ref"!="1042"]["ref"!="1200к"](55.5396,37.6666,55.5608,37.7576);
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



