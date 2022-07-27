from abc import ABC
import pyodbc

constring="Driver={SQL Server};Server=DESKTOP-9FVJH8C\SQLEXPRESS;Database=railway_db;Trusted_Connection=yes;"

connection=pyodbc.connect(constring)

#class train(ABC):


#class TVM_ALP(train):

#class TVM_ERN(train):

#class TVM_KZK(train):

