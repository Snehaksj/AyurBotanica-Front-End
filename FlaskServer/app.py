from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from pymongo import MongoClient
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
load_dotenv()

# Get MongoDB connection details from environment variables
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
try:
    client = MongoClient(MONGO_URI)  # Replace with your MongoDB connection string
    db = client[DB_NAME]  # Replace 'your_database_name' with your database name
    collection = db[COLLECTION_NAME]  # Replace 'your_collection_name' with your collection name
    print("Connected to MongoDB successfully!")
except Exception as e:
        print("Error connecting to MongoDB", e)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set up connection to MongoDB


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No image selected"})

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Dummy processing (replace this with your actual image processing logic)
        # In this example, we'll just return a dummy prediction
        dummy_prediction = [
            [0.4, "Coffee"],
            [0.2, "Beetle Leaf"],
            [0.2, "Papaya"],
            [0.1, "Aloe Vera"],
            [0.1, "Lemon"]
        ]

        # You would typically process the image here and generate your prediction

        # Return the prediction in JSON format
        return jsonify({"pred": dummy_prediction})
@app.route('/upload', methods=['POST'])
def upload():
    try:
        plant = {
            "name": "Lemon",
            "binomial_nomenclature": "Citrus limon",
            "description": "The lemon leaf, a fragrant member of the Citrus genus, is prized for its aromatic foliage and versatile uses. With its glossy, ovate leaves and petite white flowers, it adds a touch of elegance to gardens and landscapes. Native to South Asia, it has found its way into culinary, medicinal, and aromatic applications worldwide. The zesty aroma and citrusy flavor of its leaves are esteemed in cooking, herbal teas, and essential oils. Lemon leaves are also valued for their potential health benefits, including digestive support, immune enhancement, and stress relief.",
            "medicinal_values": "Lemon leaves are renowned for their potential health benefits, including digestive support, immune enhancement, and stress relief. Rich in antioxidants and essential oils, they possess antimicrobial, anti-inflammatory, and calming properties. Consumed as herbal teas or incorporated into culinary dishes, lemon leaves offer a refreshing and invigorating experience.",
            "area_found": "Lemon trees flourish in subtropical and tropical regions worldwide, including countries such as India, Italy, Spain, United States, and Australia. They thrive in warm climates with well-drained soil and ample sunlight, making them popular additions to gardens, orchards, and landscapes.",
            "best_suitable_soil": "Lemon trees prefer well-drained, slightly acidic soils with a pH range between 5.5 and 6.5. Sandy loam or loamy soils rich in organic matter are ideal for optimal growth and fruit production. Adequate moisture retention and good drainage are essential for healthy root development and overall plant vigor.",
        }
        collection.insert_one(plant)
        return jsonify({"message": "Plant details uploaded successfully"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"error uploading": str(e)})
@app.route("/fetch", methods=['POST'])
def fetch():
    try:
        plant_name = request.json.get('plant_name')
        plant_detail = collection.find_one({'name': plant_name})
        if plant_detail:
            plant_detail['_id'] = str(plant_detail['_id'])  # Convert ObjectId to string
            return jsonify({'plant_detail': plant_detail})
        else:
            return jsonify({'error': 'Plant not found'}), 404
    except Exception as e:
        print("Error fetching details", e)
        return jsonify({"error": str(e)}), 400


         


    
if __name__ == '__main__':
    app.run(debug=True)
