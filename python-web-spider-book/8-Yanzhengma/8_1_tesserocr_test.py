import tesserocr
from PIL import Image

image = Image.open('CheckCode.jpg')
image = image.convert('L')
# threshold = 80
# table = []
# for i in range(256):
# 	if i < threshold:
# 		table.append(0)
# 	else:
# 		table.append(1)

WHITE, BLACK = 1, 0
image = image.point(lambda x: WHITE if x > 128 else BLACK, '1')
image.show()
result = tesserocr.image_to_text(image)
print(result)