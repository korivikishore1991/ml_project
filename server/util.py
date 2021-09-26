import pickle
import pandas as pd

"""
@author: Ranga.Korivi
"""

# global variables
__model = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    #loading Serialized Model
    with open('/usr/app/model/classifier.pkl', 'rb') as f:
        __model = pickle.load(f)
    print("loading saved model artifacts...done")

def get_estimated_class(variance, skewness, curtosis, entropy):
    return __model.predict([[int(variance), int(skewness), int(curtosis), int(entropy)]])[0]

def get_estimated_class_file(file_path):
    df = pd.read_csv(file_path)
    print("Preview if file content: \n", df.head())
    predictions = __model.predict(df)
    return str(list(predictions))

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_class('2','3','4','1'))  # other location
    print(get_estimated_class_file('/usr/app/model/testFile.csv'))

