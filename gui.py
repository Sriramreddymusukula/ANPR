import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
from detector import detect_number_plate
from database import save_to_database
from history import get_history, get_image_path
import os

# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()
app.title("Number Plate Recognition System")
app.geometry("1400x800")

selected_image = None
current_plate = ""


# Upload Function
def upload_image():
    global selected_image

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if file_path:
        img = Image.open(file_path)

        img.thumbnail((700, 500))

        photo = ImageTk.PhotoImage(img)

        image_label.configure(image=photo, text="")
        image_label.image = photo

        selected_image = file_path


# Detect Function
def detect_plate():

    global selected_image
    global current_plate

    if selected_image:

        plate = detect_number_plate(selected_image)

        current_plate = plate

        if plate != "No Plate Detected" and plate != "OCR Failed":

            save_to_database(plate, selected_image)

            history_label.configure(
                text=get_history()
            )

        result_label.configure(
            text=f"Detected Plate:\n{plate}"
        )


# View Last Vehicle Image
# Open Output Folder
def view_last_image():

    if os.path.exists("output"):

        os.startfile("output")

    else:

        print("Output folder not found")

# Title
title = ctk.CTkLabel(
    app,
    text="🚗 Number Plate Recognition System",
    font=("Arial", 32, "bold")
)
title.pack(pady=20)

# Main Frame
main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Left Frame
left_frame = ctk.CTkFrame(main_frame, width=300)
left_frame.pack(side="left", fill="both", expand=False, padx=20, pady=20)

# Upload Button
upload_btn = ctk.CTkButton(
    left_frame,
    text="Upload Image",
    width=220,
    height=50,
    command=upload_image
)
upload_btn.pack(pady=30)

# Detect Button
detect_btn = ctk.CTkButton(
    left_frame,
    text="Detect Number Plate",
    width=220,
    height=50,
    command=detect_plate
)
detect_btn.pack(pady=20)

# Result Label
result_label = ctk.CTkLabel(
    left_frame,
    text="Detected Plate:\n--------",
    font=("Arial", 20)
)
result_label.pack(pady=30)

# History Title
history_title = ctk.CTkLabel(
    left_frame,
    text="Detection History",
    font=("Arial", 18, "bold")
)
history_title.pack(pady=10)

# History Label
history_label = ctk.CTkLabel(
    left_frame,
    text=get_history(),
    font=("Arial", 14),
    justify="left"
)
history_label.pack(pady=10)

# View Image Button
# Open Output Folder Button
view_btn = ctk.CTkButton(
    left_frame,
    text="📂 Open Output Folder",
    width=220,
    height=40,
    command=view_last_image
)

view_btn.pack(pady=10)

# Right Frame
right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Image Preview Area
image_label = ctk.CTkLabel(
    right_frame,
    text="Image Preview Area",
    font=("Arial", 24)
)
image_label.pack(expand=True)

# Run App
app.mainloop()