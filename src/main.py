import sys
sys.path.insert(0,'P:/pipeline/extra_scripts/python_include')

import argparse
import os
import json
from control.python.classes.Trumbo import Trumbo



'''
python P:/pipeline/dev/a.cormier/core/editors/scenarios/repos/OO_Trumbo/src/main.py -analyse -i "P:/projects/testa/storyboard/scenarios/RIV_106_Script_Un_tsunami_de_sentiments_VF_VAL.pdf" -o "P:/projects/testa/storyboard/scenarios/report.json"
'''

def main(_args):
    Tr = Trumbo()
    if _args.analyse==True and _args.input_path and _args.output_path:
        report = Tr.analyse_scenario(_args.input_path)
        with open(_args.output_path,"w") as file:
            file.write(json.dumps(report))

if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input_path",required=True)
    parser.add_argument("-analyse","--analyse",action="store_true")
    parser.add_argument("-o","--output_path")
    args = parser.parse_args()
    main(args)