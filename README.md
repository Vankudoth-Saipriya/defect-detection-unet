# 🎭 Multimodal Emotion Detection

A complete AI system for detecting emotions from **text**, **images**, and **audio** using deep learning and natural language processing. Built with PyTorch, HuggingFace Transformers, and deployed via Streamlit.

---

## 🧠 Overview

This project combines **three powerful models** into a single system that can analyze human emotion from:
- ✍️ Written **Text**
- 📸 Facial **Image** (via file or webcam)
- 🎙️ **Audio** recordings *(coming soon)*

It supports multiple input modes, provides user-friendly interfaces, and is built for deployment.

---

## 📂 Project Structure

```
MULTIMODAL_EMOTION_DETECTION/
│
├── app.py                           # Streamlit interface
├── predict_text.py                  # Text emotion inference
├── predict_image_one.py             # Image emotion inference
├── predict_multimodal.py            # Combined model (if needed)
│
├── data/                            # Text datasets
│   ├── train.txt / val.txt / test.txt
│   └── requirements.txt             # Dependencies
│
├── image_data/                      # Image datasets
│   ├── train/ val/ test/
│   └── split_val.py
│
├── models/
│   ├── image_emotion_model/         # Trained CNN model for image
│   └── text_emotion_model/          # DistilBERT-based model
│       ├── config.json
│       ├── tokenizer.json, vocab.txt
│       └── model.safetensors
│
├── text_model_output/               # Trained checkpoints
│   ├── checkpoint-1000/
│   ├── checkpoint-2000/
│   └── checkpoint-3000/
│
├── text_model/                      # Text model code
│
├── results/                         # Output logs or prediction results
│
└── venv/                            # Virtual environment
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r data/requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

### 3. Interface Options

- 📷 **Image Input**: Upload an image or use webcam
- 📄 **Text Input**: Type your sentence to detect emotion
- 🔊 **Audio Input**: *(Planned)* Record through mic and predict

---

## 📊 Models Used

| Modality | Model                      | Library             |
|----------|----------------------------|---------------------|
| Text     | DistilBERT fine-tuned      | HuggingFace Transformers |
| Image    | Custom CNN                 | PyTorch, TorchVision |
| Audio    | *(Planned)* MFCC + CNN     | torchaudio, librosa |

---

## 🧪 Emotion Labels

- **Text**: `joy`, `sadness`, `anger`, `fear`, `surprise`, `love`
- **Image**: `happy`, `sad`, `angry`, `fear`, `disgust`, `surprise`, `neutral`

---

## 🛠️ Tech Stack

- Python 3.11
- PyTorch, HuggingFace Transformers
- OpenCV, TorchVision
- Streamlit (App deployment)
- Git, GitHub (Version control)

---

## 💡 Future Improvements

- 🎙️ Real-time audio emotion detection
- 🔀 Fuse predictions across modalities for higher accuracy
- 🌐 Deploy the app to HuggingFace Spaces or Streamlit Cloud
- 📱 Build mobile-responsive UI

---

## 🙋‍♀️ Author

**Sai Priya Vankudoth**  
🎓 B.Tech, IIT | Data Science & AI Enthusiast  
🔗 GitHub: [saipriyavankudoth](https://github.com/saipriyavankudoth)  
📧 Email: saipriyavankudoth@example.com

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
