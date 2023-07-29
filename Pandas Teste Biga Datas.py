# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:27:17 2023

@author: fmour
"""

import pandas as pd

df = pd.read_excel(r"C:\Users\fmour\Documents\MEGAsync Downloads\Documentos\Mestrado\Python\Base de dados\Kaggle\50Hertz.xlsx")

pd.set_option('display.max_columns', 8)

print(df)