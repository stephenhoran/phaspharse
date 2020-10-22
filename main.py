from PIL import ImageGrab, ImageOps
import keyboard
import time
import pytesseract


def main():
    while True:
        if keyboard.is_pressed('page down'):
            print("Snapping Screenshot...")
            img = ImageGrab.grab().resize((3840, 1080)).convert('LA')
            gray = ImageOps.grayscale(img)
            gray.save('screen_capture.jpg')

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
            print(pytesseract.image_to_string(r'screen_capture.jpg'))

        time.sleep(.1)


if __name__ == '__main__':
    main()