mass=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print ([x**2 for x in mass])
print(list(map(lambda x: x*x, mass)))