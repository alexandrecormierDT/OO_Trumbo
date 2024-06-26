from model.python.classes.ScenarioParserAbstract import ScenarioParserAbstract



class Scenario:

    
    def __init__(self,_path:str) -> None:
        self._path = _path
        self._parsing_strategy:ScenarioParserAbstract = None
        self._content = {}
        self._scenes = []
        self._episode = []
        pass

    def get_path(self)->str:
        return self._path
    
    def _parse(self)->str:
        if self._parsing_strategy is None:
            return {}
        self._content = self._parsing_strategy.parse(self._path)
        return self._content
      
    
    def get_content(self)->str:
        return self._content
    