from flask import Flask, request, jsonify, render_template
import io
from model import load_model, preprocess_image, postprocess_image
from PIL import Image
import torch

# Initialize the Flask app
app = Flask(__name__)

# Load both the models when the server starts
G_AB = load_model('generator_ab_epoch_4.pth')  # For face to sketch
G_BA = load_model('generator_ba_epoch_4.pth')  # For sketch to face

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for image conversion
@app.route('/convert', methods=['POST'])
def convert_image():
    file = request.files['file']  # Get the uploaded file
    img = Image.open(file.stream).convert('RGB')  # Open the image and convert to RGB

    # Preprocess the image
    input_image = preprocess_image(img)

    # Check which type of conversion to apply
    conversion_type = request.form['type']
    
    with torch.no_grad():  # Disable gradient calculation for inference
        if conversion_type == 'face_to_sketch':
            output_image = G_AB(input_image)  # Convert face to sketch
        elif conversion_type == 'sketch_to_face':
            output_image = G_BA(input_image)  # Convert sketch to face
        else:
            return jsonify({"error": "Invalid conversion type"}), 400

    # Post-process the output to convert it back to an image
    output_image = postprocess_image(output_image)

    # Convert the output image to bytes
    img_byte_arr = io.BytesIO()
    output_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Return the image as a response
    return img_byte_arr, 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=True)
