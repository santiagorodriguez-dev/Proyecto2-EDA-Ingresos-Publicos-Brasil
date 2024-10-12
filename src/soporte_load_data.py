"""
Este módulo proporciona funciones para cargar, combinar y guardar datos en formato CSV.

Incluye las siguientes funciones:
- load_all_data(): carga todos los archivos CSV desde un directorio específico y los devuelve como una lista de DataFrames.
- union_all_data(df_array): combina una lista de DataFrames en un solo DataFrame.
- save_to_file(df_all_data_union, nombre): guarda un DataFrame combinado en un archivo CSV.
- check_columns_equal(df_array): verifica si todos los DataFrames tienen las mismas columnas.
"""

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
    try:
        df_array = []
        list_ficheros_clean = []

        list_ficheros = os.listdir("../datos")

        for filtrado in list_ficheros:
            if ".csv" in filtrado:
                list_ficheros_clean.append(filtrado)

        for fichero in list_ficheros_clean:
            try:
                df_array.append(pd.read_csv(path_ficheros + fichero, sep = ';'))
            except:
                print(f"Error al cargar el fichero {path_ficheros + fichero} en la funcion load_all_data")        

        return df_array
    except:
        print("Error en la funcion load_all_data")
        return df_array

# hacemos la union de todos los dataframe, se le pasa la lista y el concat lo hace
def union_all_data(df_array):
    try:
        return  pd.concat(df_array, axis=0, ignore_index = True)
    except:
        print("Error en la funcion union_all_data")

# guardamos el dataframe con todos los datos a un fichero
def save_to_file(df_all_data_union, nombre):
    try:
        if not os.path.exists(path_ficheros_salida):
            os.mkdir(path_ficheros_salida)

        df_all_data_union.to_csv(path_ficheros_salida + nombre, sep = ';')
    except:
        print("Error en la funcion save_to_file")

# verificamos que todos los ficheros tienen exactamente las mismas columnas
def check_columns_equal(df_array):
    try:
        for df_elment in df_array:

            list_columnas = pd.DataFrame(df_elment).columns

            for df_elment_inside in df_array:
                list_columnas_inside = pd.DataFrame(df_elment_inside).columns

                if set(list_columnas) != set(list_columnas_inside):
                    return False

        return True 
    except:
        print("Error en la funcion check_columns_equal")      







