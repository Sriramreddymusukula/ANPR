from ultralytics import YOLO
import cv2
import pytesseract
import re

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load YOLO model
model = YOLO("models/best.pt")


def detect_number_plate(image_path):

    # Read image
    img = cv2.imread(image_path)

    # Run YOLO
    results = model(img)

    print("Results:", results)

    plate_text = "No Plate Detected"

    for result in results:

        boxes = result.boxes

        print("Boxes found:", len(boxes))

        for box in boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Add more padding around plate
            x1 = max(0, x1 - 50)
            y1 = max(0, y1 - 30)
            x2 = min(img.shape[1], x2 + 50)
            y2 = min(img.shape[0], y2 + 30)

            print("Coordinates:", x1, y1, x2, y2)

            # Crop plate
            plate = img[y1:y2, x1:x2]

            # Save cropped image
            cv2.imwrite("output/cropped_plate.jpg", plate)

            # Convert to grayscale
            gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)

            # Enlarge image
            gray = cv2.resize(gray, None, fx=10, fy=10)

            # Remove noise
            gray = cv2.bilateralFilter(gray, 11, 17, 17)

            # Threshold
            _, thresh = cv2.threshold(
                gray,
                150,
                255,
                cv2.THRESH_BINARY
            )

            # Save preprocessed image
            cv2.imwrite("output/preprocessed_plate.jpg", thresh)

            # OCR configuration
            custom_config = r'--oem 3 --psm 7'

            # OCR
            text = pytesseract.image_to_string(
                thresh,
                config=custom_config
            )

            print("OCR Raw Text:", text)
            print("repr =", repr(text))

            # Clean output
            plate_text = re.sub(r'[^A-Z0-9]', '', text.upper())

            # Common OCR corrections
            plate_text = (
                plate_text
                .replace("O", "0")
                .replace("I", "1")
                .replace("S", "5")
            )

            if len(plate_text) < 4:
                plate_text = "OCR Failed"

            break

    return plate_text