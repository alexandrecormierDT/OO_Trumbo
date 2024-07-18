from model.python.classes.ScenarioContentPlace import ScenarioContentPlace
from model.python.classes.ScenarioContentCharacter import ScenarioContentCharacter
from model.python.classes.ScenarioContentScene import ScenarioContentScene

class ScenarioContentSceneFactory():

    
    def __init__(self) -> None:
        pass


    def create(self,_data:dict)->ScenarioContentScene:
        print("CREATE SCENE")
        if self._validate_data(_data)==False:
            return ScenarioContentScene("empty_scene")
        name = _data["number"]
        scene = ScenarioContentScene(name)
        scene.set_place(ScenarioContentPlace(_data["place"]))
        scene.set_lines(_data["lines"])
        characters = self._get_characters(_data)
        for char in characters:
            scene.add_character(char)
        return scene
    
    def _get_characters(self,_data:dict)->list:
        list = []
        if "characters" not in _data.keys():
            return list
        for char_name in _data["characters"]:
            name = "ch_"+char_name.lower()
            character = ScenarioContentCharacter(name)
            list.append(character)
        return list
            
    def _validate_data(self,_data:dict)->bool:
        return True
        if ["number","place","lines"] in _data.keys():
            return True
        return False


    



    