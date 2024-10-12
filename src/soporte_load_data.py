""""""

# ini imports
import pandas as pd # type: ignore
import os

pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# fin imports

# constantes
path_ficheros = '../datos/'
path_ficheros_salida = '../datos/output/'

#cargamos los datos de los ficheros y devolvemos un array de todos los dataframe cargados
def load_all_data():
    df_array = []
    list_ficheros_clean = []

    list_ficheros = os.listdir("../datos")

    for filtrado in list_ficheros:
        if ".csv" in filtrado:
            list_ficheros_clean.append(filtrado)

    for fichero in list_ficheros_clean:
        df_array.append(pd.read_csv(path_ficheros + fichero, sep = ';'))

    return df_array

def union_all_data(df_array):

    return  pd.concat(df_array, axis=0, ignore_index = True)

def save_to_file(df_all_data_union, nombre):

    if not os.path.exists(path_ficheros_salida):
        os.mkdir(path_ficheros_salida)

    df_all_data_union.to_csv(path_ficheros_salida + nombre)



