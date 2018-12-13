def transformar(expresion, tope, LISTA_RESULTADOS_PROVISORIOS):
    contador = 1
    lista_aux = []
    ultimo = len(expresion) - 2
    ultimo1 = len(expresion) - 1
    if len(expresion) != 1:
        for character in range(len(expresion) - 1):
            if expresion[character] != expresion[character + 1] or character == ultimo:
                if expresion[character] == "a":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            LISTA_RESULTADOS_PROVISORIOS.append(("[a-zA-Z]", tope))
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[a-zA-Z]", contador))
                            transformar(expresion[ultimo1], tope, lista_aux)
                        else:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[a-zA-Z]", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[a-zA-Z]", contador))
                    contador = 1
                elif expresion[character] == "n":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            LISTA_RESULTADOS_PROVISORIOS.append(("[0-9]", tope))
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[0-9]", contador))
                            transformar(expresion[ultimo1], tope, lista_aux)
                        else:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[0-9]", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[0-9]", contador))
                    contador = 1
                elif expresion[character] == "x":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            LISTA_RESULTADOS_PROVISORIOS.append(("[\w]", tope))
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[\w]", contador))
                            transformar(expresion[ultimo1], tope, lista_aux)
                        else:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[\w]", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[\w]", contador))
                    contador = 1
                elif expresion[character] == "&":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s]", tope))
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s]", contador))
                            transformar(expresion[ultimo1], tope, lista_aux)
                        else:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s]", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s]", contador))
                    contador = 1
                elif expresion[character] == "o":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s0-9]", tope))
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s0-9]", contador))
                            transformar(expresion[ultimo1], tope, lista_aux)
                        else:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s0-9]", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s0-9]", contador))
                elif expresion[character] == "c":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\sa-zA-Z]", tope))
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s][a-zA-Z]", contador))
                            transformar(expresion[ultimo1], tope, lista_aux)
                        else:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s][a-zA-Z]", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s][a-zA-Z]", contador))
                    contador = 1
                elif expresion[character] == "?":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-\/\s\w]", tope))
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-\/\s\w]", contador))
                            transformar(expresion[ultimo1], tope, lista_aux)
                        else:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[-\/\s\w]", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[-\/\s\w]", contador))
                elif expresion[character] == "w":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            LISTA_RESULTADOS_PROVISORIOS.append(("[\s]$", tope))
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[\s]$", contador))
                            transformar(expresion[ultimo1], tope, lista_aux)
                        else:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[\s]$", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[\s]$", contador))
                elif expresion[character] == ".":
                    pass
                elif expresion[character] == "b":
                    if character == ultimo:
                        if expresion[ultimo1] == "@":
                            pass
                            #LISTA_RESULTADOS_PROVISORIOS.append(["[b]+"])
                        elif expresion[ultimo] != expresion[ultimo1]:
                            LISTA_RESULTADOS_PROVISORIOS.append(("[b]", contador))
                            result2 = transformar(expresion[ultimo1], tope, lista_aux)
                            LISTA_RESULTADOS_PROVISORIOS.append(result2[0])
                        else:
                            pass
                            #LISTA_RESULTADOS_PROVISORIOS.append(("[b]", contador + 1))
                    else:
                        LISTA_RESULTADOS_PROVISORIOS.append(("[b]", contador))

            elif expresion[character] == expresion[character + 1]:
                contador += 1

    elif len(expresion) == 1:
        if expresion == "a":
            LISTA_RESULTADOS_PROVISORIOS.append(("[a-zA-Z]", 1))   #Ver si le agrego en una tupla el (RE,1).
        elif expresion == "n":
            LISTA_RESULTADOS_PROVISORIOS.append(("[0-9]", 1))
        elif expresion == "x":
            LISTA_RESULTADOS_PROVISORIOS.append(("[\w]", 1))
        elif expresion == "&":
            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s]", 1))
        elif expresion == "c":
            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\sa-zA-Z]", 1))
        elif expresion == "o":
            LISTA_RESULTADOS_PROVISORIOS.append(("[-/\s0-9]", 1))
        elif expresion == "?":
            LISTA_RESULTADOS_PROVISORIOS.append(("[-\/\s\w]", 1))
        elif expresion == "w":
            LISTA_RESULTADOS_PROVISORIOS.append(("[\s]$", 1))
        elif expresion == ".":
            pass
        elif expresion == "b":
            pass
            #LISTA_RESULTADOS_PROVISORIOS.append(("[b]", 1))
            #print("entre")

    return LISTA_RESULTADOS_PROVISORIOS

