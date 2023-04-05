# Дополнить телефонный справочник возможностью изменения и удаления данных.\
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных
# Функция для импорта данных из файла
def import_data():
    try:
        with open('contacts.txt', 'r') as file:
            data = file.read().split('\n')[:-1]  # Удаляем последний элемент - пустую строку
            contacts = []
            for contact in data:
                contact_info = contact.split(',')
                contacts.append(contact_info)
            return contacts
    except FileNotFoundError:
        print('Файл не найден')


# Функция для экспорта данных в файл
def export_data(contacts):
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            contact_info = ','.join(contact) + '\n'
            file.write(contact_info)


# Функция для добавления новой записи в список контактов
def add_contact(contacts):
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    new_contact = [name, surname, patronymic, phone_number]
    contacts.append(new_contact)
    return contacts


# Функция для поиска записей по заданной характеристике
def search_contacts(contacts):
    search_char = input('Введите характеристику для поиска (имя, фамилия, отчество или номер телефона): ')
    matches = []
    for contact in contacts:
        if search_char.lower() in [char.lower() for char in contact]:
            matches.append(contact)
    if len(matches) == 0:
        print('Контакты не найдены')
    else:
        print('Результаты поиска:')
        for match in matches:
            print(f'{match[0]} {match[1]} {match[2]}, телефон: {match[3]}')


# Функция для удаления записи из списка контактов
def delete_contact(contacts):
    search_char = input('Введите характеристику для поиска (имя, фамилия, отчество или номер телефона) для удаления: ')
    match = None
    for contact in contacts:
        if search_char.lower() in [char.lower() for char in contact]:
            match = contact
    if match:
        contacts.remove(match)
        print(f'{match[0]} {match[1]} {match[2]} был удален')
    else:
        print('Контакты не найдены')
    return contacts


# Функция для изменения записи в списке контактов
def edit_contact(contacts):
    search_char = input('Введите характеристику для поиска (имя, фамилия, отчество или номер телефона) для изменения: ')
    match = None
    for contact in contacts:
        if search_char.lower() in [char.lower() for char in contact]:
            match = contact
    if match:
        print(f'Контакт: {match[0]} {match[1]} {match[2]}, телефон: {match[3]}')
        new_name = input('Введите новое имя (оставьте пустым, если оставить без изменений): ')
        new_surname = input('Введите новую фамилию (оставьте пустым, если оставить без изменений): ')
        new_patronymic = input('Введите новое отчество (оставьте пустым, если оставить без изменений): ')
        new_phone = input('Введите новый номер телефона (оставьте пустым, если оставить без изменений): ')
        if new_name != '':
            match[0] = new_name
        if new_surname != '':
            match[1] = new_surname
        if new_patronymic != '':
            match[2] = new_patronymic
        if new_phone != '':
            match[3] = new_phone
        print(f'Контакт успешно изменен: {match[0]} {match[1]} {match[2]}, телефон: {match[3]}')
    else:
        print('Контакты не найдены')
    return contacts


# Основная функция
def main():
    contacts = []
    while True:
        print('Выберите действие:')
        print('1. Просмотреть все контакты')
        print('2. Добавить контакт')
        print('3. Найти контакт')
        print('4. Удалить контакт')
        print('5. Изменить контакт')
        print('6. Экспортировать данные в файл')
        print('7. Импортировать данные из файла')
        print('8. Выйти из программы')
        choice = input('Выбор: ')

        if choice == '1':
            if len(contacts) == 0:
                print('Список контактов пуст')
            else:
                print('Все контакты:')
                for contact in contacts:
                    print(f'{contact[0]} {contact[1]} {contact[2]}, телефон: {contact[3]}')

                    elif choice == '2':
                    contacts = add_contact(contacts)

                elif choice == '3':
                search_contacts(contacts)

            elif choice == '4':
            contacts = delete_contact(contacts)

        elif choice == '5':
            contacts = edit_contact(contacts)

        elif choice == '6':
            export_data(contacts)
            print('Данные экспортированы в файл')
 #второй вариант
# r - только чтение файла
# a - дозапись в файл
# w - перезапись файла
def show_data():
    """эта ф-ция показывает содержимое справочника"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()  # .split('\n')
    return book


def new_data():
    """добавляет строку в справочник"""
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: ' + '\n'))


def find_data():
    """Эта ф-ция ищет информацию в справочнике"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('что ищем?: ')
        for i in book:
            if temp in i:
                print(i)


def delete_person(name):
    """Удаляет данные"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8") as file:
        for person in persons:
            if name != person:
                file.write(person)


def change_person(new_name, old_name):
    """Изменяет данные"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8") as file:
        for person in persons:
            if old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")


while True:
    mode = input('Выберите режим работы справочника' + '\n'
                 + '0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('кого удалять?: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('кого переименовать?: ')
        new_name = input('как  назвать?: ')
        change_person(new_name, old_name)
    elif mode == '5':
        break
    else:
        print('No mode')

        elif choice == '7':
            contacts = import_data()
