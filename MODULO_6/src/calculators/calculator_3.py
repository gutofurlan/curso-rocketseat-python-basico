from http.client import responses
from statistics import variance

from flask import request as FlaskRequest
from typing import Dict, List

from src.drivers.interfaces.driver_handle_interface import DriverHandleInterface
from src.drivers.numpy_handler import NumpyHandler

class Calculator3:

    '''

    N N numeros sao enviados
    Caso a variancia de todos esses numeros fir menor que a multiplicacao deles, é apresentado uma info de sucesso
    Caso contrario é apresentado uma onfo de falha

    '''

    def __init__(self, driver_handle : DriverHandleInterface) -> None:
        self.__driver_handle = driver_handle

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        print(input_data)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_result(variance, multiplication)
        response = self.__format_response(variance)
        return response

    #valida body
    def __validate_body(self, body: Dict)->List[float]:
        if "numbers" not in body:
            raise Exception("Number field is missing")

        input_data = body["numbers"]
        return input_data

    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "success": True
            }
        }

    def __calculate_variance(self, numbers:List[float]) -> float:
        variance = self.__driver_handle.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers:List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num

        return multiplication

    def __verify_result(self, variance:float, multiplication:float) -> None:
        if variance < multiplication:
            raise Exception("Falha no processo: Variancia Menor que multiplicacao")