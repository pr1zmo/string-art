from PIL import Image
from PIL import ImageOps
import numpy as np
import math
import random, cv2, sys, os

width = 480
heigth = 480
nails = 500

# θk​=θ0​+n2πk​,xk​=xc​+Rcosθk​,yk​=yc​+Rsinθk​,k=0,…,n−1.

def draw_line(color: float, x: int, y: int, img: Image):
	"""
	y = f(x) = mx + b
	where m {\displaystyle m} is the slope and b {\displaystyle b} is the y-intercept.
	Because this is a function of only x {\displaystyle x}, it can't represent a vertical line.
	Therefore, it would be useful to make this equation written as a function of both x {\displaystyle x} and y {\displaystyle y}, to be able to draw lines at any angle.
	The angle (or slope) of a line can be stated as "rise over run", or Δ y / Δ x {\displaystyle \Delta y/\Delta x}. Then, using algebraic manipulation 
	"""
	# img[x, y] = color
	# if (x == x + width/2 * math.cos())
	angle = 0
	for k in range(nails):
		angle = angle + (2 * math.pi * k) / nails
		xk = (width/2) + width / 2 * angle * math.cos(angle)
		yk = (width/2) + width / 2 * angle * math.sin(angle)
		# img[int(xk), int(yk)] = (255, 255, 255)
		if (xk <= x and yk <= y):
			img[x, y] = (255, 255, 255)


def scale(Image: any) -> np.ndarray:
	scaled = ImageOps.fit(Image, (width, heigth))
	return np.array(scaled)

def run(Image : any, name: str):
	original_img = scale(Image)
	img = np.zeros((width, heigth,3),np.uint8)

	for x in range(width):
		for y in range(heigth):
			x_c, y_p = width / 2, heigth / 2
			d = math.sqrt(math.pow(x - x_c, 2) + math.pow(y - y_p, 2))
			if d > heigth / 2:
				continue
			# img[x,y] = original_img[x, y]
			# Convert from RGB to grayscale Formula: 0.2126 R + 0.7152 G + 0.0722 B
			R, G, B = original_img[x, y]
			value = 0.2126 * R + 0.7152 * G + 0.0722 * B
			draw_line(value, x, y, img)

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