from model.python.classes.ScenarioParserAbstract import ScenarioParserAbstract
from model.python.classes.ScenarioParserPDF import ScenarioParserPDF
from model.python.classes.ScenarioParserTXT import ScenarioParserTXT
from model.python.classes.ScenarioParserDefault import ScenarioParserDefault
from model.python.classes.Scenario import Scenario

class ScenarioFactory:
    
    def __init__(self) -> None:
        pass

    def _get_parsing_strategy(self,_path:str)->ScenarioParserAbstract:
        extension = _path.split(".")[-1]
        if extension == "pdf":
            return ScenarioParserPDF()
        if extension == "txt":
            return ScenarioParserTXT()
        return ScenarioParserDefault()
        

    def create(self,_path:str)->Scenario:
        scenario = Scenario(_path)
        scenario._parsing_strategy = self._get_parsing_strategy(_path)
        scenario._parse()
        return scenario
        




