from abc import ABC,abstractmethod
from model.python.classes.ScenarioContentScene import ScenarioContentScene

class ScenarioParserAbstract(ABC):

    @abstractmethod
    def parse(self,_path:str)->dict:
        pass
    
    @abstractmethod
    def _get_raw_text(self,_pdf:str)->str:
        pass

    @abstractmethod
    def _create_scene(self,_data:dict)->ScenarioContentScene:
        pass