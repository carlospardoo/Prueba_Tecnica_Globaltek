


def __init__():
    print('Prueba Tecnica Globaltek')
    array = [{"nombre": "John", "apellido": "Doe"}, {"nombre": "Jane", "apellido": None}, {"nombre": "Jose", "apellido":
"Doe"}]
    arg = {"apellido": "Doe"}
    print(findBySecondArgument(array, arg))

def findBySecondArgument(array, arg):
    array2 = []

    for key in arg:
        continue

    for aux in array:
        if aux[key] == arg[key]:
            array2.append(aux)
    
    return array2

if __name__ == "__main__":
    __init__()
