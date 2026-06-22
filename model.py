"""**Файл-модель**

Здесь хранятся все классы и функции, так или иначе описывающие логику работа
программы"""


#Импортируем необходимые для работы элементы из сторонних библиотек.
from random import choice
import json
import string
from datetime import datetime


def create_password(len_password:int):
    """**Генератор-пароля**
    
    Вносим len_password - длинну пароля."""

    #Строка, состоящая из заглавныъ/строчных латинских букв.
    #а также цифр
    base_str = string.ascii_letters + string.digits
    #Пустая строка-база для пароляю
    password_str = ""

    #Цикл, повторяющийся len_password количество раз.
    for _ in range(len_password):

        #Выбираем случайный элемент и добавляем его к строке-базе. 
        password_str += choice(base_str)
    
    #Возращаем сформированную строку.
    return password_str


def now_time():
    """**Функция-часы**
    
    Возращает текущее время"""

    #Возращаем текущую дату и время по модели:
    #день.месяц.год часы:минуты
    return (datetime.now()).strftime("%d.%m.%Y %H:%M")


class PasswordRecord:
    """**Класс-запись**
    
    Создан для удобства структурирования данных"""

    def __init__(self, service, username, len_password):
        """**Обьявляем переменные**
        
        service - название сервиса/ссылка на сервис (строка)
        username - имя аккаунта (строка)
        password - пароль, сгенерированный по длинне (строка)
        created_at - дата создания записи (строка)
        """
        self.__service = service 
        self.__username = username
        self.__password = create_password(len_password)
        self.__created_at = now_time()


    def get_rec(self):
        """**Функция -геттер**
        
        Позволяет вывести данные в удобном для обработки формате"""


        #Создаем словарь с полями, соответствующими переменным, 
        # и помещаем в них соответствующие переменные.
        data_dict = {
            "Service": self.__service,
            "Username": self.__username,
            "Password": self.__password,
            "CreatedAt": self.__created_at
            }

        #Возращаем словарь.
        return data_dict



def create_record(base_lst:list):
    """**Функция-создатель записец**
    
    Создает запись и добавляет её в список
    
    Вносим base_lst - список"""


    #Принимаем ввод названия.
    user = input("Введите имя аккаунта:")
    #Принимаем ввод сервиса.
    service = input("Введите название сервиса/ссылку на сервис: ")

    #Пытаемся:
    try:

        #Принять ввод длины пароля  и переформатировать его в число.
        len_pass = int(input("Введите длинну пароля:"))
    
    #Если было введенро не число - выводим сообщение и возращаем ничего.
    except ValueError:

        
        print("Ошибка: введено не число.")
        print("Попробуйте в следующий раз вводить только цифры.") 
        return None

    #Создаем обьем-запись.
    data_rec = PasswordRecord(service, user, len_pass)
    #Добавляем сформированный в обьекте словарь в списокю

    base_lst.append(data_rec.get_rec())
    #Выводим сообщение.
    print("Запись добавлена.")


def delete_record(base_lst: list):
    """**Функция-удалятор**
    
    Удаляет элемент из списка по имени
    
    Вносим base_lst - список"""
    
    #Если список не пуст:
    if base_lst:

        #Принимаем ввод имени:
        need_name = input("Введите юзернейм:")

        #Проходимся по списку:
        for rec in base_lst:
        
            #Если поле Username совпадает с введенным именем:
            if rec["Username"] == need_name:

                #Вопрос
                question = "Вы уверены, что хотите удалить запись(Д/Н): "
                #Принимаем ответ на вопрос:
                choice = input(question).lower()

                #Если ответ д или l:
                if choice == "д" or choice == "l":

                    #Убираем элемент из списка.
                    base_lst.remove(rec)

                    #Выводим сообщение и завершаем функцию.
                    print("Запись удалена!")
                    return None

                #Если ответ - любой другой символ - 
                # выводим сообщение и также хавершаем функцию.
                else:   
                    print("Отмена удаления...")
                    return None

        #Иначе - выводим сообщения.
        else:
            print(f"Запись с юзером {need_name} отсутствует в базе данных.")
            print("Попробуйте другой юзернейм.")

    #Иначе - выводим сообщение.
    else:
        print("Список записей пуст.")




def load_from_json_file(URL):
    """**Функция-загрузчик**
    
    Загружает данные из файла
    
    Вносим URL - юрл файла"""

    #Пытаемся:
    try:

        #Открыть файл и поместить его содержимое в переменную data
        with open(URL, "r", encoding="UTF-8") as file:
            data = json.load(file)

        #Вывести сообщение
        print("Данные получены.")
        #Возратить переменную data
        return data

    #Если файла с таким URL несуществует:
    except FileNotFoundError:

        #Выводим сообщение
        print("Ошибка: файл несуществует!")
        print(f"Создание файла...")

        #Создаем файл
        file = open(URL, "w", encoding="UTF-8")
        file.close()


def record_to_file(URL, base_lst):
    """**Функция-записыватель**
    
    Функция, записывающая из списка информацию в файл
    
    Вносим:
    URL - юрл файла
    base_lst - список"""
    
    #Открываем файл
    with open(URL, "w", encoding="UTF-8") as file:

        #Записываем данные из списка в файл.
        #Делаем чтение русских букв возможным.
        #Задаем 4 отствупа в структуре файла. 
        json.dump(base_lst, file, ensure_ascii=False, indent=4)
        print("Файл обновлен.")


