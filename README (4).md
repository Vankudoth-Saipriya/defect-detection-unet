
# 🧠 Defect Detection in Additive Manufacturing using U-Net

This project implements a semantic segmentation pipeline using a U-Net model to detect and localize various defects in grayscale images from powder bed fusion-based metal 3D printing. The goal is to automate quality inspection by identifying 11 defect types during both powder spreading and post-melting phases.

---

## 📌 Overview

- Automates defect detection in high-resolution layer-wise images.
- Trains a custom U-Net model for multi-class segmentation.
- Works on grayscale image data labeled at the pixel level.
- Targets industrial inspection in metal additive manufacturing.

---

## 🗂️ Repository Structure

| Folder/File         | Description |
|---------------------|-------------|
| `Defect Classes.docx` | Lists and describes each of the 11 defect types |
| `Result1(EDA).docx` | Exploratory Data Analysis summary and plots |
| `Results_After_Melting_UNet.docx` | Prediction results after melting phase |
| `Results_After_PowderSpread_UNet.docx` | Results on powder spread phase |
| `Training and Evaluation.docx` | Model training setup, parameters, loss, and evaluation metrics |
| `UNet Model.docx` | U-Net architecture details with figures and description |

> **Note:** Code files and datasets are not included but can be uploaded or referenced later.

---

## 🧠 Model Highlights

- **Architecture:** Custom U-Net model with skip connections for segmentation.
- **Input:** Grayscale images with annotated defect masks.
- **Loss:** Binary Cross-Entropy with Logits.
- **Metrics:** Dice Score, Intersection-over-Union (IoU), Accuracy.

---

## ⚙️ Technologies Used

- Python (PyTorch, NumPy, OpenCV)
- Jupyter for EDA and results visualization
- Documented results and analysis in `.docx` format
- Manual annotations for multi-class masks

---

## 📊 Defect Types Detected

1. Spatter  
2. Swelling  
3. Balling  
4. Keyhole Porosity  
5. Recoater Streaking  
6. Lack of Fusion  
7. Layer Shift  
8. Crater  
9. Melt Pool Anomaly  
10. Debris Inclusion  
11. Gas Porosity

---

## 📈 Results Summary

- Achieved promising Dice and IoU scores for major classes.
- Performance visualized in before–after prediction images.
- Separate evaluations for powder spread and post-melting images.

---

## 🚀 Future Work

- Upload model training code and inference script.
- Add sample datasets or links to reproducible data.
- Extend to real-time inference with OpenCV or deployment via ONNX.
- Improve performance on under-represented defect classes.

---

## 👩‍💻 Author

**Saipriya Vankudoth**  
Final-year B.Tech @ IIT  
For queries, collaboration or credits, feel free to raise issues or connect.
