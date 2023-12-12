from Controller.Controller import Controller

class UI:
    def __init__(self, controller):
        self.controller=controller

    def menu(self):
        print("Add new article:")
        id= int(input("ID: "))
        price= int(input("Price: "))
        size= int(input("Size: "))
        article_type= int(input("Article type: "))

        self.controller.add_to_repo(id, price,size, article_type)