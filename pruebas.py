import doctest
import unittest

def factorial(n):
    """

    >>> factorial(3)
    6
    >>> factorial(4)
    25
    """
    return 1 if n < 1 else n * factorial(n-1)

class tester (unittest.TestCase):
    def test1(self):
        self.assertEqual(1,factorial(1))
    def test2(self):
        self.assertEqual(1,factorial(0))
    def test3(self):
        self.assertEqual(24,factorial(4))

if __name__ == "__main__":
    doctest.testmod()
    #unittest.main()

# despues ir a la terminal y ejecutar:
# para doctest:
# python3 rutaquesea/pruebas.py -v
# para unittest
# python3 -m unittest rutaquesea/pruebas.py