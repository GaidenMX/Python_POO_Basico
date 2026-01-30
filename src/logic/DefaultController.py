from models.defaultModel import DefaultModel
from persistencia.DefaultRepository import DefaultRepository

class DefaultController:

    def __init__(self, repositorio:DefaultRepository):
        self.__repositorio = repositorio
        self.__lista = self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        raw_data = self.__storage.cargar_datos()
        # Convertimos diccionarios JSON de vuelta a objetos Product
        return {item['id']: DefaultModel(**item) for item in raw_data}

    def agregar_item(self, default: DefaultModel):
        self.__lista[default.id]=default
        self._sync_repositorio()
        print(f"Elemento '{default.descripcion}' registrado.")

    def mostrar_items(self):
        if not self.__lista:
            print("Lista vacia.")
            return
        for item in self.__lista.values():
            print(item)
    
    def _sync_repositorio(self):
        # Convertimos objetos a diccionarios para JSON
        data_to_save = [vars(p) for p in self.__lista.values()]
        self.__storage.guardar_datos(data_to_save)