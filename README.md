# **Real-Time Face Recognition System**  

This project implements a real-time face recognition system utilizing OpenCV, the `face_recognition` library, and text-to-speech capabilities (`pyttsx3`).  

## **Key Features**  
- **Real-Time Face Detection**: Captures and detects faces using a webcam.  
- **Facial Recognition**: Identifies pre-registered individuals from a known dataset.  
- **Logging Mechanism**: Stores detection records in `data/face_detections.csv` for audit and analysis.  
- **Text-to-Speech Feedback**: Provides audible responses upon face recognition.  

## **Installation & Setup**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/manpritxelentor/facedectionsystem.git
cd facedectionsystem
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3. Run the Application**  
```bash
python src/main.py
```
