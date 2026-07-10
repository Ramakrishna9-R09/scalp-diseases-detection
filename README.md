# 🔬 ScalpAI — Scalp Disease Detection System

> AI-powered scalp disease detection using **MobileNetV2** + **Custom CNN** deep learning models. Detects 14 different scalp conditions with medication recommendations, doctor visit timelines, and nearby specialist information.

---

## 📁 Project Structure

```
Scalp diseases detection/
│
├── all/                          # Dataset (14 disease class folders)
│   ├── acne-keloidalis/
│   ├── alopecia-areata/
│   ├── androgenic-alopecia/
│   ├── discoid-lupus/
│   ├── dissecting-cellulitis/
│   ├── folliculitis-decalvans/
│   ├── hirsutism/
│   ├── hot-comb-alopecia/
│   ├── lichen-planopilaris/
│   ├── pseudopelade/
│   ├── telogen-effluvium/
│   ├── trichorrhexis-nodosa/
│   ├── trichotillomania/
│   └── tufted-folliculitis/
│
├── backend/
│   ├── app.py                    # Flask REST API
│   ├── train_model.py            # Model training script
│   ├── disease_info.py           # Disease database
│   ├── requirements.txt          # Python dependencies
│   └── models/                   # Trained models (auto-created)
│
├── frontend/
│   ├── index.html                # Main web app
│   ├── style.css                 # Styles
│   └── app.js                    # Frontend logic
│
├── start.bat                     # One-click startup script
└── README.md
```

---

## 🚀 Quick Start

### Option 1: One-Click Start (Windows)
```
Double-click: start.bat
```

### Option 2: Manual Setup

#### Step 1 — Install Python dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Step 2 — (Optional) Train the Models
> ⚠️ Requires GPU recommended. Without training, the app runs in **Demo/Simulation Mode**.
```bash
cd backend
python train_model.py
```
Training takes ~1-2 hours on a GPU. Models are saved to `backend/models/`.

#### Step 3 — Start the Flask API
```bash
cd backend
python app.py
```
API runs on: `http://localhost:5000`

#### Step 4 — Open the Frontend
Open `frontend/index.html` in any web browser.

---

## 🧠 AI Models

| Model | Architecture | Purpose |
|-------|-------------|---------|
| MobileNetV2 | Transfer learning (ImageNet) | Fast, accurate inference |
| Custom CNN | 5-block deep CNN | Complementary predictions |
| Ensemble | Averaged probabilities | Best accuracy (default) |

---

## 🩺 Detected Diseases (14 Classes)

| # | Disease | Severity | Urgency |
|---|---------|----------|---------|
| 1 | Acne Keloidalis Nuchae | Moderate | 14 days |
| 2 | Alopecia Areata | Moderate to Severe | 7 days |
| 3 | Androgenic Alopecia | Progressive | 30 days |
| 4 | Discoid Lupus Erythematosus | Severe | 3 days |
| 5 | Dissecting Cellulitis | Severe | 2 days |
| 6 | Folliculitis Decalvans | Moderate to Severe | 7 days |
| 7 | Hirsutism | Mild to Moderate | 30 days |
| 8 | Hot Comb Alopecia (CCCA) | Moderate | 14 days |
| 9 | Lichen Planopilaris | Severe | 5 days |
| 10 | Pseudopelade of Brocq | Moderate to Severe | 10 days |
| 11 | Telogen Effluvium | Mild to Moderate | 21 days |
| 12 | Trichorrhexis Nodosa | Mild | 30 days |
| 13 | Trichotillomania | Moderate (Psychological) | 7 days |
| 14 | Tufted Folliculitis | Moderate to Severe | 7 days |

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Server health + model status |
| `/predict` | POST | Predict disease from image |
| `/diseases` | GET | List all disease classes |
| `/doctors` | GET | Get nearby doctors list |

### Predict Endpoint
```http
POST /predict
Content-Type: multipart/form-data

image: <image file>
model: ensemble | mobilenet | cnn
```

---

## ⚠️ Disclaimer

ScalpAI is for **educational purposes only**. Always consult a qualified dermatologist or medical professional for diagnosis and treatment.

---

## 📊 Tech Stack

- **Backend**: Python, Flask, TensorFlow/Keras, PIL
- **Frontend**: HTML5, Vanilla CSS, Vanilla JavaScript
- **Models**: MobileNetV2 (Transfer Learning) + Custom CNN
- **Dataset**: 14-class scalp disease image dataset
# scalp-diseases-detection
