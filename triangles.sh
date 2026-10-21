# $1 is shard amt
# $2 is fact amt
the_dir=triangle_$1_shards_$2_facts
rm -r $the_dir
mkdir $the_dir
python triangle_sharder.py $1 $2 > $the_dir/triangles.dl
python triangle_facts.py $1 $2 > $the_dir/facts.json
python triangle_locations.py $1 > $the_dir/locations.json
