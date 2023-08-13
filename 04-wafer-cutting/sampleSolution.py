d = int(input())
l_x, l_y = list(map(int, input().strip().split(" ")))

max_die_count = 0
best_gx = 0
best_gy = 0
radius = d // 2

for g_x in range(l_x):
	for g_y in range(l_y):
		die_count = 0
		for x1 in range(g_x - radius, radius, l_x):
			x2 = x1 + l_x
			for y1 in range(g_y - radius, radius, l_y):
				y2 = y1 + l_y
				if (x1 * x1 + y1 * y1 <= radius**2 and
					x2 * x2 + y2 * y2 <= radius**2 and
					x1 * x1 + y2 * y2 <= radius**2 and
					x2 * x2 + y1 * y1 <= radius**2):
					die_count += 1
		if die_count > max_die_count:
			max_die_count = die_count
			best_gx = g_x
			best_gy = g_y
		
print(max_die_count)