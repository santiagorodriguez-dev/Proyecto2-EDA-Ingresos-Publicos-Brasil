""""""

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
                    df.columns[8]: 'TPO_INGRESO',
                    df.columns[9]: 'DEPARTAMENTO',
                    df.columns[10]: 'VALOR_PREVISTO_ACTUALIZADO',
                    df.columns[11]: 'VALOR_LANZADO',
                    df.columns[12]: 'VALOR_REALIZADO',
                    df.columns[13]: 'PORCENTAJE_REALIZADO',
                    df.columns[14]: 'FECHA_LANZAMIENTO',
                    df.columns[15]: 'ANIO_EJERCICIO'}

    df = df.rename(columns=cambio_columas)

    return df

#cambiamos nombre de las columnas
def l_limpieza_de_datos(df: pd.DataFrame):
    
    #CODIGO_ORGANIZACION_SUPERIOR
    df[df.columns[0]] = df[df.columns[0]].fillna(0)
    df[df.columns[0]] = df[df.columns[0]].astype(int);

    #CODIGO_DE_ORGANO
    df[df.columns[2]] = df[df.columns[2]].fillna(0)
    df[df.columns[2]] = df[df.columns[2]].astype(int);

    #CODIGO_DE_UNIDAD_GESTORA
    df[df.columns[4]] = df[df.columns[4]].fillna(0)
    df[df.columns[4]] = df[df.columns[4]].astype(int);

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

    #FECHA_LANZAMIENTO
    df[df.columns[14]] = df[df.columns[14]].str.strip()
    df[df.columns[14]] = pd.to_datetime(df[df.columns[14]])

    return df

def rellenado_faltante(df: pd.DataFrame):
    df_columnas = df[['CODIGO_ORGANIZACION_SUPERIOR','NOMBRE_ORGANIZACION_SUPERIOR']]

    df_columnas_filtrado = df_columnas[df_columnas['CODIGO_ORGANIZACION_SUPERIOR'] != 0]

    df_columnas_filtrado_limpio = df_columnas_filtrado.drop_duplicates().dropna()
    
    diccionario_clave_valor = df_columnas_filtrado_limpio.set_index('CODIGO_ORGANIZACION_SUPERIOR')['NOMBRE_ORGANIZACION_SUPERIOR'].to_dict()

    df['NOMBRE_ORGANIZACION_SUPERIOR'] = df['NOMBRE_ORGANIZACION_SUPERIOR'].fillna(df['CODIGO_ORGANIZACION_SUPERIOR'].map(diccionario_clave_valor))

    return df





