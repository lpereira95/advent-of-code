from part2 import load_solution

sol = load_solution('test.dat')

i, j = 0, 1
print(sorted(sol, key=lambda x: (x[i], x[j])))
