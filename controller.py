
from model import create_record, delete_record, show_records, record_to_file, load_from_json_file
from view import show_menu

def main():
    data = []
    while True:
        show_menu()

        choice = input("> ")


        if choice == "1":
            create_record(data)


        elif choice == "2":
            delete_record(data)


        elif choice == "3":
            show_records(data)


        elif choice == "4":
            record_to_file("data.json", data)


        elif choice == "5":
            data = load_from_json_file("data.json")
        

        elif choice == "6":
            print("Завершение программы...")
            print("Всего доброго!")
            break


        else:
            print("Ошибка: невершная команда!")
            print("Попробуйте ввести одну из предложенных комманд.")

try:
    main()
except KeyboardInterrupt:
    print("\nЗавершение программы...")