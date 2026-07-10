"""
Scalp Disease Detection - Flask REST API
Serves predictions from MobileNetV2 + CNN models with simulation fallback.
"""
import os, random, time
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from disease_info import DISEASE_INFO

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

# ── Config ────────────────────────────────────────────────────────────────────
IMG_SIZE   = 224
MODEL_DIR  = os.path.join(os.path.dirname(__file__), 'models')
CLASSES    = [
    'acne-keloidalis', 'alopecia-areata', 'androgenic-alopecia',
    'discoid-lupus', 'dissecting-cellulitis', 'folliculitis-decalvans',
    'hirsutism', 'hot-comb-alopecia', 'lichen-planopilaris',
    'pseudopelade', 'telogen-effluvium', 'trichorrhexis-nodosa',
    'trichotillomania', 'tufted-folliculitis'
]

cnn_model       = None
mobilenet_model = None
simulation_mode = False

# ── Load Models ───────────────────────────────────────────────────────────────
def load_models():
    global cnn_model, mobilenet_model, simulation_mode
    try:
        import tensorflow as tf
        cnn_path = os.path.join(MODEL_DIR, 'cnn_model.h5')
        mn_path  = os.path.join(MODEL_DIR, 'mobilenet_model.h5')
        if os.path.exists(cnn_path):
            cnn_model = tf.keras.models.load_model(cnn_path)
            print("[OK] CNN model loaded")
        if os.path.exists(mn_path):
            mobilenet_model = tf.keras.models.load_model(mn_path)
            print("[OK] MobileNetV2 model loaded")
        if cnn_model is None and mobilenet_model is None:
            simulation_mode = True
            print("[!] No trained models found. Running in SIMULATION mode.")
    except Exception as e:
        simulation_mode = True
        print(f"[!] TF load error: {e}. Running in SIMULATION mode.")

# ── Preprocess Image ──────────────────────────────────────────────────────────
def preprocess_image(file_storage):
    img = Image.open(file_storage).convert('RGB')
    img = img.resize((IMG_SIZE, IMG_SIZE))
    arr = np.array(img, dtype=np.float32)
    return np.expand_dims(arr, 0)

# ── Simulate Prediction ───────────────────────────────────────────────────────
def simulate_prediction(model_type='ensemble'):
    """Realistic-looking simulation when models aren't trained yet."""
    primary = random.randint(0, len(CLASSES) - 1)
    probs   = np.random.dirichlet(np.ones(len(CLASSES)) * 0.3)
    probs[primary] += 0.4
    probs   = probs / probs.sum()
    return probs, "simulation"

# ── Real Prediction ───────────────────────────────────────────────────────────
def predict_image(img_array, model_type='ensemble'):
    import tensorflow as tf
    if model_type == 'mobilenet' and mobilenet_model:
        preds = mobilenet_model.predict(img_array, verbose=0)[0]
        return preds, 'mobilenet'
    elif model_type == 'cnn' and cnn_model:
        preds = cnn_model.predict(img_array, verbose=0)[0]
        return preds, 'cnn'
    elif model_type == 'ensemble':
        results = []
        if mobilenet_model:
            results.append(mobilenet_model.predict(img_array, verbose=0)[0])
        if cnn_model:
            results.append(cnn_model.predict(img_array, verbose=0)[0])
        if results:
            preds = np.mean(results, axis=0)
            return preds, 'ensemble'
    return simulate_prediction(model_type)

