from model.python.classes.Scenario import Scenario
from model.python.classes.ScenarioFactory import ScenarioFactory
import os

class Trumbo :

    _SF:ScenarioFactory = ScenarioFactory()

    def __init__(self) -> None:
        pass

    def analyse_scenario(self,_input_path:str,_ouput_path:str=""):
        scenario = self._SF.create(_input_path)
        return scenario.get_content()
        
        ...

