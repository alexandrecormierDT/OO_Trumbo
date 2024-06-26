import enchant

class WordChecker():

    _french_dictionnary =None

    def __init__(self):
        print("The dict is", enchant.list_languages())
        self._french_dictionnary = enchant.Dict("fr_FR")

        ...

    def is_a_word(self,_w:str):
        if self._french_dictionnary.check(_w):
            print("is a word")
            return True
        print("is not a word")
        return False
