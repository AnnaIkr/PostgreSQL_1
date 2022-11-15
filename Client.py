import psycopg2
from pprint import pprint

def create_tables(cur):

    #Создание таблицы данных клиента
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id SERIAL PRIMARY KEY, 
        name VARCHAR(20) NOT NULL, 
        surname VARCHAR(50) NOT NULL, 
        email VARCHAR(50) NOT NULL);
    """)
    #Создание отдельной таблицы с номерами телефона клиента
    cur.execute("""
    CREATE TABLE IF NOT EXISTS telephones(
        id_telephone SERIAL PRIMARY KEY,
        client_id INTEGER NOT NULL REFERENCES clients(id),
        telephone VARCHAR(11) UNIQUE);
    """)

def add_new_client(cur, name, surname, email):
    #Добавление нового клиента в таблицу clients
    cur.execute("""
    INSERT INTO clients(name, surname, email) VALUES(%s, %s, %s);
    """, (name, surname, email))

def add_new_telephones(cur, client_id, telephone):
    #Добавление нового номера телефона в таблицу telephones
    cur.execute("""
    INSERT INTO telephones(client_id, telephone) VALUES(%s, %s);
    """, (client_id, telephone))

def change_client_data():
    #Изменение данных о клиенте
    print("Для изменения данных о клиенте введите нужную команду.\n "
        "1 - изменить имя; 2 - изменить фамилию; 3 - изменить e-mail; 4 - изменить номер телефона")

    while True:
        command_symbol = int(input())
        if command_symbol == 1:
            input_id_for_changing_name = input("Введите id клиента имя которого хотите изменить: ")
            input_name_for_changing = input("Введите новое имя: ")
            cur.execute("""
            UPDATE clients SET name=%s WHERE id=%s;
            """, (input_name_for_changing, input_id_for_changing_name))
            break
        elif command_symbol == 2:
            input_id_for_changing_surname = input("Введите id клиента фамилию которого хотите изменить: ")
            input_surname_for_changing = input("Введите новую фамилию: ")
            cur.execute("""
            UPDATE clients_ SET surname=%s WHERE id=%s;
            """, (input_surname_for_changing, input_id_for_changing_surname))
            break
        elif command_symbol == 3:
            input_id_for_changing_email = input("Введите id клиента e-mail которого хотите изменить: ")
            input_email_for_changing = input("Введите новый e-mail: ")
            cur.execute("""
            UPDATE clients SET email=%s WHERE id=%s;
            """, (input_email_for_changing, input_id_for_changing_email))
            break
        elif command_symbol == 4:
            input_telephone_you_wanna_change = input("Введите номер телефона который Вы хотите изменить: ")
            input_telephone_for_changing = input("Введите новый номер телефона: ")
            cur.execute("""
            UPDATE telephones SET telephone=%s WHERE telephone=%s;
            """, (input_telephone_for_changing, input_telephone_you_wanna_change))
            break
        else:
            print("Вы ввели неправильную команду, повторите ввод")

def delete_telephones():
    #Удаление номера телефона клиента из таблицы telephones
    input_id_for_deleting_telephones = input("Введите id клиента номер телефона которого хотите удалить: ")
    input_telephones_for_deleting = input("Введите номер телефона который хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM telephones WHERE client_id=%s AND telephones=%s
        """, (input_id_for_deleting_telephones, input_telephones_for_deleting))

def delete_client():
    #Удаление имеющейся информации о клиенте
    input_id_for_deleting_client = input("Введите id клиента которого хотите удалить: ")
    input_client_surname_for_deleting = input("Введите фамилию клиента которого хотите удалить: ")
    with conn.cursor() as cur:
        #удаление связи с таблицей telephones
        cur.execute("""
        DELETE FROM telephones WHERE client_id=%s
        """, (input_id_for_deleting_client,))
        #удаление информации о клиенте из таблицы clients
        cur.execute("""
        DELETE FROM clients WHERE id=%s AND surname=%s
        """, (input_id_for_deleting_client, input_client_surname_for_deleting))

def find_client():
    #Поиск клиента по данным
    print("Для поиска информации о клиенте введите команду, где:\n "
          "1 - найти по имени; 2 - найти по фамилии; 3 - найти по e-mail; 4 - найти по номеру телефона")
    while True:
        input_command_for_finding = int(input("Введите команду для поиска информации о клиенте: "))
        if input_command_for_finding == 1:
            input_name_for_finding = input("Введите имя для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, surname, email, telephone
            FROM clients AS ch5
            LEFT JOIN telephones AS cp ON cp.id_telephone = ch5.id
            WHERE name=%s
            """, (input_name_for_finding,))
            print(cur.fetchall())
        elif input_command_for_finding == 2:
            input_surname_for_finding = input("Введите фамилию для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, surname, email, telephone
            FROM clients AS ch5
            LEFT JOIN telephones AS cp ON cp.id_telephone = ch5.id
            WHERE surname=%s
            """, (input_surname_for_finding,))
            print(cur.fetchall())
        elif input_command_for_finding == 3:
            input_email_for_finding = input("Введите email для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, surname, email, telephone
            FROM clients AS ch5
            LEFT JOIN telephones AS cp ON cp.id_telephone = ch5.id
            WHERE email=%s
            """, (input_email_for_finding,))
            print(cur.fetchall())
        elif input_command_for_finding == 4:
            input_telephone_for_finding = input("Введите номер телефона для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, surname, email, telephone
            FROM clients AS ch5
            LEFT JOIN telephones AS cp ON cp.id_telephone = ch5.id
            WHERE telephone=%s
            """, (input_telephone_for_finding,))
            print(cur.fetchall())
        else:
            print("Вы ввели неправильную команду, повторите ввод")

def check_function(cur):
    #Проверочная функция, отображает содержимое таблиц
    cur.execute("""
    SELECT * FROM clients;
    """)
    pprint(cur.fetchall())
    cur.execute("""
    SELECT * FROM telephones;
    """)
    pprint(cur.fetchall())


with psycopg2.connect(host="", user="", password="", database="", port="") as conn:
    with conn.cursor() as cur:
        create_tables(cur)
        check_function(cur)
        add_new_client(cur, "Иван", "Иванов", "iv@g.com")
        add_new_client(cur, "Петр", "Петров", "pr@g.com")
        add_new_client(cur, "Николай", "Николаев", "nn@g.com")
        add_new_client(cur, "Сидор", "Сидоров", "cd@g.com")
        add_new_client(cur, "Максим", "Максимов", "max@g.com")
        add_new_telephones(cur, 1, "11111111111")
        add_new_telephones(cur, 2, "22222222222")
        add_new_telephones(cur, 3, "33333333333")
        add_new_telephones(cur, 4, "44444444444")
        add_new_telephones(cur, 5, "55555555555")
        change_client_data()
        delete_telephones()
        delete_client()
        find_client()

conn.close()