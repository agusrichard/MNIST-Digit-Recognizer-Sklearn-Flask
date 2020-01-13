import re
import io
import base64
import pickle
import numpy as np
from PIL import Image 

def convert_image(image_url):
	img_size = 28, 28
	image_string = re.search(r'base64,(.*)', image_url).group(1)  
	image_bytes = io.BytesIO(base64.b64decode(image_string)) 
	image = Image.open(image_bytes) 
	image = image.resize(img_size, Image.ANTIALIAS)  
	image = image.convert('1')
	image_array = np.asarray(image)
	image_array = image_array.flatten()
	image_array = image_array.reshape(1, -1)

	print("image_array.shape: ", image_array.shape) 

	return image_array

def make_prediction(image_array, loaded_model):
	prediction = loaded_model.predict(image_array)
	prediction = int(prediction[0])

	print("Prediction: ", prediction)

	return prediction