import os

cmd = 'ogrmerge.py -o bch_railways_mainlines.gpkg source-mainlines/* -single -overwrite_ds -progress'
os.system(cmd)
