data = [(3, 3, 3), (12, 10, 10), (5, 5, 6), (1, 2, 10), (6, 6, 10), (17, 18, 19)]
valid_triangles = list(filter(lambda t: t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0],data))
mapped_triangles = list(map(lambda t: (t, sum(t)), valid_triangles))
print(mapped_triangles)

isosceles_triangles = list(filter(lambda item: (item[0][0] == item[0][1] or item[0][0] == item[0][2] or item[0][1] == item[0][2]) and not (item[0][0] == item[0][1] == item[0][2]),mapped_triangles))

sorted_triangles = sorted(valid_triangles, key=lambda t: sum(t))
print(sorted_triangles)
