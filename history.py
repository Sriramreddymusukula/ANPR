import pandas as pd
import os


def get_history():

    if os.path.exists("vehicle_database.csv"):

        df = pd.read_csv("vehicle_database.csv")

        history = ""

        df = df.iloc[::-1]

        for index, row in df.iterrows():

            history += (
                f"{row['Plate Number']}\n"
                f"{row['Date']}  {row['Time']}\n\n"
            )

        return history

    return "No History Available"


def get_history_data():

    if os.path.exists("vehicle_database.csv"):
        return pd.read_csv("vehicle_database.csv")

    return pd.DataFrame()


def get_image_path(plate_number):

    if os.path.exists("vehicle_database.csv"):

        df = pd.read_csv("vehicle_database.csv")

        rows = df[df["Plate Number"] == plate_number]

        if len(rows) > 0:

            return rows.iloc[-1]["Image Path"]

    return None