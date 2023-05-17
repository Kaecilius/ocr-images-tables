import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def thresholding(image):
    return cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)[1]

def get_text_from_image(image, config):
    # process image
    img = thresholding(image)
    text = pytesseract.image_to_string(img, lang="spa", config=config)
    words = str(text).split("\n")
    list_words = [word for word in words if len(word) > 1]
    
    return list_words


def main():
    img = cv2.imread("images/test2.jpg")
    config = r"--oem 3 --psm 6"

    print( get_text_from_image(img, config) )
   
if __name__ == "__main__":
    
    main()