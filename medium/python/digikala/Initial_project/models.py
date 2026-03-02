from datetime import datetime


class Comment:
    def __init__(self, text, user):
        self.text = text
        self.user = user
        self.date_added = datetime.now()


class Product:
    DEFAULT_SELLER = 'Digikala'
    last_unused_id = 1

    def __init__(self, name, price, category, seller=DEFAULT_SELLER):
        self.id = Product.last_unused_id
        self.name = name
        self.price = price
        self.seller = seller
        self.category = category
        self.related_products = list()
        self.comments = list()

        Product.last_unused_id += 1

    def add_review(self, comment: Comment):
        self.comments.append(comment)

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.id == other.id

    def __hash__(self):
        return super().__hash__()


class User:
    def __init__(self, username):
        self.username = username
        self.bought_products = list()

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username
        return False
