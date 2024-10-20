from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1
from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory
#renomei todas as rotas de calculadoras de calc_routes
calc_routes_bp = Blueprint('calc_routes', __name__)

@calc_routes_bp.route('/calculator/1', methods=['POST'])
def calculator1():
    # print(request.json) #body
    calc = Calculator1()
    response = calc.calculate(request)
    return jsonify(response), 200

@calc_routes_bp.route('/calculator/2', methods=['POST'])
def calculator2():
    # print(request.json) #body
    calc = calculator2_factory()
    response = calc.calculate(request)
    return jsonify(response), 200

@calc_routes_bp.route('/calculator/3', methods=['POST'])
def calculator3():
    # print(request.json) #body
    calc = calculator3_factory()
    response = calc.calculate(request)
    return jsonify(response), 200