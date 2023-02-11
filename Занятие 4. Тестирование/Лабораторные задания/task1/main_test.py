import unittest

from main import Pets
from main import Cat


class TestPets(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("setUpClass")
    #     cls.pet = Pets("Cat", "Maincoon", "Hulk", 10)
    def setUp(self):
        self.pet = Pets("Cat", "Maincoon", "Hulk", 10)

    def test_count(self):
        self.assertEqual(self.pet.counter, 1)
        self.assertEqual(Pets.counter, 1)
        self.pet1 = Pets("Cat", "Maincoon", "Hulk", 10)
        self.assertEqual(self.pet.counter, 2)
        self.assertEqual(Pets.counter, 2)

    def test_init(self):
        self.assertEqual(self.pet.kind, "Cat")
        self.assertEqual(self.pet.breed, "Maincoon")
        self.assertEqual(self.pet.name, "Hulk")
        self.assertEqual(self.pet.age, 10)

    def test_kind(self):
        self.assertEqual(self.pet.kind, "Cat")
        self.assertTrue(isinstance(self.pet.kind, str))
        self.assertIsInstance(self.pet.kind, str)

    def test_breed(self):
        self.assertEqual(self.pet.breed, "Maincoon")
        self.assertTrue(isinstance(self.pet.breed, str))
        self.assertIsInstance(self.pet.breed, str)

    def test_is_valid_kind_breed(self):
        self.assertIsInstance(self.pet.breed, str)
        self.assertIsInstance(self.pet.kind, str)
        self.assertTrue(self.pet.is_valid_kind_breed)
        self.assertTrue(Pets.is_valid_kind_breed("cat", "maincoon"))
        self.assertEqual(Pets.is_valid_kind_breed("cat", "maincoon"), "Вид и порода валидны")
        with self.assertRaises(TypeError):
            Pets.is_valid_kind_breed(123, "maincoon")
        with self.assertRaises(TypeError):
            Pets.is_valid_kind_breed("cat", 123)

    def test_name(self):
        self.assertEqual(self.pet.name, "Hulk")
        self.assertIsInstance(self.pet.name, str)
        with self.assertRaises(TypeError):
            self.pet.name = 123
        self.pet.name = "Jerry"
        self.assertEqual(self.pet.name, "Jerry")

    def test_age(self):
        self.assertEqual(self.pet.age, 10)
        self.pet.age = 11
        self.assertEqual(self.pet.age, 11)
        with self.assertRaises(ValueError):
            self.pet.age = 0
        with self.assertRaises(TypeError):
            self.pet.age = 11.1
        with self.assertRaises(TypeError):
            self.pet.age = "10"

    def test_repr(self):
        self.assertEqual(self.pet.__repr__(), "Pets(kind='Cat', breed='Maincoon', name='Hulk', age=10)")

    def test_str(self):
        self.assertEqual(self.pet.__str__(), "Вид: Cat, порода: 'Maincoon', кличка: 'Hulk', возраст: 10")


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("munchkin", "jerry", 9, "высокая")

    def test_init(self):
        self.assertEqual(self.cat.kind, "Кот")
        self.assertEqual(self.cat.breed, "munchkin")
        self.assertEqual(self.cat.name, "jerry")
        self.assertEqual(self.cat.age, 9)
        self.assertEqual(self.cat.affectionateness, "высокая")

    def test_affectionateness(self):
        self.assertEqual(self.cat.affectionateness, "высокая")
        self.assertIsInstance(self.cat.affectionateness, str)
        with self.assertRaises(TypeError):
            self.cat.name = 123
        self.cat.name = "Jerry1"
        self.assertEqual(self.cat.name, "Jerry1")

    def test_repr(self):
        self.assertEqual(self.cat.__repr__(), "Cat(breed='munchkin', name='jerry', age=9, affectionateness=высокая)")

    def test_str(self):
        self.assertEqual(self.cat.__str__(), "Вид: Кот, порода: 'munchkin', кличка: 'jerry', возраст: 9")

# if __name__ == '__main__':
#     unittest.main()
