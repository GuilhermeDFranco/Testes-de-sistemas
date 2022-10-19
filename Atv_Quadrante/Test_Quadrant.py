
from Coordinate import Coordinate
from Quadrant import Quadrant
from pytest import mark

def test_all_quadrants():
    
    #Arange
    positivo = 1
    negativo = -1

    quadrant_1 = Quadrant(Coordinate(positivo, positivo))
    quadrant_2 = Quadrant(Coordinate(positivo, negativo))
    quadrant_3 = Quadrant(Coordinate(negativo, positivo))
    quadrant_4 = Quadrant(Coordinate(negativo, negativo))

    # Act / Action
    result_1 = quadrant_1.get_quadrant_coordinate()
    result_2 = quadrant_2.get_quadrant_coordinate()
    result_3 = quadrant_3.get_quadrant_coordinate()
    result_4 = quadrant_4.get_quadrant_coordinate()

    # Assert
    assert result_1 == "First"
    assert result_2 == "Fourth"
    assert result_3 == "Second"
    assert result_4 == "Third"


def test_exit():

    #Arange
    quadrant = Quadrant(Coordinate(1, 0))

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == ""


@mark.xfail
def test_number():

    #Arange
    quadrant = Quadrant(Coordinate("c", 4))

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == ""