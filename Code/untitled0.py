# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:54:26 2019

@author: Mario Abel García
"""

from ftplib import FTP
import pandas as pd
import xml.etree.cElementTree as et
import numpy as np

#%% Inventario de CT conexion via FTP

ftp = FTP('216.70.82.104')
ftp.login(user='GDL2536', passwd = 'gdl2536')
print('login success :)')
print(ftp.pwd())

ftp.cwd('catalogo_xml')
ftp.dir()

download = 'productos.xml'


ftp.retrbinary('RETR ' + download, open(download, 'wb').write)
print('archivo descargado')
ftp.quit()
print('goodbye FTP')
#%% Transformar XML a XLSX https://stackoverflow.com/questions/43007874/how-to-import-an-xml-file-into-an-excel-xls-file-template-using-python

def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None

parsed_xml = et.parse("productos.xml")
dfcols = ['name','clave']
df_xml = pd.DataFrame(columns=dfcols)
 
for node in parsed_xml.getroot():
    name = node.attrib.get('no_parte')
    clave = node.find('clave')
 
    df_xml = df_xml.append(pd.Series([name, getvalueofnode(clave)], index=dfcols),ignore_index=True)