import csv
import datetime

def log_data(temp, humidity, pressure):
    with open("climate_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.datetime.now().isoformat(),
            temp,
            humidity,
            pressure
        ])

if __name__ == "__main__":
    log_data(21.4, 55.2, 1008.3)
    print("Sample climate record written.")
