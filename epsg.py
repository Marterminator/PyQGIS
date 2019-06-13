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
  print geom.contains(gPnt)
  print f['zone']
