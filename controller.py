"""**Файл-контроллер**


Здесь описывается взаимодействие моделей, описываемых в model.py"""


#
from model import create_record, delete_record, record_to_file, load_from_json_file
#
from view import show_menu, show_records


def main():
    """**Основная функция**
    
    Рабочее тело проекта"""


    #Список записей (пока пустой)
    data = []

    #Бесконечный цикл:
    while True:
        #Выводим меню:
        show_menu()

        #Получаем ввод выбора с клавиатуры пользователя:
        choice = input("> ")

        #Если выбор - 1 - создаем новую запись и добавляем в список
        if choice == "1":
            create_record(data)

        #Если выбор - 2 - удаляем запись из списка
        elif choice == "2":
            delete_record(data)

        #Если выбор - 3 - красиво выводим все записи
        elif choice == "3":
            show_records(data)

        #Если выюор - 4 - записываем все данные из списка в файл data.json
        elif choice == "4":
            record_to_file("data.json", data)

        #Если выбор - 5 - загружаем в список данные из файла data.json
        elif choice == "5":
            data = load_from_json_file("data.json")
        
        #Если выбор 6 - выводим сообщения и прерываем список.
        elif choice == "6":
            print("Завершение программы...")
            print("Всего доброго!")
            break

        #Иначе: выводим сообщения
        else:
            print("Ошибка: неверная команда!")
            print("Попробуйте ввести одну из предложенных комманд.")


#Пытаемся запустить программу:
try:
    main()
#Если программа "грубо завершается" - выводим сообщения.
except KeyboardInterrupt:
    print("\nЗавершение программы...")