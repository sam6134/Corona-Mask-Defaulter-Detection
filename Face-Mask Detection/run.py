from flask import Flask, render_template, Response
from detect import camera_stream

app = Flask(__name__)

# the starting route
@app.route('/')
def index():
    return render_template('index.html')

# the function which generates frame by calling function camera_stream
def gen_frame():
    while True:
        frame = camera_stream()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# function to concat all video frames and display on web-app
@app.route('/video_feed')
def video_feed():

    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# start the host on local server
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)




