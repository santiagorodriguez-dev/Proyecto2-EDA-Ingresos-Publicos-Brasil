
"""
Este módulo proporciona funciones para la transformación y limpieza de datos en un DataFrame de pandas.

Incluye las siguientes funciones:
- l_cambio_nombre_columnas(df): renombra las columnas del DataFrame según un diccionario de mapeo predefinido.
- l_limpieza_de_datos(df): realiza varias tareas de limpieza en el DataFrame, como conversión de tipos de datos y eliminación de espacios en blanco.
- l_rellenado_faltante(df, col1, col2, opcion): rellena los valores faltantes en una columna utilizando los valores de otra columna.
- l_limpieza_de_datos_final(df): finaliza la limpieza del DataFrame, llenando valores faltantes y ajustando tipos de datos.
"""

# ini imports
import pandas as pd # type: ignore

pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# fin imports

#cambiamos nombre de las columnas
def l_cambio_nombre_columnas(df: pd.DataFrame):
    
    cambio_columas = {df.columns[0]: 'CODIGO_ORGANIZACION_SUPERIOR', 
                    df.columns[1]: 'NOMBRE_ORGANIZACION_SUPERIOR',
                    df.columns[2]: 'CODIGO_DE_ORGANO',
                    df.columns[3]: 'NOMBRE_DEL_ORGANO',
                    df.columns[4]: 'CODIGO_DE_UNIDAD_GESTORA',
                    df.columns[5]: 'NOMBRE_UNIDAD_GESTORA',
                    df.columns[6]: 'CATEGORIA_ECONOMICA',
                    df.columns[7]: 'ORIGEN_INGRESO',
                    df.columns[8]: 'TIPO_INGRESO',
                    df.columns[9]: 'DEPARTAMENTO',
                    df.columns[10]: 'VALOR_PREVISTO_ACTUALIZADO',
                    df.columns[11]: 'VALOR_LANZADO',
                    df.columns[12]: 'VALOR_REALIZADO',
                    df.columns[13]: 'PORCENTAJE_REALIZADO',
                    df.columns[14]: 'FECHA_LANZAMIENTO',
                    df.columns[15]: 'ANIO_EJERCICIO'}

    df = df.rename(columns=cambio_columas)

    return df

#limpiamos datos
def l_limpieza_de_datos(df: pd.DataFrame):
    
    #ANIO_EJERCICIO
    df[df.columns[15]] = df[df.columns[15]].fillna(0)
    df[df.columns[15]] = df[df.columns[15]].astype(int);

    #VALOR_PREVISTO_ACTUALIZADO
    df[df.columns[10]] = df[df.columns[10]].str.replace(',', '.')
    df[df.columns[10]] = df[df.columns[10]].astype(float);

    #VALOR_LANZADO
    df[df.columns[11]] = df[df.columns[11]].str.replace(',', '.')
    df[df.columns[11]] = df[df.columns[11]].astype(float);

    #VALOR_REALIZADO
    df[df.columns[12]] = df[df.columns[12]].str.replace(',', '.')
    df[df.columns[12]] = df[df.columns[12]].astype(float); 

    #PORCENTAJE_REALIZADO
    df[df.columns[13]] = df[df.columns[13]].str.replace(',', '.')
    df[df.columns[13]] = df[df.columns[13]].astype(float); 

    #FECHA_LANZAMIENTO
    df[df.columns[14]] = df[df.columns[14]].str.strip()
    df[df.columns[14]] = pd.to_datetime(df[df.columns[14]],format="%d/%m/%Y")

    #NOMBRE_DEL_ORGANO
    df[df.columns[3]] = df[df.columns[3]].str.strip().str.capitalize()

    #NOMBRE_DEL_ORGANO
    df[df.columns[3]] = df[df.columns[3]].str.strip().str.capitalize()

    #NOMBRE_ORGANIZACION_SUPERIOR
    df[df.columns[1]] = df[df.columns[1]].str.strip().str.capitalize()

    #NOMBRE_UNIDAD_GESTORA
    df[df.columns[5]] = df[df.columns[5]].str.strip().str.capitalize()

    #DEPARTAMENTO
    df[df.columns[9]] = df[df.columns[9]].str.strip().str.capitalize()

    #TIPO_INGRESO
    df[df.columns[8]] = df[df.columns[8]].str.strip().str.capitalize()

    #ORIGEN_INGRESO
    df[df.columns[7]] = df[df.columns[7]].str.strip().str.capitalize()

    #CATEGORIA_ECONOMICA
    df[df.columns[6]] = df[df.columns[6]].str.strip().str.capitalize()

    return df

# rellenamos los datos que faltan de las columnas
def l_rellenado_faltante(df: pd.DataFrame, col1, col2, opcion):

    df_columnas = df[[col1,col2]]

    if opcion == True:
        df_columnas_filtrado = df_columnas[df_columnas[col1] != 0]
    else:
        df_columnas_filtrado = df_columnas[df_columnas[col2] != 0]

    df_columnas_filtrado_limpio = df_columnas_filtrado.drop_duplicates().dropna()

    diccionario_clave_valor = df_columnas_filtrado_limpio.set_index(col1)[col2].to_dict()

    df[col2] = df[col2].fillna(df[col1].map(diccionario_clave_valor))

    return df

#limpiamos datos
def l_limpieza_de_datos_final(df: pd.DataFrame):
    
    #CODIGO_ORGANIZACION_SUPERIOR
    df[df.columns[0]] = df[df.columns[0]].fillna(0)
    df[df.columns[0]] = df[df.columns[0]].astype(int);

    #CODIGO_DE_ORGANO
    df[df.columns[2]] = df[df.columns[2]].fillna(0)
    df[df.columns[2]] = df[df.columns[2]].astype(int);

    #CODIGO_DE_UNIDAD_GESTORA
    df[df.columns[4]] = df[df.columns[4]].fillna(0)
    df[df.columns[4]] = df[df.columns[4]].astype(int);

    #CATEGORIA_ECONOMICA
    df[df.columns[6]] = df[df.columns[6]].fillna('Sem informação')

    #ORIGEN_INGRESO
    df[df.columns[7]] = df[df.columns[7]].fillna('Sem informação')

    #eliminamos duplicados
    df = df.drop_duplicates()

    return df





