#_________________Robust File Processor_________________

# Write a function process_csv(filepath) that reads a CSV, calculates column averages, and handles: FileNotFoundError, PermissionError, csv. Error for malformed data. Use finally to always close the file



import csv

def process_csv(filepath):
    file = None

    try:
        file = open(filepath, "r")
        reader = csv.reader(file)

        data = list(reader)

        num_cols = len(data[0])
        sums = [0] * num_cols

        for row in data:
            for i in range(num_cols):
                sums[i] += float(row[i])

        averages = [total / len(data) for total in sums]

        print("Column Averages:")
        for i, avg in enumerate(averages, start=1):
            print(f"Column {i}: {avg}")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except csv.Error:
        print("Error: Malformed CSV file.")

    finally:
        if file:
            file.close()
            print("File closed.")


# Example
process_csv("data.csv")