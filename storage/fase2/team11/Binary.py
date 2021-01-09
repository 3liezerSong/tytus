import pickle
import os.path as path
import re
import os
from PIL import Image

def commit(obj, file_name):  # Escribe los archivos

    if path.exists("./data/"):
        file = open(f"./data/{file_name}.bin", "wb+")
        file.write(pickle.dumps(obj))
        file.close()
    else:
        os.makedirs('./data/')
        return commit(obj, file_name)


def rollback(file_name):  # Cargar los elementos que estan en el archivo binario
    if path.exists(f"./data/{file_name}.bin"):
        file = open(f"./data/{file_name}.bin", "rb")
        b = file.read()
        file.close()
        return pickle.loads(b)
    return None


# Metodo que se encarga de verficar que los nombres cumplan con la nomenclatura de las base de datos
# Retorna True -> Si cumple
# False -> si NO cumple

def verify_string(string):
    patron = re.compile('[a-zA-Z_][a-zA-z0-9_]*')
    match = patron.match(str(string))
    if match:
        if match.group() is string:
            return True
    return False


def verify_columns(nums_columns, columns):
    if isinstance(columns, list):
        patron = re.compile(f"[0-{nums_columns}]")
        for value in columns:
            column = f"{value}"
            match = patron.match(column)
            if match is None:
                return False
        return True
    else:
        #print("entro al verify")
        return 1
    
    
def generate_grapviz(cadena, path_file, ):
    if path.exists("./resource/"):
        file = open("./resource/" + path_file + ".dot", "w", encoding="utf-8")
        file.write(str(cadena))
        file.close()
        from graphviz import render
        render('dot', 'png', f'./resource/{path_file}.dot')
        f'./resource/{path_file}.dot.png'
        #f = Image.open(f'./resource/{path_file}.dot.svg')
        #f.show()d
    else:
        os.makedirs('./resource/')
        return generate_grapviz(cadena, path_file)#
