from functions import try_to_log_in, show_main_menu, exit_program, manage_factories, manage_employees, manage_clients

PASSWORD = "geoinformatyka"

is_logged_in = False


while not is_logged_in:
    is_logged_in = try_to_log_in(PASSWORD)


if is_logged_in:
    while True:
        show_main_menu()
        choice = input("Wybierz pozycje z listy: ")
        match choice:
            case "0":
                exit_program()
            case "1":
                manage_factories()
            case "2":
                manage_employees()
            case "3":
                manage_clients()


