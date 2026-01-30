from models.defaultModel import DefaultModel
from logic.defaultController import DefaultController
from persistencia.DefaultRepository import DefaultRepository

def run():
    controlador = DefaultController()

    item1 = DefaultModel(1,"Elemento 1")
    item2 = DefaultModel(2,"Elemento 2")

    controlador.agregar_item(item1)
    controlador.agregar_item(item2)

    print("\n--- Estado Actual del Inventario ---")
    controlador.mostrar_items()

if __name__ == "__main__":
    run()