from model.python.classes.ScenarioContent import ScenarioContent
from model.python.classes.ScenarioContentPlace import ScenarioContentPlace
from model.python.classes.ScenarioContentCharacter import ScenarioContentCharacter

class ScenarioContentScene(ScenarioContent):

    
    def __init__(self,_name) -> None:
        super().__init__(_name)
        self._characters = []
        self._place:ScenarioContentPlace = None
        self._lines:list = []
        pass


    def add_character(self,_char:ScenarioContentCharacter):
        return self
    
    def set_place(self,_place:ScenarioContentPlace):
        return self
    
    



    