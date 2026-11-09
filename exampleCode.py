import cv2
from flask import Flask, render_template, Response

app = Flask(__name__) #maak flask app

camera = cv2.VideoCapture(0) #camera


def makeFrames():
    if(not camera.isOpened()) : #als de camera niet geopend kan worden -> sluit programma af
        print("Can't open camera")
        exit()
    while True:
        success, frame = camera.read() #succes = is de frame capture gelukt, frame = de gecapturede frame
        if not success:
            print("Can't recieve frame")
            continue
        success, buffer = cv2.imencode('.jpg', frame) #succes = is de omzetting gelukt, buffer = de frame omgezet naar.jpg
        frameBytes = buffer.tobytes() #buffer omgezet naar bytes
        
        yield (b'--frame\r\n' #lijk een return maar sluit de functie niet af en returned een stream indeplaats van 1 waarde
            b'Content-Type: image/jpeg\r\n\r\n' + frameBytes
            + b'\r\n\r\n')

@app.route('/video') #op /video krijg je de video functie te zien
def video():
    return Response(makeFrames(), mimetype='multipart/x-mixed-replace; boundary=frame') #Response = wat flask moet returnen aan de browser, mimetype = welke soort inhoud de browser ontvangt

if __name__ == '__main__': #als het gerund wordt als hoofdprogramma
    app.run(port = 5000, debug = True, threaded = True)