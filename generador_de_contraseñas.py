import random 

archive = "guardar.txt"

def guardar(data, pw):
    dt = data
    psw = pw
    with open(archive,"w") as archivo:
        archivo.writelines(f"{dt}\n")

def cargar():
    with open("guardar.txt", "r") as archivo:
        contenido = archivo.read()
        # for linea in lineas:
        #     print(linea)
        return contenido

list = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[',
    ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~'
]

def gen(gen,long):
    per = int(gen)
    if per == 1:
        password = 0
        password += 1
        qu = int(long)

        gn = [random.choice(list) for i in range(qu)]
        generator = str(gn)
        result = generator.replace('[', "")
        result = result.replace(']',"")
        result = result.replace(",","")
        result = result.replace("'","")
        result = result.replace(" ","")
        
        guardar(result,password)
    
        print(f'{result}:{password}')
    
        return result