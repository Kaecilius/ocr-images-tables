import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def main():
    img = cv2.imread("images/test2.jpg")
    gray = get_grayscale(img)

    # thresh = thresholding(gray)
    custom_config = r"--oem 3"
    text = pytesseract.image_to_string(gray, lang = "spa", config=custom_config)
    print( text )

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    print(d.keys())

if __name__ == "__main__":
    main()
    # img = cv2.imread("images/test2.jpg")

    # h, w, c = img.shape
    # boxes = pytesseract.image_to_boxes(img) 
    # for b in boxes.splitlines():
    #     b = b.split(' ')
    #     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    # cv2.imshow('img', img)
    # cv2.waitKey(0)