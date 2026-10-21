# run `python triangle_facts.py N M` to get input facts corresponding to a graph with M nodes, with each relation sharded into N**2 pieces
import sys
import random

N = 1 if len(sys.argv) < 2 else int(sys.argv[1])
num_nodes = 1 if len(sys.argv) < 3 else int(sys.argv[2])

def coin():
    return random.choice([True, False])

# generate one of the input relations R,S,T to the program
def input_rel():
    return { (i, j) for i in range(num_nodes) for j in range(num_nodes) if coin() }

def hash_rel():
    return { (random.randint(0, N-1), random.randint(0, N-1), random.randint(0, N-1)) for _ in range(num_nodes) }

# into NxN pieces
def shard(rel):
    out = {(i, j) : set() for i in range(N) for j in range(N)}

    for (i, j) in rel:
        out[(i%N, j%N)].add((i, j))
    return out


def format_fact(relname, args):
    return { "rel": relname,
             "args": [str(arg) for arg in args],
             "node": [0, 0],
             "timestamp": 42 }

def format_rel(relname, tuples):
    return [format_fact(relname, tup) for tup in tuples]

def format_sharded_input(input_name):
    rel = shard(input_rel())
    return [fact for ((i, j), tuples) in rel.items() for fact in format_rel(input_name + str(i) + str(j), tuples)]

output = format_sharded_input("R") + format_sharded_input("S") + format_sharded_input("T") + format_rel("Hash", hash_rel())

import json

print(json.dumps(output))
