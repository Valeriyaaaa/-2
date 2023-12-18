import csv

def read_csv(file_path):
    """
    Чтение данных из CSV-файла.
    """
    data = []
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return None

def write_csv(file_path, data):
    """
    Запись данных в CSV-файл.
    """
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
        print(f"Данные успешно записаны в CSV-файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при записи в CSV-файл: {e}")
