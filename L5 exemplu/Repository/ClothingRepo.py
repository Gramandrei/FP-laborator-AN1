class ClothingRepo:
    def __init__(self):
        self.clothes=[]
        # self.datei= ""
        # self.load(self.datei)

    def add(self, article):
        self.clothes.append(article)
        print("SUccesfully added")

    def delete(self, id):
        for article in self.clothes:
            if article.id==id:
                self.clothes.remove(article)

   # repo.update(id=12,new_price=36)

    def update(self, id, new_price=None, new_size=None, new_article_type=None):
        for aticle in self.clothes:
            if article.id==id:
                if new_price !=None:
                    article.price=new_price
                if new_size is not None:
                    article.size+new_size
                if new_article_type is not None:
                    article.article_type = new_article_type
