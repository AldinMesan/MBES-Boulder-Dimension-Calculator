import os
from osgeo import ogr
from shapely.geometry import Polygon


def measure_boulder_dimensions(input_vector_path, output_vector_path, block_name):
    # Open the input vector file
    input_vector = ogr.Open(input_vector_path)
    input_layer = input_vector.GetLayer()

    # Create an output shapefile
    output_driver = ogr.GetDriverByName('ESRI Shapefile')
    if os.path.exists(output_vector_path):
        output_driver.DeleteDataSource(output_vector_path)
    output_ds = output_driver.CreateDataSource(output_vector_path)
    output_layer = output_ds.CreateLayer('BoulderMeasurements', geom_type=ogr.wkbPoint)

    # Add attribute fields to the output layer
    output_layer.CreateField(ogr.FieldDefn('Poly_ID', ogr.OFTInteger))
    output_layer.CreateField(ogr.FieldDefn('Target_ID', ogr.OFTString))
    output_layer.CreateField(ogr.FieldDefn('Block', ogr.OFTString))
    output_layer.CreateField(ogr.FieldDefn('Easting', ogr.OFTReal))
    output_layer.CreateField(ogr.FieldDefn('Northing', ogr.OFTReal))
    output_layer.CreateField(ogr.FieldDefn('Water_depth', ogr.OFTReal))
    output_layer.CreateField(ogr.FieldDefn('Length', ogr.OFTReal))
    output_layer.CreateField(ogr.FieldDefn('Width', ogr.OFTReal))
    output_layer.CreateField(ogr.FieldDefn('Height', ogr.OFTReal))

    # Iterate through input boulder polygons
    for feature in input_layer:
        # Get the geometry and centroid of the polygon
        geom = feature.GetGeometryRef()
        centroid = geom.Centroid()

        # Calculate the boulder dimensions (length, width, and height)
        boulder_polygon = Polygon(geom.GetPoints())
        length = boulder_polygon.length
        width = boulder_polygon.width

        # For height and water depth, set them to None since bathymetry data is not available
        height = None
        water_depth = None

        # Get the coordinates of the centroid
        easting, northing = centroid.GetX(), centroid.GetY()

        # Create a new feature and set the attributes
        new_feature = ogr.Feature(output_layer.GetLayerDefn())
        new_feature.SetGeometry(centroid)
        new_feature.SetField('Poly_ID', feature.GetFID())
        new_feature.SetField('Target_ID', f'MBES_{block_name}_{feature.GetFID()}')
        new_feature.SetField('Block', block_name)
        new_feature.SetField('Easting', easting)
        new_feature.SetField('Northing', northing)
        new_feature.SetField('Water_depth', water_depth)
        new_feature.SetField('Length', length)
        new_feature.SetField('Width', width)
        new_feature.SetField('Height', height)

        # Add the feature to the output layer
        output_layer.CreateFeature(new_feature)
        # new_feature = None

    # Clean up
    # input_vector = None
    # output_ds = None
