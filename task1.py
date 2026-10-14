
data = [(3, 3, 3), (12, 10, 10), (5, 5, 6), (1, 2, 10), (6, 6, 10), (17, 18, 19)]
counts = {"equilateral": 0, "isosceles": 0, "scalene": 0, "invalid": 0}
for a, b, c in data:
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            counts["equilateral"] += 1
        elif a == b or a == c or b == c:
            counts["isosceles"] += 1
        else:
            counts["scalene"] += 1
    else:
        counts["invalid"] += 1

print(counts)
