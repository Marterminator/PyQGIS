# Input paramters:
#   field_name: Field name containing elevation data.
#   tolerance: Tolerance for finding outliers, multiplicator of standard deviation.

def find_outliers(field_name, tolerance):
  # Get active layer containing point elevation data.
  layer = iface.activeLayer()

  # Clear selection.
  layer.setSelectedFeatures([])

  # Fetch z values.
  z = [f[field_name] for f in layer.getFeatures()]

  # Calculate standard deviation and confidence interval with given tolerance.
  mean = sum(z)/len(z)
  i = sum(e**2 for e in z) / len(z)
  var = i - mean**2
  s = (var ** 0.5) * tolerance
  conf = (mean-s, mean+s)

  # Find point id's outside confidence interval.
  ids = [f.id() for f in layer.getFeatures() if f[field_name] < conf[0] or f[field_name] > conf[1]]

  # Select ids.
  layer.setSelectedFeatures(ids)

find_outliers('Z', 1)
