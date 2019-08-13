
#download, filter and convert OSM data to GIS layers

#download

url = 'http://download.geo'
filename = 'kansai-latest.osm.pbf'

if not os.path.isfile(filename):
    print('download file '+url)
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
else:
    print(filename+' alreany exist, no downloading')
