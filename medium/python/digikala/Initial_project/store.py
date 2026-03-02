# link https://quera.org/problemset/21206

from models import Product, User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        product_count = self.products[product]
        if amount > product_count:
            raise ValueError("Not Enough Products")
        elif amount == product_count:
            self.products.pop(product)
        else:
            self.products[product] -= amount

    def add_user(self, username):
        if username in [user.username for user in self.users]:
            return None
        user = User(username=username)
        self.users.append(user)
        return user.username

    def get_total_asset(self):
        asset = 0
        for product, count in self.products.items():
            asset += product.price * count
        return asset

    def get_total_profit(self):
        profit = 0
        for user in self.users:
            profit += sum([product.price for product in user.bought_products])
        return profit

    def get_comments_by_user(self, user):
        comment_texts = []
        for product in self.products.keys():
            for comment in product.comments:
                if comment.user == user:
                    comment_texts.append(comment.text)
        return comment_texts

    def get_inflation_affected_product_names(self):
        name_price = [(product.name, product.price) for product in self.products.keys()]
        name_price.sort()

        inflated = []
        for i, product_details in enumerate(name_price):
            try:
                next_product_details = name_price[i + 1]
            except IndexError:
                break

            if (
                product_details[0] == next_product_details[0]
                and product_details[1] != next_product_details[1]
            ):
                inflated.append(product_details[0])
        return list(set(inflated))

    def clean_old_comments(self, date):
        for product in self.products.keys():
            kept_comments = []
            for comment in product.comments:
                if comment.date_added >= date:
                    kept_comments.append(comment)
            product.comments = kept_comments

    def get_comments_by_bought_users(self, product):
        bought_user_comments = []

        for comment in product.comments:
            comment_owner_bought_products = comment.user.bought_products
            if product in comment_owner_bought_products:
                bought_user_comments.append(comment.text)

        return bought_user_comments
