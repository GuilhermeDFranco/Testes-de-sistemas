from sqlite3 import InterfaceError
from MenuRepository import MenuRepository
from Order import Order
from UserInterface import UserInterface

def test_get_user_input():

    order3 = Order(2,4)

    menu = MenuRepository()

    interface = UserInterface(menu)

    teste = interface.get_user_input()
    
    assert order3.code == teste.code
    assert order3.quantity == teste.quantity