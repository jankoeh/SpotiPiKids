#!/usr/bin/env python3

DEBOUNCE = 8

def draw_window(image, points):
    import cv2
    if points is not None:
        nrOfPoints = len(points)
        for i in range(nrOfPoints):
            nextPointIndex = (i+1) % nrOfPoints
            cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
    cv2.imshow("QR Scanner", image)
    cv2.waitKey(1)

def qr_detect_loop(framerate=2, show_window=False):

    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import cv2
    import time
    import datetime

    last_decode_time = 0

    camera = PiCamera()
    camera.resolution = (800, 600)
    camera.framerate = framerate
    camera.rotation = 90  #my pi specific
    rawCapture = PiRGBArray(camera, size=(800, 600))
    qrCodeDetector = cv2.QRCodeDetector()
    time.sleep(1) #for initialization
    last_decoded_text = ""
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        decodedText, points, _ = qrCodeDetector.detectAndDecode(gray)
        if points is not None and len(decodedText) and \
          last_decoded_text != decodedText and last_decode_time + DEBOUNCE < time.time():
            print(datetime.datetime.now(), "Detected:", decodedText)
            last_decode_time = time.time()
            handle_play_command(decodedText)
        last_decoded_text = decodedText
        if show_window:
            draw_window(image, points)
        rawCapture.truncate(0)


def handle_play_command(decoded_text):
    from spotify_if import spotify_cmd
    ret = spotify_cmd("play {}".format(decoded_text))
    if ret != 0:
        print( "Command not successfull" )


