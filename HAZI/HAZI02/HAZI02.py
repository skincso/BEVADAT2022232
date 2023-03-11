# %%
import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%
# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

def column_swap(a : np.array) -> np.array:

    a[:, [0, 1]] = a[:,[1 ,0]]
    return a


#a = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(column_swap(a))

# %%
# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

def compare_two_array(a : np.array, b : np.array) -> np.array:
    arr = a == b
    ret = np.asarray(np.where(arr == True))
    return ret.ravel()


#a = np.array([7,8,9])
#b = np.array([9,8,7])
#print(compare_two_array(a, b))

# %%
# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!

def get_array_shape(a : np.array) -> str:
    shape = np.shape(a)
    if len(shape) > 2:
        return "sor: %(sor)i, oszlop: %(oszlop)i, melyseg: %(melyseg)i" % {'sor': shape[0], 'oszlop': shape[1], 'melyseg': shape[2]}
    elif len(shape) > 1:
        return "sor: %(sor)i, oszlop: %(oszlop)i, melyseg: %(melyseg)i" % {'sor': shape[0], 'oszlop': shape[1], 'melyseg': 1}    
    else:
        return "sor: %(sor)i, oszlop: %(oszlop)i, melyseg: %(melyseg)i" % {'sor': shape[0], 'oszlop': 1, 'melyseg': 1}


#c = np.zeros((2, 3, 10))
#print(get_array_shape(c))

# %%
# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek.
# Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

def encode_Y(a : np.array, classes: int) -> np.array:
    arr = np.zeros((classes, a.shape[0]), dtype=int)

    idcs = np.arange(classes)

    arr[idcs, a] = 1

    return arr


#a = np.array([1, 0, 0, 2])
#print(encode_Y(a, 4))

# %%
# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

def decode_Y(arr : np.array) -> np.array:
    a = np.argwhere(arr == 1)
    return a[:,1]


#arr = np.array([[0,1,0,0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
#print(decode_Y(arr))    

# %%
# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t
# és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()

def eval_classification(l : list, a: np.array):
    x = np.argmax(a)
    return l[x]


#l = ['alma', 'körte', 'szilva']
#a = np.array([0.2, 0.2, 0.6])
#print(eval_classification(l, a))

# %%
# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()

def replace_odd_numbers(a : np.array) -> np.array:
    a[a % 2 == 1] = -1
    return a


#a = np.array([1,2,3,11,5,6,1,1])
#print(replace_odd_numbers(a))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy 
# az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

def replace_by_value(a : np.array, value: int) -> np.array:
    return np.where(a < value, -1, 1)


#a = np.array([1, 2, 5, 0])
#print(replace_by_value(a, 2))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

def array_multi(a : np.array) -> np.array:
    return np.prod(a)


#a = np.array([[1,0,1,1,1],[2, 2, 2, 2, 2]])
#print(array_multi(a))

# %%
# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, 
# aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

def array_multi_2d(a : np.array) -> np.array:
    arr = np.zeros(a.shape[0])
    ind = np.arange(a.shape[0])

    arr[ind] = np.prod(a[ind], axis = 1)

    return arr


#a = np.array([[1, 2, 2], [3, 4, 2], [1, 1, 2]])
#print(array_multi_2d(a))

# %%
# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()

def add_border(a : np.array) -> np.array:
    arr = np.zeros((a.shape[0] + 2, a.shape[1] + 2))

    arr[1:-1,1:-1] = a[:]

    return arr


#a = np.array([[1,2],[3,4],[5,6]])
#print(add_border(a))

# %%
# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!

# %%
# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. A fgv két str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

def list_days(start: str, end: str) -> np.array:
    return np.arange(start, end, dtype='datetime64[D]')


#start = '2002-02'
#end = '2002-03'
#print(list_days(start, end))

# %%
# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24

def get_act_date() -> np.datetime64:
    return np.datetime64('today')


#print(get_act_date())

# %%
# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()

# time stemp mikortól

def sec_from_1970() -> int:
    d0 = np.datetime64('1970')
    d1 = np.datetime64('now')
    return int((d1 - d0) / np.timedelta64(1, "s"))


#print(sec_from_1970())


