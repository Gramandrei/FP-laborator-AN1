from UI.ui import UI
from Controller.Controller import Controller
from Repository.ClothingRepo import ClothingRepo

def main():
    my_repository = ClothingRepo()
    my_controller = Controller()
    my_ui = UI(my_controller)
    my_ui.menu()


main()