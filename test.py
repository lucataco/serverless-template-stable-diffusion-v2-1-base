# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests
import base64
from io import BytesIO
from PIL import Image
import time

model_inputs = {
    'prompt': 'a photo of an astronaut riding a horse on mars',
    'negative': 'blurry'
}

# Run the model
t1 = time.time()
res = requests.post('http://localhost:8000/', json = model_inputs)
t2 = time.time()
print("Inference in ",t2-t1,"seconds")

image_byte_string = res.json()["image_base64"]
image_encoded = image_byte_string.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.jpg")