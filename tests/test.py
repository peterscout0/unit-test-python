def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0  # Se espera que el total sea 0 si la lista de productos está vacía

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products) == 12


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()

'''

Tipos de Testing:

Testing Unitario: Verifica el correcto funcionamiento de unidades individuales de código, como funciones o métodos.
Testing de Integración: Asegura que los diferentes módulos o componentes funcionen bien en conjunto.
Testing de Sistema: Evalúa el sistema completo para asegurarse de que cumple con los requisitos especificados.
Testing de Aceptación: Verifica que el software satisface las necesidades del usuario final.
Testing de Regresión: Asegura que los cambios o actualizaciones no hayan introducido nuevos errores en funcionalidades ya existentes.

'''