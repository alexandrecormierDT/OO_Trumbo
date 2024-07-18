import enchant

class WordChecker():

    _french_dictionnary =None
    _temp_list = ["projet","cette","prenant","un","une","je","le","les","se","mer","quoi","si","merci","au","dans","il","elle","tu","et","sous","grande","raaah","de","mais","face","sous","brume","toi","non","oui","panique","nous","vous","ils","on","off","la","le","tout","soudain"]

    def __init__(self):
        #print("The dict is", enchant.list_languages())
        #self._french_dictionnary = enchant.Dict("fr_FR")
        pass
    def is_a_word(self,_w:str):
        return _w in self._temp_list
        if self._french_dictionnary.check(_w):
            print("is a word")
            return True
        print("is not a word")
        return False
