# ♻️ Smart Waste Classification Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![YOLO](https://img.shields.io/badge/YOLOv8-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An AI-powered waste classification system that helps identify and sort waste materials using computer vision. Built with Streamlit for an interactive dashboard experience.

---

## 📸 Dashboard Screenshots

### 🏠 Home Dashboard
![Home Dashboard](screenshots/home_dashboard.png)

### 📤 Upload & Classify
![Upload Page](screenshots/upload_page.png)

### 📊 Analytics Dashboard
![Analytics](screenshots/analytics_page.png)

### 📜 Prediction History
![History](screenshots/history_page.png)

### ⚙️ Settings
![Settings](screenshots/settings_page.png)

---

## ✨ Features

- **🤖 AI-Powered Classification** — Real-time waste classification using YOLOv8
- **📊 Interactive Dashboard** — Beautiful charts and analytics with Plotly
- **📤 Image Upload** — Drag & drop upload with instant classification
- **📜 History Tracking** — Complete prediction history with search and filters
- **📥 Data Export** — Export predictions as CSV for analysis
- **⚙️ Customizable Settings** — Configure model, display, and notification preferences
- **🎨 Beautiful UI** — Modern, responsive design with custom CSS styling

---

## 🗂️ Waste Categories

| Category | Examples | Bin Color | Recyclable |
|----------|----------|-----------|------------|
| ♻️ Plastic | Bottles, bags, containers | Yellow | ✅ Yes |
| 📄 Paper | Newspapers, cardboard, books | Blue | ✅ Yes |
| 🍶 Glass | Bottles, jars, window glass | Green | ✅ Yes |
| 🥫 Metal | Cans, foil, appliances | Gray | ✅ Yes |
| 🌱 Organic | Food scraps, leaves, wood | Brown | 🌱 Compost |
| 💻 E-Waste | Electronics, batteries, cables | Red | ⚠️ Special |
| 🗑️ Others | Textiles, rubber, mixed | Black | ❓ Check |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **AI Model** | YOLOv8 (Ultralytics) |
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **Database** | SQLite |
| **Charts** | Plotly |
| **Language** | Python 3.10+ |

---

## 📁 Project Structure

```
smart-waste-classifier/
├── app.py                      # Main Streamlit application
├── pages/
│   ├── 1_📊_Analytics.py       # Analytics dashboard page
│   ├── 2_📤_Upload.py          # Image upload & classification page
│   ├── 3_📜_History.py         # Prediction history page
│   └── 4_⚙️_Settings.py        # Settings configuration page
├── screenshots/                 # Dashboard screenshots
├── models/                      # Pre-trained YOLO models
├── data/                        # Training & test data
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/smart-waste-classifier.git
   cd smart-waste-classifier
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   Navigate to `http://localhost:8501`

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **Accuracy** | 94.2% |
| **Precision** | 93.8% |
| **Recall** | 92.5% |
| **F1 Score** | 93.1% |
| **Inference Speed** | ~23ms per image |

---

## 🔧 Configuration

The dashboard can be configured through the Settings page or by editing the configuration file:

| Setting | Default | Description |
|---------|---------|-------------|
| Confidence Threshold | 0.5 | Minimum confidence for predictions |
| Model Version | YOLOv8n | YOLO model variant |
| Theme | Light | UI color theme |
| Auto-save | True | Save predictions automatically |

---

## 📈 API Endpoints (Backend)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/classify` | Classify waste image |
| GET | `/api/predictions` | Get prediction history |
| GET | `/api/analytics` | Get analytics data |
| PUT | `/api/settings` | Update settings |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - Amazing framework for data apps
- [Ultralytics YOLOv8](https://ultralytics.com/) - State-of-the-art object detection
- [Plotly](https://plotly.com/python/) - Interactive visualization library
- Built with ❤️ for sustainable waste management

---

## 📧 Contact

**Your Name** -bhavya talluri (bhavyathalluri446@gmail.com)
Project Link: https://github.com/bhavyasri02599/smart-waste-classification-using-AI.git
