

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from com_in_ineuron_ai_utils.utils import load_classes_from_json

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def prediction(self):
        # load model
        model = load_model('best_model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (96, 96))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image/255)
        #print(result[0][0])
        temp = np.argmax(result)
        #print(temp)
        classes = load_classes_from_json()
        result = classes[str(temp)]
        return [{"image": result}]



