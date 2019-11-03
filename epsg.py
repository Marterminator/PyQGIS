import processing

# Working directory needed for importing UTM file.
wd = '/home/martin/projects/PyQGIS/'

# Get UTM zones.
utm = QgsVectorLayer(wd + '/data/utmzones.shp', 'utm', 'ogr')

# Get active layer and reproject to same CRS as UTM file.
layer = iface.activeLayer()
reproject = processing.runalg('qgis:reprojectlayer',layer,'EPSG:25832',None)
layer = QgsVectorLayer(reproject['OUTPUT'], "layer", "ogr")

# Fetch extent of reprojected layer.
ext = layer.extent()
xmin = ext.xMinimum()
xmax = ext.xMaximum()
ymin = ext.yMinimum()
ymax = ext.yMaximum()

# Calculate mean of extent and create point feature.
gPnt = QgsGeometry.fromPoint(QgsPoint((xmin+xmax)/2,(ymin+ymax)/2))
features = utm.getFeatures()
for f in features:
  geom = f.geometry()
  # Find zone containing point.
  if geom.contains(gPnt):
      zone = f['zone']
if zone == 31:
    print('Your suggested CRS is EPSG 25831')
elif zone == 32:
    print('Your suggested CRS is EPSG 25832')
elif zone == 33:
    print('Your suggested CRS is EPSG 25833')
