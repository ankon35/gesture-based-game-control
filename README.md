# 🎮 Hill Climb Racing – Gesture Controlled with Computer Vision

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9+-red)

Control **Hill Climb Racing** with just your **hand gestures**! 🖐️  
No keyboard needed—your webcam becomes the controller.

![Demo GIF](https://github.com/yourusername/hill-climb-gesture-control/assets/demo.gif)

---

## 🎯 Gestures
- ✋ **Open hand → ACCELERATE**  
- ✊ **Closed hand → BRAKE**  

---

## 🛠 Tech Stack
- Python  
- OpenCV (cv2)  
- MediaPipe  
- PyAutoGUI  
- NumPy  
- Time  

---

## ⚙️ How It Works
1️⃣ Webcam captures live video frames.  
2️⃣ OpenCV processes each frame in real-time.  
3️⃣ MediaPipe detects **21 hand landmarks**.  
4️⃣ NumPy extracts landmark coordinates.  
5️⃣ Rule-based logic determines which gesture is made.  
6️⃣ PyAutoGUI triggers the corresponding action in the game.  

✅ Real-time performance ensures smooth, responsive gameplay.

---

## 🧠 Key Concepts
- Real-Time Image Processing  
- Hand Landmark Detection  
- Rule-Based Gesture Recognition  
- Coordinate Geometry with NumPy  
- Human-Computer Interaction (HCI)  

---

## 🚀 Installation & Run
```bash
git clone https://github.com/jiyajahnavi/hill-climb-gesture-control.git
cd hill-climb-gesture-control
pip install -r requirements.txt
python main.py
