#variables
def variables():
    edad, _peso = 50, 70.5
    nombres = 'Daniel Vera'
    dirDomiciliaria= "Chile y Guayaquil"
    Tipo_sexo = 'M'
    civil = True
    usuario = ('dchiki','1234','chiki@gmail.com')
    materias = ['Programacion Web','PHP','POO']
    docente = {'nombre':'Daniel','edad':50,'fac':'faci'}
    print("""Mi nombre es {}, tengo {}
            años""".format(nombres,edad))
    print(usuario,materias,docente)

#variables()
def uso_if():
    x=(input("Ingresa un numero entero: "))
    if x < 0:
      x = 0
      print('Negativo cambiado a cero')
    elif x == 0:
      print('Cero')
    elif x == 1:
      print('Uno')
    else:
      print('Ninguna opcion')
    print("Ok") if type(x) == int else print("String")
#uso_if()

def uso_while():
    vocal = input("Ingrese vocal:")
    while vocal not in('a','e','i','o','u'):
        if vocal == '.':
            break
        vocal = input("Ingrese vocal:")
    print('Su vocal o punto es:{}'.format(vocal))
#uso_while()
def uso_for():
    frase = input("Ingrese frase: ")
    for indice in range(len(frase)-1,-1,-1):
        print(indice,'=',frase[indice])
    
    cvoc=0
    for car in frase:
        if car in ("a","e","i","o","u","A","E","I","O","U"):
            if car in ["A","E","I","O","U"]:
                continue
            else:
                cvoc=cvoc+1
    print('cantidad vocales:{}'.format(cvoc))
    [print(car) for car in['a','e','i','o','u'] if car not in('a','i','o')]

#uso_for()
'''Funciones sin retorno'''
def vocales(frase):
     for car in frase:
         if car in('a','e','i','o','u'):
            print(car)
'''oracion = input('Ingrese oracion:')
vocales(oracion.lower())'''

def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
#print('Promedio: {} = {}'.format(listanotas, prom))

def uso_math():
    import math
    num1, num2, num, men = 12.572,  15.4,  4,  '1234'
    print(math.ceil(num1), '\t',math.floor(num1))
    print(round(num1,1),'\t',type(num),'\t',type(men))
#uso_math()
def uso_cadenas():
    mensaje = 'Hola ' + 'mundo ' + 'Python'
    men1=mensaje.split()
    men2=';'.join(men1)
    print(mensaje[0],mensaje[0:4],men1,men2)
    print(mensaje.find("mundo"), mensaje.lower())
#uso_cadenas()
def uso_fecha():
    from datetime import datetime,timedelta,date
    hoy, fdia = datetime.now(), date.today()
    futuro = hoy + timedelta(days=30)
    dif, aa, mm, dd = futuro - hoy, hoy.year, hoy.month, hoy.day
    fecha = date(aa, mm, dd+2)
    print(hoy, fdia, futuro)
#uso_fecha()

def colecciones():
    usuario = ('dchiki','1234','chiki@gmail.com')
    materias = ['Python','PHP','POO','Go']
    docente = {'nombre':'Daniel','edad':50,'fac':'faci'}
    print(usuario[0],materias[1],docente['nombre'])
    print(usuario[0:2],docente.keys(),docente.values())
    materias.append('Programacion Movil')
    docente['sexo'], docente['edad']='M', 51
    print(materias,docente)
    tupla,lista,diccionario=(),[],{}
    for valor in usuario: print(valor)
    for i, c in enumerate(materias): print(i,':',c)
    for c, v in docente.items(): print(c,':',v)
#colecciones()
''' manejo de archivos'''
archivo, f = 'datos.txt', ""
docentes = [{'nombre':'Daniel','edad':50,'fac':'Ingenieria'},
    {'nombre':'Juan','edad':30,'fac':'Salud'},
    {'nombre':'Yady','edad':40,'fac':'Administrativa'} ]

def escribir_archivo(arch,modo):
  with open(arch, modo) as writer:
    for i in range(len(docentes)):
        linea=''
        for clave, valor in docentes[i].items():
            if clave == 'fac':
                linea = linea + (str(valor) if type(valor) == int else valor) + '\n'
            else:
                linea = linea + (str(valor) if type(valor) == int else valor) + ';'
        writer.writelines(linea)
escribir_archivo(archivo,'w')

def leer_archivo(arch):
    f=""
    try:
        f = open(arch, "r")
        for linea in f: print(linea)
    except Exception as e:
        print('Error de archivo: ' + str(e))
    finally:  
        f.close()
leer_archivo(archivo)
















