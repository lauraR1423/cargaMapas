import sys
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import chaininghashtable as ch

import dsv as dsv


def load_data():
    mapa=mp.newMap(numelements=17,maptype='CHAINING',loadfactor=0.5, cmpfunction=None)
    mapsfile=cf.data_dir + "2023.dsv"
    input_file= dsv.read(open(mapsfile, encoding='utf-8'))

    


load_data()