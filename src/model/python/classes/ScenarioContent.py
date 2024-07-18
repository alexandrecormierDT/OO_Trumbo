
class ScenarioContent:
    
    def __init__(self,_name:str) -> None:
        self._name = _name
        self._meta = {}
        pass

    def get_meta(self,_key)->str:
        return 
    
    def set_meta(self,_key,_value):
        return self
    
    def __str__(self) -> str:
        return self._name
    
    def get_name(self)->str:
        return self._name