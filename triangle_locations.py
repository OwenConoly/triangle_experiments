# run `python triangle_locations.py N` to get locations for when each relation is sharded into N**2 pieces
import sys

N = int(sys.argv[1])

def shards(relname):
    return [relname + str(i) + str(j) for i in range(N) for j in range(N)]

input_relations = shards("R") + shards("S") + shards("T") + ["Hash"]
output_relations = ["Interesting"]

output = { "fact_producers": { rel: [[0, 0]] for rel in input_relations},
           "fact_consumers": { rel: [[0, 0]] for rel in output_relations} }

import json
print(json.dumps(output))
