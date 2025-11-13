from PIL import Image
from PIL import ImageOps
import numpy as np
import math
import random, cv2, sys, os, time
from tqdm import tqdm
from ctypes import cdll
from bresenham import bresenham

lib = cdll.LoadLibrary('./libfoo.so')

width = 4396
heigth = 4396
nails = 300
nail_pos = list()
thread_operations = 3000

def best_line(i, j, brightness):
   pass

def get_points(img, nails) -> np.array:
   pass

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
		a -= 1
		b -= 1
		img[a, b] = color

def scale(Image) -> np.ndarray:
	scaled = ImageOps.fit(Image, (width, heigth))
	return np.array(scaled)

def opposite_index(i: int, n: int) -> int:
	"""Index of the opposite nail on a circle with n nails (n must be even)."""
	if n % 2 != 0:
		raise ValueError("opposite_index requires an even number of nails")
	return (i + n // 2) % n

def draw_points(k, nails, img):
	angle = (2 * math.pi * k) / nails
	xk = (width/2) + (width / 2) * math.cos(angle)
	yk = (heigth/2) + (heigth / 2) * math.sin(angle)
	nail_pos.append((int(xk), int(yk)))
	img[math.ceil(xk - 1), math.ceil(yk - 1)] = (255, 255, 255)

def check_pixel(pixel) -> bool:
	return True

def run(Image, name: str):
	original_img = scale(Image)
	img = np.zeros((width, heigth,3),np.uint8)

	xk = 0
	for i in range(nails):
		draw_points(i, nails, img)

	a ,b = 0, 0
	with tqdm(total=thread_operations, desc="Drawing threads", unit="lines") as pbar:
		for z in range(thread_operations):
			pbar.set_postfix({"status": "drawing"})
			i = random.randint(0, nails - 1)
			j = random.randint(0, nails - 1)
			x1, y1 = nail_pos[i]
			x2, y2 = nail_pos[j]
			draw_line((255, 255, 255), x1, y1, x2, y2, img)
			pbar.update(1)

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