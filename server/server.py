from flask import Flask, request, jsonify
import util
import flasgger
from flasgger import Swagger

"""
@author: Ranga.Korivi
"""

app = Flask(__name__)
Swagger(app)


# app startUp message
@app.route('/', methods=['GET'])
def welcome():
    return 'Version2: Welcome Ready to run your code'


# posting the request and getting the prediction
#@app.route('/predict_class_var', methods=['POST', 'GET'])
def predict_class_var():
    variance = request.form['variance']
    skewness = request.form['skewness']
    curtosis = request.form['curtosis']
    entropy = request.form['entropy']
    response = jsonify({
        'estimated_class': str(util.get_estimated_class(variance, skewness, curtosis, entropy))
    })
    return response


# posting the request and getting the prediction
#@app.route('/predict_class_file', methods=['POST', 'GET'])
def predict_class_file():
    # Get the file from post request
    file_path = request.files.get("file")
    response = util.get_estimated_class_file(file_path)
    return response


# Swagger functions for frontEnd
## for args in request the in from Swagger would be query
@app.route('/predict_class_var', methods=['POST'])
def predict_note_authentication():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = str(util.get_estimated_class(variance, skewness, curtosis, entropy))
    print(prediction)
    return "Hello The answer is " + prediction


## for form databased inputs in the Swagger the in would be formData
@app.route('/predict_class_file', methods=['POST'])
def predict_note_file():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true

    responses:
        200:
            description: The output values

    """
    # Get the file from post request
    file_path = request.files.get("file")
    response = util.get_estimated_class_file(file_path)
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Docker ML classification Project...")
    util.load_saved_artifacts()
    app.run(host="0.0.0.0", port=5000)
    #app.run(debug=True)
