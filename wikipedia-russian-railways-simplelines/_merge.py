import os

#os.unlink('merged.gpkg')
os.system('ogrmerge  -f VRT -o _merged.vrt -single -overwrite_ds *.geojson')
os.system('ogrmerge.py  -f VRT -o _merged.vrt -single -overwrite_ds *.geojson') #two run for unix/windows
