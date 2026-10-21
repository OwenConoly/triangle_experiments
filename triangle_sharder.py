# run `python triangle_sharder.py N` to get a program with each relation sharded into N**2 pieces
import sys

N = 1 if len(sys.argv) < 2 else int(sys.argv[1])

for i in range(N):
    for j in range(N):
        print(f".decl R{i}{j}(x: number, y: number)")
        print(f".decl S{i}{j}(x: number, y: number)")
        print(f".decl T{i}{j}(x: number, y: number)")

for i in range(N):
    for j in range(N):
        for k in range(N):
            print(f".decl Triangle{i}{j}{k}(x: number, y: number, z: number)")

print(".decl Hash(x: number, y: number, z: number)")

print()
print()

for i in range(N):
    for j in range(N):
        for k in range(N):
            print(f"Triangle{i}{j}{k}(x, y, z) :- R{i}{j}(x, y), S{j}{k}(y, z), T{k}{i}(z, x).")
            print(f"Interesting(x, y, z) :- Triangle{i}{j}{k}(x, y, z), Hash(x, y, z).")
