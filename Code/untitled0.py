# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:54:26 2019

@author: Mario Abel García
"""

from ftplib import FTP
import pandas as pd
import numpy as np
#%% Inventario de CT conexion via FTP

ftp = FTP('216.70.82.104')
ftp.login(user='GDL2536', passwd = 'gdl2536')

#ftp.cwd('/whyfix/')
