import os
import time
import picamera


path = os.path.join(os.path.dirname(os.path.realpath(__file__)))


def snap():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        for filename in camera.capture_continuous(os.path.join(path, 'pics', 'img_{timestamp:%Y-%m-%d-%H-%M-%S-%f}.jpg')):
            print('captured %s' % filename)
            time.sleep(1)

if __name__ == '__main__':
    snap()

