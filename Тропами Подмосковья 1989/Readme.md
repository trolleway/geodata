# Геоданные по книге "Тропами Подмосковья" (1989)

Смотреть на веб-карте: http://trolleway.nextgis.com/resource/3414/display?panel=info

```
В книге "Тропами Подмосковья" (1989) перечислены пешеходные маршруты по лесным и полевым дорогам, и приведены малодетальные схемы. Для того, что бы эти данные можно было использовать в наше время, я взял упомянутые в книге точки маршрутов, и построил между ними маршруты по графу Openstreetmap. Результаты сложены в стандартный обменный формат геоданных, и теперь могут обработаны на компьютере.
Почти всегда местность изменилась, и после строительства автодорог пройти именно по тем маршрутам стало нельзя. Автоматически расчитанные маршруты показывают, где именно нельзя пройти, а где ещё можно.

После ввода всех маршрутов оказалось:
 - Неизменными осталось совсем немного маршрутов, не более 10 штук
 - 45% маршрутов проходят по автодорогам, которые с 1989 года стали такими напряжёнными, что движение пешеходов по ним сложно.
 - Другие 45% маршрутов проходят по глухим лесам, тропы в которых либо не нарисованы в OSM, либо заросли, потому что с 2000-х сильно возросла автомобилизация сельского населения, и теперь ходить между деревнями по лесу - некому.
 - Крайне мало в нащем регионе размеченных пешеходных маршрутов, но в принципе некоторые есть, например вдоль реки Рожайки
 - Подбор населённых пунктов и путевая информация из этой книжки может использоваться для составления новых маршрутов для катания на велосипедах, рейсовых автобусах, и даже на машинах
 - Книжка 1989 года ссылается на деревни, которые подписаны на топокартах того же советского времени. На современных картах приоритет подписей может не совпадать, и эти деревни можно не найти.
 
 ```
 # Attribution
 
 Popadejkin, Vitalij I., Vladimir V. Strukov, and Aleksej M. Tarunov. 1989. Tropami Podmoskov'ja: putevoditel' ; [100 maršrutov]. Moskva: Moskov. Rabočij.
 
 Popadeĭkin, V. (Vitaliĭ). Tropami Podmoskovʹi︠a︡ : putevoditelʹ. — 4-e izd., dop. i perer. — [Moskva]: Moskovskiĭ rabochiĭ, 1989. — 410 pages с. — ISBN 5239000549, 9785239000540.
 
 # Usage
 
 Набор данных представляет собой линейный векторный слой в WGS84 (EPSG:4326), лежащий в файле tropami_podmoskoviya.gpkg
 Geopackage - это стандартный формат для обмена геоданными с 2018 года. Он открывается в QGIS.
 
 Смотреть на веб-карте: http://trolleway.nextgis.com/resource/3414/display?panel=info
 
 # Deploy
 
 ```
unzip
ogrmerge -single -overwrite_ds -progress -o tropami_podmoskoviya.gpkg *.geojson
 ```
