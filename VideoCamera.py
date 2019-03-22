import cv2


# 連結視訊
class VideoCamera(object):
    def __init__(self):
        # 開啟視訊
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # 關閉視訊
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 用motion JPEG模式先將圖片轉成jpg格式
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