def cambio(UDID, LISTA_RESULTADOS_PROVISORIOS1, counter=0):
    for expresion in UDID.values():         # ---> [map, [start, finish], description, field]
        if len(expresion[1]) == 0:          # Pongo esto en los caso que no hay parámetros para los límites.
            expresion[1] = ["1", "50"]
        lista_clave1 = []
        lista_clave = transformar(expresion[0], expresion[1][1], lista_clave1)
        if expresion[0][0] == "b":
            opcional = "0"
        else:
            opcional = "1"
        # LISTA_RESULTADOS_PROVISORIOS = LISTA_RESULTADOS_PROVISORIOS[::-1]               #----> Arregla los b
        #my_set = {i[0] for i in lista_clave}
        #my_sum = [(j, sum(int(x[1]) for x in lista_clave if x[0] == j)) for j in my_set]
        #print(my_sum)
        contador_clave = 0
        booleano = False
        for i in lista_clave:
            if i[0] == "[b]":
                booleano = True
                continue
            if len(i) == 1:  # Cuando es 1
                LISTA_RESULTADOS_PROVISORIOS1.append(i)
                contador_clave += 1
            elif i[1] == expresion[1][1]:  # significa que tiene @  --> tambien se acaba
                if opcional == "1":
                    if booleano:
                        LISTA_RESULTADOS_PROVISORIOS1.append(i[0] + "{" + str(0) + "," + str(int(i[1]) - contador_clave) + "}")
                    else:
                        LISTA_RESULTADOS_PROVISORIOS1.append(i[0] + "{" + str(contador_clave + 1) + "," + str(int(i[1]) - contador_clave) + "}")
                else:
                    LISTA_RESULTADOS_PROVISORIOS1.append(i[0] + "{" + str(contador_clave) + "," + str(int(i[1]) - contador_clave) + "}")
            else:
                if opcional == "1":  # ---> no es b
                    if booleano:
                        LISTA_RESULTADOS_PROVISORIOS1.append(i[0] + "{0, " + str(int(i[1])) + "}")
                    else:
                        LISTA_RESULTADOS_PROVISORIOS1.append(i[0] + "{" + str(int(i[1])) + "}")
                else:
                    LISTA_RESULTADOS_PROVISORIOS1.append(
                        i[0] + "{" + str(0) + "," + str(int(i[1])) + "}")
                    contador_clave += i[1]
        for k in LISTA_RESULTADOS_PROVISORIOS1:
            if type(k) == list:
                indice = LISTA_RESULTADOS_PROVISORIOS1.index(k)
                LISTA_RESULTADOS_PROVISORIOS1[indice] = k[0]
        Final_Result = "".join(LISTA_RESULTADOS_PROVISORIOS1)
        UDID[list(UDID.keys())[counter]] = (Final_Result, UDID[list(UDID.keys())[counter]][3], UDID[list(UDID.keys())[counter]][2])
        counter += 1
        LISTA_RESULTADOS_PROVISORIOS1 = []
    return UDID


LISTA_RESULTADOS_PROVISORIOS1 = list()
LISTA_RESULTADOS_PROVISORIOS2 = list()
NOMBRE_EMPRESA = ""
UDID = dict()
UDID_COMPUESTOS = dict()
description = ""
with open("CAP/BSTN86.TXT", mode="r", encoding="UTF-8") as file:
    data = file.read().splitlines()
    for line in data:
        if line.find("Company Description") != -1:
            result = line.split(":")
            results = [j.strip() for j in result]
            NOMBRE_EMPRESA = results[2]

    for line in data:
        if line.find("UDID") != -1:
            field = line[73:80].strip()
            description = line[85:113].strip()
            result1 = line.split(" ")
            udid = [k for k in result1 if k != ""]
            nombre = udid[0] + udid[1]                                   #UDID = {key, [map, [empieza, termina], field, description]}
            UDID[nombre] = [udid[2], udid[3:5], description, field]

            linea_udid = data.index(line)
            if data[linea_udid + 1][0] == " " and data[linea_udid + 1][65] not in ["1", " "]:  # --> es compuesto
                field_compuesto = data[linea_udid + 1][73:80].strip()
                description_compuesto = data[linea_udid + 1][85:113].strip()
                result_compuestos = data[linea_udid + 1].split(" ")
                udid_compuestos = [k for k in result_compuestos if k != ""]
                UDID_COMPUESTOS[nombre] = ["?@", ["1", str(int(udid_compuestos[1]) - int(udid_compuestos[0]) + 1)], description_compuesto, field_compuesto]


print(UDID)
print(UDID_COMPUESTOS)
counter = 0
RESULTADO = dict()
dict_1 = cambio(UDID, LISTA_RESULTADOS_PROVISORIOS1)
dict_2 = cambio(UDID_COMPUESTOS, LISTA_RESULTADOS_PROVISORIOS2)
for k in dict_1.keys():
    if k in dict_2.keys():
        string_field = dict_1[k][1] + " - " + dict_2[k][1]
        string_description = dict_1[k][2] + " - " + dict_2[k][2]
        RESULTADO[k] = (dict_1[k][0] + dict_2[k][0], string_field, string_description)
    else:
        RESULTADO[k] = dict_1[k]

#print(dict_1)
#print(dict_2)
print(RESULTADO)
