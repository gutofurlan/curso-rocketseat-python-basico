from pytest import raises
from .calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handle_interface import DriverHandleInterface
from src.main.factories.calculator2_factory import calculator2_factory

class MockDriverHandle(DriverHandleInterface):
    def standard_derivation(self, numbers : List[float]) -> float:
        return 3

    def variance(self, numbers : List[float]) -> float:
        return 1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

#Integracao entree numpy e calculator
def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })
    calculator_2 = calculator2_factory()

    response = calculator_2.calculate(mock_request)
    print(response)
    #formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    #
    # #ASSERTIVIDADE DA RESPOSTA
    assert response["data"]["Calculator"] == 2
    assert response["data"]["result"] == 0.08

    assert isinstance(response, dict) #VAlida o tipo da instancia
    assert response == {'data': {'Calculator': 2, 'result': 0.08}}

def test_calculate_with_body_error():
    # ASSERTIVIDADE DE EXCEPTION
    mock_request = MockRequest(body={"number": 1})
    calculator_2 = calculator2_factory()

    with raises(Exception) as excinfo:
        calculator_2.calculate(mock_request)

    assert str(excinfo.value) == "Number field is missing"


def test_calculate():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })
    driver = MockDriverHandle()
    calculator_2 = Calculator2(driver)

    response = calculator_2.calculate(mock_request)

    #formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    #
    # #ASSERTIVIDADE DA RESPOSTA
    assert response["data"]["Calculator"] == 2
    assert response["data"]["result"] == 0.33

    assert isinstance(response, dict) #VAlida o tipo da instancia
    assert response == {'data': {'Calculator': 2, 'result': 0.33}}


