import json
from typing import List
from pytype import load_pytd

def extract_types(filename:str)->None:
    # Load the pytd file with the types
    pytd = load_pytd(filename)
    variables = pytd.lookup("")
    with open("types.txt", "w") as outfile:
        for variable in variables.items():
            name = variable[0]
            _type = variable[1].name
            outfile.write(f"{name}:{_type}\n")




extract_types("proyectoFinal.py")