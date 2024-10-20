from flask import request as FlaskRequest
from typing import Dict, List

from src.drivers.interfaces.driver_handle_interface import DriverHandleInterface
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:

    '''

    N Numeros sao enviados
    Todos esses N numeros sao multiplicados 11 e elevado a 0.95
    Por fim é retirado o desvio padrao desses resultado e retornando o inverso desse valor (1/result)

    '''

    def __init__(self, driver_handle : DriverHandleInterface) -> None:
        self.__driver_handle = driver_handle

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        print(input_data)

        calculator_number = self.__process_data(input_data)
        response = self.__format_response(calculator_number)
        return response

    #valida body
    def __validate_body(self, body: Dict)->List[float]:
        if "numbers" not in body:
            raise Exception("Number field is missing")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data : List[float]) -> float:
        first_process_result = [ (num * 11) ** 0.95 for num in input_data ]
        result = self.__driver_handle.standard_derivation(first_process_result)
        print(1/result)
        return 1/result

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calc_result, 2) # Deixa com 2 casa decimais
            }
        }