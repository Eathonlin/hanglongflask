from flask import Flask, render_template, request, Response, url_for
# import cv2
import VideoCamera as Video

app = Flask(__name__)

# 登入頁  檢查帳號密碼
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['name'] == "HLAD" and request.form["password"] == "1234":
            return render_template("funlist.html")
        else:
            return render_template("index.html", alertdata="密碼錯誤!!")
    return render_template("index.html")

#首頁菜單 URL連結
@app.route('/myside/<myurl>')
def Leaflet(myurl):
    return render_template(myurl + '.html')


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
    app.run(debug=True)
