from menu import main_menu
from users.admin import Admin

def run():
    admin = Admin()
    admin.create_first_admin()

    main_menu()

if __name__ == "__main__":
    run()
