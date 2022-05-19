from PIL import UnidentifiedImageError
from flask import Flask, request, jsonify, render_template, Response
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage
from plant_education.database import insertIntoTable
from predict import plant

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = plant(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.prediction()
        return jsonify(result)
    except ValueError as val:
        print(val)
        insertIntoTable(val)
        return Response("Value not found inside json data")
    except KeyError as k:
        insertIntoTable(k)
        return Response("Key value error incorrect key passed")
    except UnidentifiedImageError as i:
        insertIntoTable("File not Found")
    except Exception as e:
        insertIntoTable(str(type(e).__name__)+str(__file__))
        return Response(str(e))


#clApp = ClientApp()
# #port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    port = 9000
    app.run(host='127.0.0.1', port=port)
    #app.run(debug=True)
