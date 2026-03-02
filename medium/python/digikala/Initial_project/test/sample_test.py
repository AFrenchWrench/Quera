import unittest
from datetime import datetime
import sys
sys.path.append('../Initial_project')
from models import User, Product, Comment
from store import Store


class TestAll(unittest.TestCase):

    @staticmethod
    def comment_create(text, user, date):
        cmt = Comment(text, user)
        cmt.date_added = datetime.strptime(date, '%Y-%m-%d')
        return cmt

    def populate_users(self, store):
        users = [
            User('SAliB'),
            User('Ali'),
            User('Sajjad'),
            User('Seyed')
        ]
        store.users = users

    def populate_products(self, store):

        p1 = Product('P1', 1, 'C1', 'Digi_Style')
        p1.comments.extend([self.comment_create('random comment1', store.users[0], "2018-10-10"),
                            self.comment_create('random comment2', store.users[3], "2018-10-09"),
                            self.comment_create('random comment3', store.users[2], "2018-10-02"),
                            self.comment_create('random comment4', store.users[3], "2018-10-01"),
                            self.comment_create('random comment5', store.users[2], "2018-09-01"),
                            self.comment_create('random comment6', store.users[2], "2018-09-01")])
        p1_expensive = Product('P1', 10, 'C1', 'Digi_Kala')
        p1_more_expensive = Product('P1', 100, 'C1', 'Digi_Kala')
        p2 = Product('P2', 2, 'C2')
        p2.comments.extend([self.comment_create('P2 comment1', store.users[2], "2018-10-10"),
                            self.comment_create('P2 comment2', store.users[0], "2018-10-09"),
                            self.comment_create('P2 comment3', store.users[1], "2018-10-02"),
                            self.comment_create('P2 comment4', store.users[2], "2018-10-01"),
                            self.comment_create('P2 comment5', store.users[3], "2018-09-01"),
                            self.comment_create('P2 comment6', store.users[1], "2018-09-01"),
                            self.comment_create('P2 comment7', store.users[1], "2018-09-01")])
        products = {
            p1: 2,
            p1_expensive: 3,
            p1_more_expensive: 4,
            p2: 2
        }
        store.products = products

    def setUp(self):
        self.store_user = Store()
        self.populate_users(self.store_user)
        self.populate_products(self.store_user)

    def test_remove_product(self):
        p1 = list(self.store_user.products.keys())[0]
        p2 = list(self.store_user.products.keys())[1]

        count = self.store_user.products[p1]
        self.store_user.remove_product(p1, 1)
        self.assertEqual(self.store_user.products[p1], count - 1)

        self.store_user.remove_product(p1, self.store_user.products[p1])
        self.assertNotIn(p1, self.store_user.products.keys())

        try:
            self.store_user.remove_product(p2, 10)
        except Exception as e:
            self.assertEqual(str(e), 'Not Enough Products')
            return
        self.assertEqual(1, 0)  # fail if reaches this line

    def test_add_user(self):
        self.assertEqual(None, self.store_user.add_user('SAliB'))
        self.assertEqual("Seyed_Ali", self.store_user.add_user('Seyed_Ali'))

    def test_get_inflation_affected_product_names(self):
        self.assertCountEqual(['P1'], self.store_user.get_inflation_affected_product_names())
        self.assertIn('P1', self.store_user.get_inflation_affected_product_names())


if __name__ == '__main__':
    unittest.main()