Automatic Number Plate Recognition System using YOLOv8 and Tesseract OCR 
Overview 
This project is an Automatic Number Plate Recognition (ANPR) system developed using Python. It 
detects vehicle number plates from images using YOLOv8 and extracts the plate number using 
Tesseract OCR. The system provides a graphical user interface (GUI) built with CustomTkinter and 
maintains a history of detections in a CSV database. 
Features 
• Upload vehicle images 
• Number plate detection using YOLOv8 
• Character recognition using Tesseract OCR 
• Image preprocessing and post-processing 
• Detection history with date and time 
• Automatic CSV database storage 
• Vehicle image saving 
• Output folder viewer 
• User-friendly GUI with image preview 
�
� Technologies Used 
• Python 3.12 
• YOLOv8 (Ultralytics) 
• OpenCV 
• Tesseract OCR 
• Pandas 
• CustomTkinter 
• Pillow (PIL) 
Project Structure 
NumberPlateRecognition/ 
│ 
├── gui.py 
├── detector.py 
├── database.py 
├── history.py 
├── vehicle_database.csv 
│ 
├── models/ 
│   └── best.pt 
│ 
├── output/ 
│   ├── cropped_plate.jpg 
│   ├── preprocessed_plate.jpg 
│   └── detected_vehicle_*.jpg 
│ 
└── README.md 
 
⚙ Workflow 
Image Upload 
      ↓ 
YOLOv8 Plate Detection 
      ↓ 
Crop Number Plate 
      ↓ 
Image Preprocessing 
      ↓ 
Tesseract OCR 
      ↓ 
Post Processing 
      ↓ 
Detected Plate Number 
      ↓ 
CSV Database Storage 
 
        How to Run 
1. Activate virtual environment: 
venv\Scripts\activate 
2. Install dependencies: 
pip install ultralytics opencv-python pytesseract pandas pillow customtkinter 
3. Run the application: 
python gui.py 
 
      Sample Output 
Detected Plate: 
TG257602 
Detection history is automatically stored in: 
vehicle_database.csv 
 
      Future Enhancements 
• Real-time camera support 
• Cloud database integration 
• Multi-vehicle detection 
• Advanced OCR models 
• Vehicle tracking system 
• Parking management integration 
 
                        Developed By 
Musukula Sriram Reddy 
B.Tech CSE (AI & ML) 
CMR Technical Campus (CMRTC)
