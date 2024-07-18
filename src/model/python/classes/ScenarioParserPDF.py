from model.python.classes.ScenarioParserAbstract import ScenarioParserAbstract
from pypdf import PdfReader 
import re

from model.python.classes.ScenarioContentScene import ScenarioContentScene
from model.python.classes.ScenarioContentSceneFactory import ScenarioContentSceneFactory
from model.python.classes.WordChecker import WordChecker

class ScenarioParserPDF(ScenarioParserAbstract):

    _SCSF:ScenarioContentSceneFactory = ScenarioContentSceneFactory()
    _WC:WordChecker = WordChecker()

    def __init__(self):
        self._pages = []
        pass

    def parse(self,_path:str)->dict:
        raw = self._get_raw_text(_path)
        lines = raw.split("\n")
        current_scene = None
        current_episode = "no_episode"
        scenes = []
        for line in lines: 
            if self._is_episode(line) == True:
                current_episode = line
                continue
            scene = self._get_scene(line)
            if scene is not None:
                if current_scene is not None:
                    current_scene["episode"] = current_episode
                    current_scene["characters"] = self._parse_characters(current_scene["lines"])
                    scenes.append(current_scene)
                current_scene = scene
                continue
            if current_scene is not None:
                current_scene["lines"].append(line)
        Sscenes = []
        for data in scenes:
            print(data)
            nscene = self._create_scene(data)
            print(nscene)
            Sscenes.append(nscene.get_dict())
        return Sscenes
            

    def _is_episode(self,_string)->bool:
        if "- EP" in _string:
            return True
        return False
    
    def _create_scene(self, _data:dict) -> ScenarioContentScene:
        return self._SCSF.create(_data)
    
    def _is_a_word(self,_word:str):
        print("*****************************")
        print("IS A WORD ? ")
        print(_word)
        return self._WC.is_a_word(_word)

 
    def _get_scene(self,_string):
        if self._is_place(_string)==False:
            return None
        scene = {
            "episode":"",
            "number":_string.split(".")[0],
            "place":".".join(_string.split(".")[1:]),
            "characters":[],
            "props":[],
            "lines":[]
        }
        return scene
    
    def _get_capitalized(self,_string:str):
        list = []
        result = re.findall("([A-Z]([a-z]+|\.))",_string)
        if result is None:
            return list
        for g1,g2 in result:
            list.append(g1)
        return list
    
    def _get_upper_words(self,_string:str):
        list = []
        result = re.findall("[0-9]\.\s([A-Z]([A-Z]+|\.))",_string)
        if result is None:
            return list
        for g1,g2 in result:
            list.append(g1)
        return list
        
    def _parse_characters(self,_lines:list)->list:
        raw = "".join(_lines)
        #wip
        #capital = self._get_capitalized(raw)
        #names = [word.lower() for word in capital if self._is_a_word(word.lower())==False]
        upper = self._get_upper_words(raw)
        names = [word.lower() for word in upper]
        unique_names = list(set(names))
        return unique_names


    def _is_place(self,_string)->bool:
        if "EXT" in _string:
            return True
        if "INT" in _string:
            return True
        if "JOUR" in _string:
            return True
        return False
        
    
    def clean_character(self,_string:str)->str:
        return _string.replace(" ","")
    
    def _get_raw_text(self,_pdf:str)->str:
        reader = PdfReader(_pdf) 
        all_pages = ""
        for page in reader.pages:
            all_pages+=page.extract_text() 
        return all_pages





