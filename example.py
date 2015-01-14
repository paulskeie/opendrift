#!/usr/bin/env python

from readers import reader_basemap_landmask
from readers import reader_netCDF_CF_generic
from openDriftSimulation import *

o = OpenDriftSimulation()

# Landmask (Basemap)
reader_basemap = reader_basemap_landmask.Reader(llcrnrlon=-3, llcrnrlat=59,
                    urcrnrlon=10, urcrnrlat=67, resolution='i')
o.readers.add_reader(reader_basemap, name='basemap_landmask')

# Arome
reader_arome = reader_netCDF_CF_generic.Reader('http://thredds.met.no/thredds/dodsC/arome25/arome_metcoop_default2_5km_latest.nc')
o.readers.add_reader(reader_arome, name='arome_thredds')

# Norkyst
reader_norkyst = reader_netCDF_CF_generic.Reader('http://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
o.readers.add_reader(reader_norkyst, name='norkyst800_thredds')

# Arctic20
reader_arctic20 = reader_netCDF_CF_generic.Reader('http://thredds.met.no/thredds/dodsC/sea/arctic20km/1h/aggregate_be')
o.readers.add_reader(reader_arctic20, name='arctic20_thredds')

# Test Reader
print o.readers.list_environment_variables()

#o.get_environment(['x_wind', 'y_wind', 'salinity'], 0,0,0,0)

for reader in o.readers.readers:
    #print reader.startTime, reader.endTime
    #print reader.proj4
    print reader

#for r in o.readers:
#    print r().proj4