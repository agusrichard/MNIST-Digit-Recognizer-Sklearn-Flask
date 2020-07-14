from flask import Flask, render_template, url_for, request, jsonify
import pickle
from .utilities import convert_image, make_prediction

app = Flask(__name__)

loaded_model = pickle.load(open('app/model/finalized_model.sav', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
	prediction = None;
	if request.method == 'POST':
		image_url = request.values['imageBase64']
		image_array = convert_image(image_url)
		prediction = make_prediction(image_array, loaded_model)

		return jsonify(prediction=prediction)

	return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
	app.run(debug=True)


