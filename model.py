import random
import json
from datetime import datetime




class PassBase:
    def __init__(self, len_passord: int):
        self.__base_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.__len_password = len_passord
        self.__password = ""

    def create_password(self):
        password_str = ""
        for _ in range(self.__len_password):
            print(self.__base_str)
            password_str += random.choice(self.base_str)
        
        self.__password = password_str


class PasswordRecord:
    
    def __init__(self, len_passord, Service, Username):
        self.__created_at = (datetime.now()).strftime("%d.%m.%Y %H:%M")
        self.__Service = Service 
        self.__Username = Username
        self.__password = PassBase(len_passord).create_password()

    def get_rec(self):
        return {"Service": self.__Service, 
                "Username": self.__Username, 
                "CreatedAt": self.__created_at, 
                "Password":  self.__password}


def get_new_record(base_lst:list):
    name = input()
    service = input()
    len_password = int(input())
    
    obj = PasswordRecord(len_password, service, name)
    base_lst.append(obj.get_rec())


def show_lst(base_lst):
    for i in base_lst:
        print(f"Сервис: {i["Service"]}")
        print(f"Юзернейм: {i["Username"]}")
        print(f"Дата создания: {i["CreatedAt"]}")
        print(f"Пароль: {i["Password"]}")



def load_from_json_file(URL):
    try:
        with open(URL, "r", encoding="UTF-8") as file:
            data = json.load(file)

        return data
    
    except FileNotFoundError:

        print("Ошибка: файл несуществует!")
        print(f"Создание файла {URL}")

        file = open(URL, "w", encoding="UTF-8")
        file.close()


def record_to_file(URL, base_lst):
    with open(URL, "w", encoding="UTF-8") as file:
        json.dump(base_lst, file, ensure_ascii=False, indent=4)