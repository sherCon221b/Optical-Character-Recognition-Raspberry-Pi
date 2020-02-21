from PIL import Image
import pytesseract
import cv2 

src_path = "/home/pi/Desktop/"
captured_img_path = src_path + 'captured_img.jpeg'

def resize(img, scale):
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)
    res_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return res_img

def captureImage():
    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        frame =  resize(frame, 70)
        cv2.imwrite(str(captured_img_path), frame)
        cap.release()
    except:
        print("Camera Error")

# capture image to recognise
captureImage()

# load the example image and convert it to grayscale
image = cv2.imread(captured_img_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply thresholding to preprocess the image
thres_gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# write the grayscaled image and apply OCR
thres_img = src_path + "gray_output.jpeg"
cv2.imwrite(str(thres_img), thres_gray)

text = pytesseract.image_to_string(Image.open(captured_img_path).convert("RGB"), lang = 'eng')
print(text)

# show the output image
cv2.imshow("Output", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()