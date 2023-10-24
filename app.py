from flask import Flask, render_template, request
import base64
import os

# --------------------- Define Prediction Models for Dog, Human, and Dog Breed Prediction ------------------------ # 

def dog_detector(img_path: str) -> bool:
    return True if img_path.lower() == 'dog' else False

def face_detector(img_path: str) -> bool:
    return True if img_path.lower() == 'human' else False

def VGG19_predict_mixbreed(img_path: str):
    # Mock Data Structure
    return True

# --------------------- Define Web Application for Dog Classification Model ------------------------ # 

app = Flask(__name__)

UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET'])
def display_landing_page():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        image_file = request.files['imagefile']
        if image_file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(image_path)

            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
                image_base64 = base64.b64encode(image_data).decode('utf-8')

            # Run the Prediction Model (from Kaggle) and pass as input in the 
            # For testing Dog Detection
            isDogDetected = dog_detector('Dog')
            isHumanDetected = face_detector('No')
            dogBreedPrediction = VGG19_predict_mixbreed('John')
            # For testing Human Detection
            # isDogDetected = dog_detector('No')
            # isHumanDetected = face_detector('Human')
            # dogBreedPrediction = VGG19_predict_mixbreed('John')
            first_breed_prob = 0.999

            # For testing Neither Dog or Human
            isDogDetected = dog_detector('No')
            isHumanDetected = face_detector('No')
            dogBreedPrediction = VGG19_predict_mixbreed('John')

            if isDogDetected:
                if first_breed_prob < 0.99:
                    return render_template('mixbreed_prediction.html', image_base64=image_base64, race='Mixbreed Dog')
                else:
                    return render_template('dogbreed_prediction.html', image_base64=image_base64, race='Dog')
                
            elif isHumanDetected:
                return render_template('human_prediction.html', image_base64=image_base64, race='Human')
            
            else:
                return render_template('neither_prediction.html', image_base64=image_base64, race='Alien')


    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)