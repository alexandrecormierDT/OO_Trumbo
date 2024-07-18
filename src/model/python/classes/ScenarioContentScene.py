from model.python.classes.ScenarioContent import ScenarioContent
from model.python.classes.ScenarioContentPlace import ScenarioContentPlace
from model.python.classes.ScenarioContentCharacter import ScenarioContentCharacter

class ScenarioContentScene(ScenarioContent):

    
    def __init__(self,_name) -> None:
        super().__init__(_name)
        self._episode = ""
        self._characters = []
        self._place:ScenarioContentPlace = None
        self._lines:list = []
        self._fx:list= []
        self._characters:list= []
        self._places:list= []
        self._props:list = []
        self._dial:list = []
        pass


    def add_character(self,_char:ScenarioContentCharacter):
        self._characters.append(_char)
        return self
    
    def set_lines(self,_l:list):
        self._lines = _l
        return self
    
    def set_place(self,_place:ScenarioContentPlace):
        self._place=_place
        return self
    
    def get_dict(self)->dict:
        dict = {
            "episode":self._episode,
            "name":self._name,
            "place":self._place.get_name(),
            "props":[prop.get_name() for prop in self._props],
            "characters":[char.get_name() for char in self._characters],
            "lines":self._lines
        }
        return dict
        ...

    def _get_string(self)->str:
        dict = self.get_dict()
        string = "------------------------------------------------"
        string+="NAME : "+dict["name"]+"\n"
        string+="PLACE : "+dict["place"]+"\n"
        string+="CHARACTERS : "+",".join(dict["characters"])+"\n"
        string+="TEXT : "+"\n".join(dict["lines"])+"\n"
        return string
    
    def __str__(self) -> str:
        return self._get_string()
    
    def __repr__(self) -> str:
        return self._get_string()
    
    



    