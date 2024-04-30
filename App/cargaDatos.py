import sys
import config as cf
import dsv as dsv
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import chaininghashtable as ch



def load_data():
    mapa=mp.newMap(numelements=17,maptype='CHAINING',loadfactor=0.5, cmpfunction=None)
    
    mapsfile=cf.data_dir + "2023.dsv"

    input_file= dsv.read(mapsfile)
    
    for fila in input_file:
        tipo=fila[11]
        trafico=fila[9]
        if tipo=="Aviaciòn comercial Regular" and trafico=="I":
            destino=fila[7]
            existdestino = mp.contains(mapa, destino)
            if (existdestino):
                entry = mp.get(mapa, destino)
                ref = me.getValue(entry)
            else:
                ref =lt.newList()
                mp.put(mapa,destino, ref)
        
            lt.addLast(ref, fila)
            
    return mapa

def filtrar_destinos(mapa):
    destinos=mp.keySet(mapa) 
    lista=[]
    
    for destino in lt.iterator(destinos):
        lista.append(destino)

    return lista


mapa=load_data()

destinos=filtrar_destinos(mapa)
