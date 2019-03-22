import cv2
from flask import Flask, render_template, request, Response
import VideoCamera as Video

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['name'] == "HLAD" and request.form["password"] == "1234":
            return render_template("image.html")
        else:
            return render_template("index.html", alertdata="密碼錯誤!!")
    return render_template("index.html")


def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator 輸出視訊， 每次输出的content=image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/image')
def image():
    return Response(gen(Video.VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
