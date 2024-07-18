from model.python.classes.ScenarioParserAbstract import ScenarioParserAbstract
from model.python.classes.ScenarioContentScene import ScenarioContentScene


class ScenarioParserTXT(ScenarioParserAbstract):

    def __init__(self):
        pass

    def parse(self,_path:str)->dict:
        pass

    def _get_raw_text(self,_pdf:str)->str:
        pass

    def _create_scene(self,_data:dict)->ScenarioContentScene:
        pass