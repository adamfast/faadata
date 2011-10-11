#!/bin/bash

# Import US airspace shapes from FADDS and SoaringWeb data.

if [ -z "$3" ]; then
	echo -e "Usage: $0 dbname FADDS-directory Soaring-File\nSoaring-File available at http://soaringweb.org/Airspace/NA/";
	exit 1;
fi
set -eu       # scripting safety net
dbname="$1"
fadds="$2"
soaring="$3"

echo -e "WARNING: This airspace data is explicitly not for navigation.\n" 1>&2


echo "Importing SoaringWeb.org airspace data.."
tmpdir=`mktemp -d "/tmp/faadata-XXXXXX"`
ogr2ogr -f "ESRI Shapefile" $tmpdir "$soaring"
shp2pgsql -d -s 4326 "$tmpdir/airspaces" sua 2> /dev/null | psql -q "$dbname" > /dev/null 2>&1
echo "delete from sua where class in ('B', 'C', 'D')" | psql -q "$dbname" > /dev/null 2>&1
rm -r "$tmpdir" 

echo "Importing FADDS shapefiles from $fadds.. "
shapefiles="$fadds/Additional_Data/Shape_Files"
for fn in class_b.shp class_c.shp class_d.shp Shape_Files_Beta_Not-for-Navigation/class_e0.shp Shape_Files_Beta_Not-for-Navigation/class_e5.shp; do
	echo "  $fn"
	shp2pgsql -d -s 4326 "$shapefiles/$fn" 2> /dev/null | psql -q "$dbname" > /dev/null 2>&1 
done

exit 0


# TODO (nelson)
#   Clean up the sua schema, make meaningful floor and ceiling
#   Consider using ogr2ogr directly to do the Postgres
#   Add an index to the geometry column?