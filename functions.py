import sys
import tkinter as tk
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim

FACTORIES = []


def try_to_log_in(password):
    user_password = input("Podaj haslo: ")
    if user_password == password:
        return True
    return False


def show_map(entities):
    if len(entities) == 0:
        print("Brak rekordow")
        return

    root = tk.Tk()
    root.title("Mapa")
    map_widget = TkinterMapView(root, width=800, height=600)
    map_widget.pack(fill="both", expand=True)
    for entity in entities:
        map_widget.set_marker(entity["latitude"], entity["longitude"], text=entity["name"])
    root.mainloop()


def show_map_of_entitty(entity):
    root = tk.Tk()
    root.title("Mapa")
    map_widget = TkinterMapView(root, width=800, height=600)
    map_widget.pack(fill="both", expand=True)
    map_widget.set_marker(entity["latitude"], entity["longitude"], text=entity["name"])
    root.mainloop()


def get_coordinates_of_city(city, entity):
    geolocator = Nominatim(user_agent="city_coordinates")
    location = geolocator.geocode(city)

    if location:
        entity["longitude"] = location.longitude
        entity["latitude"] = location.latitude
    else:
        print("Nie znaleziono takiego miasta. Koordynaty nie zostaly dodane")
        return None


def show_main_menu():
    print("0 - Koniec programu")
    print("1 - Zarzadzaj Fabrykami")
    print("2 - Zarzadzaj Pracownikami Fabryk")
    print("3 - Zarzadzaj Klientami Fabryk")


def show_factory_menu():
    print("1 - Wyświetl listę fabryk")
    print("2 - Dodaj nową fabryke")
    print("3 - Usun fabryke")
    print("4 - Zmien nazwe fabryki")
    print("5 - Pokaz mape fabryk")
    print("6 - Pokaz fabryke na mapie")


def show_list_of_the_factories():
    print("Lista fabryk: ")
    for factory in FACTORIES:
        print(f"{factory['name']}")


def add_new_factory():
    name = input("Podaj nazwe fabryki: ")
    city = input("Podaj nazwe miasta: ")
    factory = {"name": name, "city": city, "employees": [], "clients": []}
    get_coordinates_of_city(city, factory)
    FACTORIES.append(factory)


