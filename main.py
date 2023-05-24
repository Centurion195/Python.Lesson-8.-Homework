def interface():
    print("ГЛАВНОЕ МЕНЮ")
    while True:
        print("Выберите действие:")
        print("1. Показать все контакты")
        print("2. Поиск")
        print("3. Создать контакт")
        print("4. Выход")
        action = int(input("\nВведите номер: "))
        if action == 1:
            print()
            interface_view_all_contacts()
        elif action == 2:
            print()
            find_contacts()
        elif action == 3:
            print()
            interface_create_contact()
        elif action == 4:
            break
        else:
            print("Неверный пункт меню. Повторите попытку.\n")


def interface_view_all_contacts():
    print("СПИСОК КОНТАКТОВ")
    print("------------------------------------------")
    print("ID / Фамилия / Имя / Отчество / № телефона")
    print("------------------------------------------")
    with open(db, 'r', encoding='utf-8') as file:
        for el in file:
            print(el[:-1])
    print()


def find_contacts():
    print("ПОИСК")
    found_contacts = list()
    find = input("Введите Фамилию, Имя или № телефона: ")
    with open(db, 'r', encoding='utf-8') as file:
        for el in file:
            contact = el.split()
            if contact[1] == find or contact[2] == find or contact[4] == find:
                found_contacts.append(contact)
    print("\nНайденные контакты:")
    for i in found_contacts:
        print(*i)
    print()


def interface_create_contact():
    print("СОЗДАНИЕ НОВОГО КОНТАКТА")
    index = max_index()
    registration = list()
    registration.append(int(index)+1)
    registration.append(input("Фамилия: "))
    registration.append(input("Имя: "))
    registration.append(input("Отчество: "))
    registration.append(input("Номер телефона (формат: +7ХХХХХХХХХХ): "))
    print("\n" + str(registration))
    while True:
        print("\nВыберите действие:")
        print("1. Сохранить")
        print("2. Отменить")
        action = int(input("Введите номер: "))
        if action == 1:
            with open(db, 'a', encoding='utf-8') as file:
                if registration[0] != 1:
                    file.write('\n')
                for el in registration:
                    file.write(str(el) + ' ')
            with open('config.txt', 'w', encoding='utf-8') as f1:
                f1.write(str(registration[0]))
            print("\nКонтакт успешно создан!\n")
            break
        elif action == 2:
            print()
            break
        else:
            print("Неверный пункт меню. Повторите попытку.")


def max_index():
    with open('config.txt', 'r', encoding='utf-8') as file:
        return file.readline()


print("Телефонный справочник\n")
db = "contacts_db.txt"
interface()
