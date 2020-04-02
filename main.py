import re
import os

def merge(layers):
    for layer in layers:
        if re.match(r'niersc', layer.name()):
            niersc = layer
        if re.match(r's1a', layer.name()):
            s1a = layer
    return s1a, niersc

def cut():
    pass
    
def execute(path):
    layers = iface.mapCanvas().layers()
    s1a, niersc = merge(layers)
    print(s1a, niersc)
#    for layer in layers:
#        
#        if date:
#            foldername = date[-1]
#        print(layer.extent())


execute("dd")