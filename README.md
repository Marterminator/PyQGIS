# PyQGIS

Some scripts for the QGIS Python console.

# outlier.py
Different data sources of elevation data (e.g. geologic maps, drilling information) can cause inconsistencies. Outliers should be identified, compared and corrected. This algorithm finds outliers in point data of the active view dependent on a tolerance (1: normal standard deviation ... n) given by the user.

# epsg.py
The new standard in CRS throughout germany is ERTS89 UTM, but there can be 3 different possible CRS choices (31N, 32N, 33N). This algorithm helps you to find the best fitting EPSG number by an input layer in active view. Furthermore, the inaccuracies in length and area induced by the UTM projection are calculated depending on the location.
