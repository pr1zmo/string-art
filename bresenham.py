def bresenham(x0, y0, x1, y1):
	"""Return list of integer (x, y) points on the line from (x0,y0) to (x1,y1)."""
	points = []

	dx = abs(x1 - x0)
	dy = abs(y1 - y0)

	x, y = x0, y0
	sx = 1 if x1 >= x0 else -1   # step for x
	sy = 1 if y1 >= y0 else -1   # step for y

	if dy <= dx:
		err = dx // 2            # initial error term
		while x != x1:
			points.append((x, y))
			err -= dy
			if err < 0:
				y += sy
				err += dx
			x += sx
		points.append((x1, y1))
	else:
		err = dy // 2
		while y != y1:
			points.append((x, y))
			err -= dx
			if err < 0:
				x += sx
				err += dy
			y += sy
		points.append((x1, y1))

	return points