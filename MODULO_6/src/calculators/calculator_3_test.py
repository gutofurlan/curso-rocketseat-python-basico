from pytest import raises
from .calculator_3 import Calculator3
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handle_interface import DriverHandleInterface
from src.main.factories.calculator3_factory import calculator3_factory

class MockDriverHandle(DriverHandleInterface):
    def standard_derivation(self, numbers : List[float]) -> float:
        return 3

    def variance(self, numbers : List[float]) -> float:
        return 3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate_with_body_error():
    # ASSERTIVIDADE DE EXCEPTION
    mock_request = MockRequest(body={"number": 1})
    calculator_3 = calculator3_factory()

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Number field is missing"

def test_calculate_with_error_variance_smaller_multiplication():
    # ASSERTIVIDADE DE EXCEPTION
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = calculator3_factory()

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Falha no processo: Variancia Menor que multiplicacao"


def test_calculate():
    mock_request = MockRequest(body={ "numbers": [1, 1, 1, 100] })
    driver = NumpyHandler()
    calculator_3 = Calculator3(driver)

    response = calculator_3.calculate(mock_request)
    print(response)
    # formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "value" in response["data"]
    assert "success" in response["data"]
    #
    # #ASSERTIVIDADE DA RESPOSTA
    assert response["data"]["Calculator"] == 3
    assert response["data"]["value"] == 1837.6875
    assert response["data"]["success"] == True
    #
    assert isinstance(response, dict) #VAlida o tipo da instancia
    assert response == {'data': {'Calculator': 3, 'value': 1837.6875, 'success': True}}


