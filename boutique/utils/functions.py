from PIL import Image
from io import BytesIO

def compressImage(image_file, format="JPEG", quality=80, max_width=800, close_file=True):
	output_image_stream = None
	image = Image.open(image_file)

	original_width, original_height = image.size

	width = min(max_width, original_width)
	height = int((width / original_width) * original_height)

	image = image.resize((width, height))

	output_image_stream = BytesIO()

	image.save(output_image_stream, format=format, quality=80)

	output_image_stream.seek(0)
	
	if close_file:
		image_file.close()

	return output_image_stream