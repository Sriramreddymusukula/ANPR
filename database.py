import pandas as pd
from datetime import datetime
import os
import shutil


def save_to_database(plate_number, image_path):

    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    # Create output folder if not exists
    if not os.path.exists("output"):
        os.makedirs("output")

    # Save a copy of vehicle image
    saved_image_path = f"output/detected_vehicle_{timestamp}.jpg"

    shutil.copy(image_path, saved_image_path)

    new_record = pd.DataFrame({
        "Date": [date],
        "Time": [time],
        "Plate Number": [plate_number],
        "Image Path": [saved_image_path]
    })

    if os.path.exists("vehicle_database.csv"):

        old_records = pd.read_csv("vehicle_database.csv")

        updated_records = pd.concat(
            [old_records, new_record],
            ignore_index=True
        )

    else:

        updated_records = new_record

    updated_records.to_csv(
        "vehicle_database.csv",
        index=False
    )

    print("Saved to Database Successfully")