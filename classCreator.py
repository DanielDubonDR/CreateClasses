import os

path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"\\newClass.py"

def createClass(nombreClase="NombreClase", variables="variable", direccion=None, GettersAndSetters=False):
    atributos = variables.replace(" ","").split(",")
    string =  "class "+nombreClase+":\n"
    string+= "\tdef __init__(self, "+variables+"):\n"

    for atributo in atributos:
        string+="\t\tself."+atributo+" = "+atributo+"\n"

    string+= "\n\tdef __str__(self):\n"
    string+="\t\tstring = "

    for atributo in atributos:
        string+="\""+str(atributo.capitalize())+": \""+"+str(self."+atributo+")+\"\\n\"+"

    string=string.rstrip("+\"\\n")
    string+="\n\t\treturn string\n\n"

    if GettersAndSetters:
        string+="\t#Getter's\n"
        for atributo in atributos:
            string+="\tdef get"+str(atributo.capitalize())+"(self):"
            string+="\n\t\treturn self."+atributo+"\n\n"
        
        string+="\t#Setter's\n"
        for atributo in atributos:
            string+="\tdef set"+str(atributo.capitalize())+"(self, "+atributo+"):"
            string+="\n\t\tself."+atributo+" = "+atributo+"\n\n"

    if direccion==None:
        direccion=path_desktop
        print("Se creo el archivo en:", path_desktop)
    archivo = open(direccion, "a")
    archivo.write(string)
    archivo.close()