# ── Nearby Doctors Data ───────────────────────────────────────────────────────
DOCTORS_DB = [
    {"name": "Dr. Priya Sharma", "specialty": "Dermatologist & Trichologist",
     "hospital": "Apollo Skin & Hair Clinic", "rating": 4.9, "reviews": 342,
     "distance": "1.2 km", "phone": "+91-98765-43210",
     "available": "Mon-Sat 10AM-6PM", "fee": "₹800",
     "image_color": "#6C63FF", "experience": "15 years"},
    {"name": "Dr. Rahul Verma", "specialty": "Hair Specialist & Surgeon",
     "hospital": "Fortis Hair Restoration Centre", "rating": 4.8, "reviews": 287,
     "distance": "2.5 km", "phone": "+91-87654-32109",
     "available": "Mon-Fri 9AM-5PM", "fee": "₹1200",
     "image_color": "#00C9FF", "experience": "12 years"},
    {"name": "Dr. Ananya Menon", "specialty": "Cosmetic Dermatologist",
     "hospital": "Manipal Skin Care Institute", "rating": 4.7, "reviews": 198,
     "distance": "3.8 km", "phone": "+91-76543-21098",
     "available": "Tue-Sun 11AM-7PM", "fee": "₹950",
     "image_color": "#FF6B9D", "experience": "10 years"},
    {"name": "Dr. Kiran Patel", "specialty": "Trichologist & Scalp Specialist",
     "hospital": "Skin & Hair Lab", "rating": 4.6, "reviews": 156,
     "distance": "4.1 km", "phone": "+91-65432-10987",
     "available": "Mon-Sat 8AM-4PM", "fee": "₹700",
     "image_color": "#43E97B", "experience": "8 years"},
    {"name": "Dr. Meera Joshi", "specialty": "Dermatologist",
     "hospital": "City Dermatology Hospital", "rating": 4.5, "reviews": 224,
     "distance": "5.0 km", "phone": "+91-54321-09876",
     "available": "Mon-Fri 10AM-5PM", "fee": "₹600",
     "image_color": "#FA709A", "experience": "11 years"},
    {"name": "Dr. Arun Krishnan", "specialty": "Hair & Scalp Specialist",
     "hospital": "AIIMS Dermatology OPD", "rating": 4.9, "reviews": 512,
     "distance": "6.3 km", "phone": "+91-43210-98765",
     "available": "Mon-Sat 8AM-2PM", "fee": "₹500",
     "image_color": "#4FACFE", "experience": "20 years"},
]

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "simulation_mode": simulation_mode,
        "cnn_loaded": cnn_model is not None,
        "mobilenet_loaded": mobilenet_model is not None,
        "classes": len(CLASSES)
    })

@app.route('/diseases', methods=['GET'])
def list_diseases():
    return jsonify([
        {"key": k, "name": v["name"], "severity": v["severity"]}
        for k, v in DISEASE_INFO.items()
    ])

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    model_type = request.form.get('model', 'ensemble')
    file = request.files['image']
    ext  = file.filename.rsplit('.', 1)[-1].lower() if '.' in file.filename else ''
    if ext not in ['jpg', 'jpeg', 'png', 'bmp', 'webp']:
        return jsonify({"error": "Unsupported image format"}), 400

    start = time.time()
    try:
        if simulation_mode:
            probs, used_model = simulate_prediction(model_type)
        else:
            img_array        = preprocess_image(file)
            probs, used_model = predict_image(img_array, model_type)

        top_idx = int(np.argmax(probs))
        top_class = CLASSES[top_idx]
        confidence = float(probs[top_idx])

        top3 = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)[:3]
        top3_results = [
            {"disease": CLASSES[i], "name": DISEASE_INFO[CLASSES[i]]["name"],
             "confidence": round(float(p) * 100, 2)}
            for i, p in top3
        ]

        info = DISEASE_INFO[top_class]
        elapsed = round(time.time() - start, 3)

        return jsonify({
            "success": True,
            "model_used": used_model,
            "simulation_mode": simulation_mode,
            "inference_time": elapsed,
            "prediction": {
                "disease_key": top_class,
                "disease_name": info["name"],
                "confidence": round(confidence * 100, 2),
                "severity": info["severity"],
                "urgency_level": info["urgency_level"],
                "urgency_color": info["urgency_color"],
                "days_to_doctor": info["days_to_doctor"],
                "description": info["description"],
                "symptoms": info["symptoms"],
                "medications": info["medications"],
                "home_care": info["home_care"],
                "specialist": info["specialist"],
            },
            "top3": top3_results,
            "doctors": DOCTORS_DB
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify(DOCTORS_DB)

# ── Start ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    load_models()
    print("\n[OK] Flask API running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
