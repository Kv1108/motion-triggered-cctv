from flask import Flask, render_template, Response, jsonify
from detector import MotionDetector


app = Flask(__name__)
motion_detector = MotionDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(motion_detector.generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start', methods=['POST'])
def start_detection():
    motion_detector.start_detection()
    return jsonify({"status": "started"})

@app.route('/stop', methods=['POST'])
def stop_detection():
    motion_detector.stop_detection()
    return jsonify({"status": "stopped"})

if __name__ == '__main__':
    app.run(debug=True)
