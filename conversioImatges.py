from typing import List, Tuple, TypeVar

Pixel = TypeVar('Pixel',int, Tuple[int, int, int])
Dades = List[List[Pixel]]

def carregaImatgeColor(nom_fitxer: str) -> Dades:
    """
    Carrega una imatge amb nom 'nom_fitxer' i n'extreu les dades dels píxels.

    Arguments:
       nom_fitxer: cadena de caràcters que indica el nom del fitxer

    Retorna:
       Una llista de llistes de 3-tuples que conté les dades de la imatge.
       Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau)
    """
    llista_de_llistes=[]
    with open(nom_fitxer, mode='r') as imatge:
        for index in imatge.readlines()[3:]:
            llista_de_llistes.append(filaColorApixels(index))
        

#     carregaImatgeColor('Imatges Prova\Fabio\Fabio_ascii_arreglada.ppm')
    return llista_de_llistes

def prova(nom_fitxer):
    with open(nom_fitxer, mode='r') as imatge:
        a = imatge.readlines()
        print(a[:3])
    
def filaAEnters(fila: str) -> List[int]:
    """
    Converteix una cadena de caràcters composta per nombres separats per espais
    en una llista d'enters.

    Arguments:
        fila: cadena de caràcters composta per nombres separats per espais. Pot o no acabar amb un caràcter de línia nova.

    Retorna:
       Una llista d'enters
    """
    a=[]
    fila=fila.split()
    for num in fila:
        a.append(int(num))
    return a
# filaAEnters('1 23 34 14 5 6') 
def filaColorApixels(fila: str) -> List[Pixel]:
    """
    Converteix una cadena de caràcters composta per nombres separats per espais
    en una llista de píxels representats per 3-tuples.1 

    Arguments:
        fila: cadena de caràcters composta per nombres separats per espais. Pot o no acabar amb un caràcter de línia nova.

    Retorna:
       Una llista de 3-tuples.
       Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau)
    """
    llista=[]
    tupla=''
    a=[]
    llista_files=filaAEnters(fila)
    for index in llista_files:
        a.append(index)
        if len(a) == 3:
            tupla=(a[0],a[1],a[2])
            llista.append(tupla)
            a=[]
    return llista

def separaCanals(dades: Dades) -> Tuple[Dades, Dades, Dades]:
    """
    Separa les intensitats dels tres canals de color de la imatge.

    Arguments:
        dades: Una llista de llistes de píxels representats per 3-tuples.
               Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau).

    Retorna:
        Una 3-tupla que conté tres llistes de llistes de píxels.
        Corresponen respectivament als canals vermell, verd i blau respectivament.
    """
    vermell=[]
    verd=[]
    blau=[]

    for fila in dades:
        v=[]
        ve=[]
        b=[]
        for tupla in fila:
            v.append(tupla[0])
            ve.append(tupla[1])
            b.append(tupla[2])
        vermell.append(v)
        verd.append(ve)
        blau.append(b)
    tupla_colors=(vermell,verd,blau)
    return tupla_colors
# separaCanals([[(146, 163, 171), (134, 151, 159), (119, 136, 144), (106, 123, 131), (100, 117, 125), (96, 113, 121), (92, 109, 117)]])
def converteixAGrisos(dades: Dades) -> Dades:
    """
    Converteix les dades d'una imatge a escala de grisos tenint en compte la sentibilitat de l'ull a cadascun dels colors.
    El valor d'intensitat del blanc es fa a partir d'un 30% del vermell, un 59% del verd i un 11% del blau.

    Arguments:
        dades: Una llista de llistes de píxels representats per 3-tuples.
               Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau).

    Retorna:
        Una llista de llistes d'enters que representen la intensitat del blanc per cadascun dels píxels en una imatge amb escala de grisos.
    """
    llista_de_llistes=[]
    llista=[]
    for fila in dades:
        for tupla in fila:
            llista.append(int(tupla[0]*(30/100)+tupla[1]*(59/100)+tupla[2]*(11/100)))
        llista_de_llistes.append(llista)
    return llista_de_llistes
# converteixAGrisos([[(146, 163, 171), (134, 151, 159), (119, 136, 144), (106, 123, 131), (100, 117, 125), (96, 113, 121), (92, 109, 117)]])    
def valorMàxim(dades: Dades) -> int:
    """
    Calcula el valor màxim de totes les intensitats que apareixen en una imatge en color o escala de grisos.

    Arguments:
        dades: Una llista de llistes de píxels representats per o bé enters representant intensitats de blanc en escala de grisos o bé 3-tuples.
               Cada tupla conté la intensitat dels diferents canals de color de la següent manera: (vermell, verd, blau).

    Retorna:
        Un enter amb el valor màxim que conté un píxel de la imatge per a qualsevol canal.
    """
    
    if type(dades[0][0]) == tuple:
        num_max=dades[0][0][0]
        for fila in dades:
            for tupla in fila:
                for num in tupla:
                    if num > num_max:
                        num_max = num
    else:
        num_max=dades[0][0]
        for fila in dades:
            for num in fila:
                if num > num_max:
                    num_max = num
    return num_max

def dimensions(dades: Dades) -> (int, int):
    """
    Calcula les dimensions d'una imatge a partir de la llista de llistes de píxels.
    Assumeix una imatge ben formada amb totes les files de la mateixa longitud.

    Arguments:
        dades: Una llista de llistes de píxels representats o bé per enters o bé per 3-tuples.

    Retorna:
        Una 2-tupla amb les dimensions de la imatge de la següent manera (amplada, alçada).
    """

def detectaTipus(dades: Dades) -> (str, str):
    """
    Detecta el tipus d'imatge contingut a les dades.
    Identifica el tipus d'imatge de la següent manera:
       - Si els píxels estan fets de tuples és en color.
       - Si els píxels són enters i el seu valor màxim no supera l'1 són en blanc i negre.
       - Si els píxels són enters i el seu valor màxim supera l'1 són en color.

    Arguments:
        dades: llista de llistes de píxels representats o bé per enters o bé per 3-tuples.

    Retorna:
        Una 2-tupla de cadenes de caràcters amb la informació de la capçalera ('P1', 'P2', 'P3' segons sigui una imatge en Blanc i negre, en escala de grisos o en color) en el primer element i l'extensió ('ppm', 'pbm', 'pgm' respectivament) en el segon.
    """
    if type(dades[0][0]) == tuple:
        a = ('P3', )
    elif 
    
def escriuImatge(dades: Dades, nom: str):
    """
    Escriu les dades d'una imatge en un fitxer. Identifica automàticament el tipus d'imatge i l'extensió que cal fer servir.
    En cas que el valor màxim de la imatge estigui entre 2 i 255 (inclosos) definirà el valor màxim de la imatge com a 255. En cas que sigui major, deixarà el major valor com a valor màxim.

    Arguments:
        dades: Llista de llistes de píxels representats o bé per enters o bé per 3-tuples.
        nom: Cadena de caràcters que representa el nom del fitxer a escriure sense extensió.
    """
