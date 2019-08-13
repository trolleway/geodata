
#download, filter and convert OSM data to GIS layers

#download

url = 'http://download.geo'
filename = 'kansai-latest.osm.pbf'
bbox = '135.571993,34.926126,135.960634,35.144269'

if not os.path.isfile(filename):
    print('download file '+url)
    r = requests.get(url)
    if r.status_code == 404:
        quit(url + 'return 404. Find other pbf file in internet, or place it in this folder as '+filename)
    with open(filename, 'wb') as f:
        f.write(r.content)
else:
    print(filename+' alreany exist, no downloading')

#clip
#'''osmconvert.exe c:\Users\trolleway\Downloads\kansai-latest.osm.pbf -b=135.571993,34.926126,135.960634,35.144269 --complete-multipolygons  --complete-ways --drop-author -o=c:\Users\trolleway\Downloads\kyoto.osm'''

print('clip')
clipped = 'clipped.osm.pbf'

cmd = 'osmconvert {source} -b={bbox} --complete-multipolygons  --complete-ways --drop-author -o={o}'
cmd = cmd.format(source=filename,bbox=bbox,o=clipped)
print(cmd)
os.system(cmd)
                 
