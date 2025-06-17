import csv
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "value"])
    for i in range(5):
        writer.writerow([i, i*10])
print("CSV file created.")
