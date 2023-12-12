from Repository.ClothingRepo import ClothingRepo
from Modelle.ClothingArticle import ClothingArticle

class Controller:
    def __init__(self, my_repo):
        self.repo = my_repo

    def add_to_repo(self, id, price,size,article_type):
        new_article=ClothingArticle(id, price, size, article_type)
        self.repo.add(new_article)