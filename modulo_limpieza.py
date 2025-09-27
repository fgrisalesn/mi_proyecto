import pandas as pd

def cargar_datos(ruta):
    """
    Carga un archivo CSV o JSON y lo devuelve como un DataFrame de pandas.
    """
    ext = ruta.split(".")[-1].lower()
    if ext == "csv":
        return pd.read_csv(ruta)
    elif ext == "json":
        return pd.read_json(ruta)
    else:
        raise ValueError("Formato no soportado. Usa CSV o JSON.")

def manejar_nulos(df, metodo="rellenar", valor=None):
    """
    Maneja valores nulos:
    - metodo="rellenar": reemplaza los nulos con un valor dado (ejemplo: 0).
    - metodo="eliminar": elimina filas con nulos.
    """
    df = df.copy()
    if metodo == "rellenar":
        return df.fillna(valor if valor is not None else 0)
    elif metodo == "eliminar":
        return df.dropna()
    else:
        return df

def estandarizar_texto(df, columnas):
    """
    Convierte texto a minúsculas y elimina espacios en blanco extra
    en las columnas que se indiquen.
    """
    df = df.copy()
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()
    return df

def limpiar_precios(df, columna):
    """
    Elimina símbolos de moneda ($) y convierte a números.
    Ejemplo: "$45000" -> 45000
    """
    df = df.copy()
    if columna in df.columns:
        df[columna] = df[columna].astype(str).str.replace("$", "", regex=False)
        df[columna] = pd.to_numeric(df[columna], errors="coerce")
    return df
