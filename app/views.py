import os

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as Image
import numpy as np
from app.models import Predictions, ImagePath
# Create your views here.



def home(request):
    return render(request, 'index.html')


def predict(request):
    if request.method == 'POST':
        try:
            folder = 'media/images/'
            image = request.FILES['cd']
            print('image name is: ',image.name)

            file_name = str(image.name)
            fs = FileSystemStorage(location = folder)
            name = fs.save(image.name, image)

            media_path = folder + "{}"
            file_path = os.path.join(media_path).format(name)
            print('the file path is ',file_path)

            #Loading the model
            print('model is loding............')
            print("tf version",tf.__version__)
            model = tf.keras.models.load_model('model.h5')
            print('model is loaded! ')
            print('model summary is', model.summary())
            image = Image.load_img(file_path, target_size= (227,227))
            image = Image.img_to_array(image)
            # print(image)
            image = np.expand_dims(image, axis = 0)
            # print(image)


            #Prediction
            r = np.argmax(model.predict(image))
            result = model.predict(image)
            print("the results are!",r, type(r))
            if r == 7:


            img_path = ImagePath()
            img_path.path = file_path
            img_db = Predictions()
            img_db.image_path = file_path
            #img_db.prediction= pred
            img_db.save()
            return render(request, "results.html", {'image_source': img_path})


        except Exception as e:
            print('error is', e )

    else:
        return render(request, 'index.html')