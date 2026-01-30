class DefaultModel:
    def __init__(self, id:int, descripcion:str):
        self.id = id
        self.descripcion = descripcion

        
    def __str__(self):
        return f"[ID: {self.id}] {self.descripcion}"

    