def remove_factory():
    name = input("Podaj nazwe fabryki do usuniecia: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            FACTORIES.remove(factory)
            return
    print("Nie znaleziono fabryki z taka nazwa")


def change_factory_name():
    name = input("Podaj nazwe fabryki, ktorej nazwe chcesz zmienic: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            new_name = input("Podaj nowa nazwe fabryki: ")
            factory["name"] = new_name
            return
    print("Nie znaleziono fabryki z taka n2azwa")


def show_map_of_factory():
    name = input("Podaj nazwe fabryki, ktora chcesz zobaczyc na mapie: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            show_map_of_entitty(factory)
            return
    print("Nie znaleziono fabryki z taka nazwa")


def manage_factories():
    show_factory_menu()
    choice = input("Wybierz pozycje z listy: ")
    match choice:
        case "1":
            show_list_of_the_factories()
        case "2":
            add_new_factory()
        case "3":
            remove_factory()
        case "4":
            change_factory_name()
        case "5":
            show_map(FACTORIES)
        case "6":
            show_map_of_factory()


def show_employees_menu():
    print("1 - Wyświetl listę pracownikow")
    print("2 - Dodaj nowego pracownika")
    print("3 - Usun pracownika")
    print("4 - Zmien nazwe pracownika")
    print("5 - Pokaz mape pracownikow")
    print("6 - Pokaz pracownika na mapie")


def show_list_of_the_employees():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            for employee in factory["employees"]:
                print(f"{employee['name']}")
            return
    print("Nie znaleziono fabryki z taka nazwa")


def add_new_employee():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_employee = input("Podaj nazwe pracownika: ")
            city = input("Podaj nazwe miasta: ")
            employee = {"name": name_of_employee, "city": city}
            get_coordinates_of_city(city, employee)
            factory["employees"].append(employee)
            return
    print("Nie znaleziono fabryki z taka nazwa")


def remove_employee():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_employee = input("Podaj nazwe pracownika: ")
            employee = {"name": name_of_employee}
            factory["employees"].remove(employee)
            return
    print("Nie znaleziono fabryki z taka nazwa")


def change_employee_name():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_employee = input("Podaj nazwe pracownika: ")
            for employee in factory["employees"]:
                if employee["name"] == name_of_employee:
                    new_name_of_employee = input("Podaj nowa nazwe pracownika: ")
                    employee["name"] = new_name_of_employee
                    return
            print("Nie znaleziono pracownika")
            return
    print("Nie znaleziono fabryki z taka nazwa")


def show_map_of_employees():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            show_map(factory["employees"])
            return
    print("Nie znaleziono fabryki z taka nazwa")


def show_employee_on_map():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_employee = input("Podaj nazwe pracownika: ")
            for employee in factory["employees"]:
                if employee["name"] == name_of_employee:
                    show_map_of_entitty(employee)
                    return
            print("Nie znaleziono pracownika")
            return
    print("Nie znaleziono fabryki z taka nazwa")


def manage_employees():
    show_employees_menu()
    choice = input("Wybierz pozycje z listy: ")
    match choice:
        case "1":
            show_list_of_the_employees()
        case "2":
            add_new_employee()
        case "3":
            remove_employee()
        case "4":
            change_employee_name()
        case "5":
            show_map_of_employees()
        case "6":
            show_employee_on_map()


def show_clients_menu():
    print("1 - Wyświetl listę klientow")
    print("2 - Dodaj nowego klienta")
    print("3 - Usun klienta")
    print("4 - Zmien nazwe klienta")
    print("5 - Dodaj zakup dla klienta")
    print("6 - Pokaz zakupy klienta")
    print("7 - Pokaz mape klientow")
    print("8 - Pokaz klienta na mapie")


def show_list_of_the_clients():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            for client in factory["clients"]:
                print(f"{client['name']}")
            return
    print("Nie znaleziono fabryki z taka nazwa")


def add_new_client():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_client = input("Podaj nazwe klienta: ")
            city = input("Podaj nazwe miasta: ")
            client = {"name": name_of_client,"city": city, "purchases": []}
            get_coordinates_of_city(city, client)
            factory["clients"].append(client)
            return
    print("Nie znaleziono fabryki z taka nazwa")


def remove_client():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_client = input("Podaj nazwe klienta: ")
            client = {"name": name_of_client}
            factory["clients"].remove(client)
            return
    print("Nie znaleziono fabryki z taka nazwa")


def change_client_name():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_client = input("Podaj nazwe klienta: ")
            for client in factory["clients"]:
                if client["name"] == name_of_client:
                    new_name_of_client = input("Podaj nowa nazwe klienta: ")
                    client["name"] = new_name_of_client
                    return
            print("Nie znaleziono klienta")
            return
    print("Nie znaleziono fabryki z taka nazwa")


def show_client_on_map():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_client = input("Podaj nazwe klienta: ")
            for client in factory["clients"]:
                if client["name"] == name_of_client:
                    show_map_of_entitty(client)
                    return
            print("Nie znaleziono klienta")
            return
    print("Nie znaleziono fabryki z taka nazwa")


def add_purchase_to_client():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_client = input("Podaj nazwe klienta: ")
            for client in factory["clients"]:
                if client["name"] == name_of_client:
                    purchase = input("Podaj zakup: ")
                    client["purchases"].append(purchase)
                    return
            print("Nie znaleziono klienta")
            return
    print("Nie znaleziono fabryki z taka nazwa")


def show_client_purchases():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            name_of_client = input("Podaj nazwe klienta: ")
            for client in factory["clients"]:
                if client["name"] == name_of_client:
                    for purchase in client["purchases"]:
                        print(f"{purchase}")
                    return
            print("Nie znaleziono klienta")
            return
    print("Nie znaleziono fabryki z taka nazwa")


def show_map_of_clients():
    name = input("Podaj nazwe fabryki: ")
    for factory in FACTORIES:
        if factory["name"] == name:
            show_map(factory["clients"])
            return
    print("Nie znaleziono fabryki z taka nazwa")


def manage_clients():
    show_clients_menu()
    choice = input("Wybierz pozycje z listy: ")
    match choice:
        case "1":
            show_list_of_the_clients()
        case "2":
            add_new_client()
        case "3":
            remove_client()
        case "4":
            change_client_name()
        case "5":
            add_purchase_to_client()
        case "6":
            show_client_purchases()
        case "7":
            show_map_of_clients()
        case "8":
            show_client_on_map()


def exit_program():
    sys.exit()