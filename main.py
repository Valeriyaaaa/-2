from file_operations import read_csv, write_csv

def main():
    # Пример использования функций из file_operations.py
    input_file_path = 'input_data.csv'
    output_file_path = 'output_data.csv'

    # Чтение данных из CSV-файла
    data = read_csv(input_file_path)
    if data is not None:
        print("Содержимое CSV-файла:")
        for row in data:
            print(row)

        # Производим какие-то манипуляции с данными (в данном случае - просто вывод)
        processed_data = data

        # Запись обработанных данных в новый CSV-файл
        write_csv(output_file_path, processed_data)

if name == "__main__":
    main()
