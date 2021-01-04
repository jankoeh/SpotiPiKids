#!/usr/bin/env python3

"""
Uses OpenCV for QR Code reading from Raspberry PI cameria
"""

DEBOUNCE = 8

def draw_window(image, points):
    """
    Draw window from camera image, mark QR code
    """
    import cv2
    if points is not None:
        nr_of_points = len(points)
        for i in range(nr_of_points):
            next_index = (i+1) % nr_of_points
            cv2.line(image, tuple(points[i][0]), \
                     tuple(points[next_index][0]), (255, 0, 0), 5)
    cv2.imshow("QR Scanner", image)
    cv2.waitKey(1)

def qr_detect_loop(framerate=2, show_window=False):
    """
    Starts an infinite loop to read QR codes
    """
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
    raw_capture = PiRGBArray(camera, size=(800, 600))
    qr_code_detector = cv2.QRCodeDetector()
    time.sleep(1) #for initialization
    last_decoded_text = ""
    for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        decoded_text, points, _ = qr_code_detector.detectAndDecode(gray)
        if points is not None and decoded_text and \
          last_decoded_text != decoded_text and last_decode_time + DEBOUNCE < time.time():
            print(datetime.datetime.now(), "Detected:", decoded_text)
            last_decode_time = time.time()
            handle_play_command(decoded_text)
        last_decoded_text = decoded_text
        if show_window:
            draw_window(image, points)
        raw_capture.truncate(0)


def handle_play_command(decoded_text):
    """
    Execute play command with given title
    """
    from spotify_if import spotify_cmd
    ret = spotify_cmd("play {}".format(decoded_text))
    if ret != 0:
        print("Command not successfull")
