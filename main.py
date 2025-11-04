from PIL import Image
from PIL import ImageOps
import numpy as np
import math
import random, cv2, sys, os

width = 480
heigth = 480
nails = 500
nail_pos = list()

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


def draw_line(color: tuple, x, y, xe, ye, img):
	"""
	y = f(x) = mx + b
	where m  m} is the slope and b  b} is the y-intercept.
	Because this is a function of only x  x}, it can't represent a vertical line.
	Therefore, it would be useful to make this equation written as a function of both x  x} and y  y}, to be able to draw lines at any angle.
	The angle (or slope) of a line can be stated as "rise over run", or Δ y / Δ x   y/ x}. Then, using algebraic manipulation 
	"""
	# img[x, y] = color
	# if (x == x + width/2 * math.cos())
	points = bresenham(x, y, xe, ye)
	for i in points:
		a, b = i
		img[a, b] = color

def scale(Image) -> np.ndarray:
	scaled = ImageOps.fit(Image, (width, heigth))
	return np.array(scaled)

def opposite_index(i: int, n: int) -> int:
	"""Index of the opposite nail on a circle with n nails (n must be even)."""
	if n % 2 != 0:
		raise ValueError("opposite_index requires an even number of nails")
	return (i + n // 2) % n

def run(Image, name: str):
	original_img = scale(Image)
	img = np.zeros((width, heigth,3),np.uint8)

	xk = 0
	for k in range(nails):		
		angle = (2 * math.pi * k) / nails
		xk = (width/2) + (width / 2) * math.cos(angle)
		yk = (heigth/2) + (heigth / 2) * math.sin(angle)
		nail_pos.append((int(xk), int(yk)))
		img[math.ceil(xk - 1), math.ceil(yk - 1)] = (255, 255, 255)
	for t in range(10):
		# if (random.randint(1, 50) < 50):
		i = random.randint(1, 500)
		# i = int(xk)
		j = opposite_index(i, nails)
		x1, y1 = nail_pos[i]
		x2, y2 = nail_pos[j]
		draw_line((255, 0, 0), x1, y1, x2, y2, img)
		t += 1

	cv2.imwrite("string_" + name,img)

def check_file(path: str) -> bool:
	_ext = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
	return os.path.isfile(path) and path.lower().endswith(tuple(_ext))

def getImage() -> str:
	if len(sys.argv) != 2:
		raise ValueError("Error: Please provide exactly one image file as argument")
	if not check_file(sys.argv[1]):
		raise ValueError("Error opening image")
	return sys.argv[1]

if __name__ == "__main__":
	try:
		img = getImage()
		with Image.open(img) as image:
			run(image, sys.argv[1])
	except Exception as e:
		print(f"Error: {e}")