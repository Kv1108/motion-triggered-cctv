

```markdown
# 📹 Motion Triggered CCTV Recognition System

A Python-based smart CCTV system that uses a webcam to detect motion (faces or bodies) using OpenCV. When motion is detected, it records a video clip and saves it with a timestamp. The recording stops after a few seconds of no motion being detected.

---

## 🧠 Features

- 🔍 **Real-time face and body detection** using Haar Cascade classifiers  
- 🎥 **Automatic video recording** on motion detection  
- ⏱ **5-second post-detection delay** before stopping the recording  
- 💾 **Saves videos with timestamped filenames**  
- 🖼 **Visual feedback** with rectangles around detected objects  
- 🧪 Built with OpenCV for computer vision tasks  

---

## 📁 Project Structure

```

motion-triggered-cctv/
│
├── CCTV.py               # Main script for detection and recording
├── utils.py              # Utility for folder creation
├── recorded\_videos/      # Output directory (auto-created if not present)
└── README.md             # Project documentation

````

---

## 🛠️ Requirements

- Python 3.6 or higher  
- OpenCV (`opencv-python`)  

### Install Required Packages

```bash
pip install opencv-python
````

---

## 🚀 How to Run

### 1. Clone or Download the Repository

```bash
git clone https://github.com/YOUR_USERNAME/motion-triggered-cctv.git
cd motion-triggered-cctv
```

Or manually download and extract the ZIP.

---

### 2. Make Sure `utils.py` Contains:

```python
import os

def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
```

---

### 3. Run the Script

```bash
python CCTV.py
```

### 4. Use the Program

* A window titled **"Camera"** will open showing your webcam feed.
* The script detects **faces** and **full bodies**.
* When motion is detected:

  * A video starts recording.
  * It saves in the `recorded_videos/` folder with a timestamped filename.
* If there's no motion for 5 seconds, recording stops.
* Press `q` to quit the application.

---

## 🖼️ Example Output

```bash
Started Recording: recorded_videos/01-06-2025-10-30-12.mp4
Stopped Recording!
```

Videos are saved in `recorded_videos/`.


