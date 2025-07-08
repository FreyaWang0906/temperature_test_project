import csv
import random
from datetime import datetime, timedelta
import os

output_path = os.path.join("data", "temperature_log.csv")

def generate_temperature_data(num_records=50):
    start_time = datetime.now()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if os.path.exists(output_path):
        os.remove(output_path)

    print("Writing to absolute path:", os.path.abspath(output_path))

    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature"])

        for i in range(num_records):
            timestamp = start_time + timedelta(seconds = 30 * i)

            if random.random() < 0.9:
                temp = round(random.uniform(22.0, 28.0), 2)
            else:
                temp = round(random.uniform(15.0, 30.0), 2)

            writer.writerow([timestamp.strftime("%Y-%m-%d %H:%M:%S"), temp])

    print(f"Successfully generated simulated temperature data, {num_records} in total, saved in {output_path}")


if __name__ == "__main__":
    generate_temperature_data()