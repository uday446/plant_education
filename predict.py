from flask import Flask, request, jsonify, render_template, Response
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from com_in_ineuron_ai_utils.utils import load_classes_from_json
from plant_education.database import insertIntoTable


class plant:
    def __init__(self,filename):
        self.filename =filename
        self.model = load_model('best_model.h5')

    def prediction(self):
        try:
            imagename = self.filename
            test_image = image.load_img(imagename, target_size = (96, 96))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = self.model.predict(test_image/255)
            temp = np.argmax(result)
            classes = load_classes_from_json()
            result = classes[str(temp)]
            return [{"image": result}]
        except ValueError as val:
            print(val)
            insertIntoTable(val)
            return Response("Value not found inside  json data")
        except KeyError as k:
            insertIntoTable(k)
            return Response("Key value error incorrect key passed")
        except Exception as e:
            insertIntoTable(str(type(e).__name__)+str(__file__))
            return Response(str(e))



