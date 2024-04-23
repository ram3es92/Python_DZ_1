def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчетство: ")
    phone = input("Введите номер телефона: ")
    contact = {'second_name': s_name,
            'first_name': f_name,
            'middle_name': m_name,
            'phone_number': phone}
    return contact

def add_new_contact():
    contact = ask_data()
    with open("phonebook.txt", 'a', encoding= 'utf-8') as file:
        file.write('; '.join(contact.values()))
        file.write('\n')
    print("Контакт успешно добавлен.")

def open_phonebook():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding= 'utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.split(";")))

def find_contact():
    search_option = input(f"Поиск по:\n1. Имени\n2. Фамилии\n3. Отчеству\n4. Номеру телефона\nВыберите опцию: ")
    search_term = input("Введите значение для поиска: ")
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open('phonebook.txt', 'r', encoding= 'utf-8') as file:
        print("\t\t".join(title))
        found = False
        for line in file:
            contact = line.strip().split('; ')
            if search_option == '1' and search_term.lower() == contact[1].lower():
                found = True
                print("\t\t".join(contact))
            elif search_option == '2' and search_term.lower() == contact[0].lower():
                found = True
                print("\t\t".join(contact))
            elif search_option == '3' and search_term.lower() == contact[2].lower():
                found = True
                print("\t\t".join(contact))
            elif search_option == '4' and search_term.lower() == contact[3].lower():
                found = True
                print("\t\t".join(contact))
        if not found:
            print("Контакт не найден.")

def delete_contact():
    search_term = input("Введите фамилию контакта, который хотите удалить: ")
    with open('phonebook.txt', 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
    with open('phonebook.txt', 'w', encoding= 'utf-8') as file:
        deleted = False
        for line in lines:
            contact = line.strip().split('; ')
            if search_term.lower() != contact[0].lower():
                file.write('; '.join(contact) + '\n')
            else:
                deleted = True
        if deleted:
            print(f"Контакт с фамилией '{search_term}' успешно удален.")
        else:
            print(f"Контакт с фамилией '{search_term}' не найден.")

def copy_contact():
    try:
        source_filename = "phonebook.txt"
        destination_filename = "main_phonebook.txt"
        line_number = int(input("Введите номер строки для копирования: "))

        with open(source_filename, 'r', encoding='utf-8') as source_file:
            lines = source_file.readlines()
        
        if 0 < line_number <= len(lines):
            contact_data = lines[line_number - 1]
            
            with open(destination_filename, 'a', encoding='utf-8') as destination_file:
                destination_file.write(contact_data)
            
            print("Контакт успешно скопирован.")
        else:
            print("Номер строки вне диапазона.")
    except FileNotFoundError:
        print("Файл не найден.")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Поиск контакта")
        print("2. Добавление нового контакта")
        print("3. Удаление контакта")
        print("4. Открыть телефонную книгу")
        print("5. Копирование контакта из одного файла в другой")
        print("6. Выход")
        
        choice = input("Введите номер действия: ")

        if choice == "1":
            find_contact()
        elif choice == "2":
            add_new_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            open_phonebook()
        elif choice == "5":
            copy_contact()
        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

main()