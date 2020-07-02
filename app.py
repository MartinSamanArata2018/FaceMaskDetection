from pytorch_infer import run_on_video
import serial


def send_message_arduino():
    arduino.write(b'Mask')


def print_message_arduino():
    print(arduino.readlines())


if __name__ == '__main__':
    arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)
    run_on_video(0, '', conf_thresh=0.5, do_detect=send_message_arduino, do_running=print_message_arduino)
    arduino.close()
