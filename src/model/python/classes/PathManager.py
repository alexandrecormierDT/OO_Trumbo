from os import path, mkdir, getenv
import json


class PathManager:

    _script_path = __file__

    def __init__(self) -> None:
        pass

    def upstream_path(_path: str, _iterations: int) -> str:
        # return a path with a depth of _iterations
        last_path = _path
        for i in range(1, _iterations):
            parent = path.dirname(last_path)
            last_path = parent
        return last_path
    
    def get_folder_path(self,_name):
        module_folder = PathManager.upstream_path(PathManager._script_path, 6)
        fpath = module_folder + "/src/"+_name
        print(fpath)
        if path.exists(fpath):
            return fpath
        return ""        
   
    def clean_back_slash(p_path: str) -> str:
        sanitize_path = p_path.replace("\\", "/")
        return sanitize_path
        
    def get_file_type(self,_path:str)->str:
        file_type = None
        if path.isdir(_path):
            file_type = "folder"
        else:
            file_type = _path.split(".")[-1]
        return file_type
    
    def get_archive_in_path(self,_path:str)->str:
        split = self.split_path(_path)
        cut = ""
        for index in range(len(split)):
            part = split[index]
            if "." not in part:
                continue
            ext = part.split(".")[-1]
            if ext != "7z":
                continue
            cut = index
            break
        if cut == "":
            return ""
        return self.cut_path(_path,cut)
    
    def split_path(self,_path:str)->list:
        clean = PathManager.clean_back_slash(_path)
        return clean.split("/")
    
    def cut_path(self,_path:str,_index_cut:int)->str:
        if isinstance(_index_cut,int)==False:
            return _path
        split = self.split_path(_path)
        parts = []
        for index in range(len(split)):
            if index > _index_cut:
                break
            parts.append(split[index])
        return '/'.join(parts)

    def pop_path(self,_path:str,_index_cut:int)->str: # cut before index
        if isinstance(_index_cut,int)==False:
            return _path
        split = self.split_path(_path)
        parts = []
        for index in range(len(split)):
            if index < _index_cut:
                continue
            parts.append(split[index])
        return '/'.join(parts)
    
    def create_temp_root_folder(self,_name):
        tpath = getenv("TEMP")+"/"+_name
        if path.exists(tpath)==False:
            print("[PathManager] creating temp root folder "+tpath)
            mkdir(tpath)
        return tpath

    def get_temp_folder(self,_sub_folder=""):
        root = self.create_temp_root_folder()
        tpath =root+"/"+_sub_folder
        if path.exists(tpath)==False:
            print("[PathManager] creating temp subfolder "+tpath)
            mkdir(tpath)
        clean = PathManager.clean_back_slash(tpath)
        return clean
    
    def get_data_path()->str:
        module_folder = PathManager.upstream_path(PathManager._script_path, 6)
        data_path = module_folder + "\\data"
        if path.exists(data_path):
            return data_path
        return ""
    
    def get_config_path(self)->str:
        return PathManager.get_data_path() + "\\config\\config.json"

    def validate(_path:str)->bool:
        bad_chars = ["[32m", "[39m"," ","é","*",",","ù","#"]
        for char in bad_chars:
            if char in _path:
                print("[ERROR] bad char "+char+" detected  in path ("+_path+")")
                return False
        if len(_path)>=255:
            print(f"[ERROR] path is too long {len(_path)} ({_path}) " )
            return False
        if len(_path)<10:
            print(f"[ERROR] path is too short {len(_path)} ({_path}) " )
            return False
        return True

        

    
