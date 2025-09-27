# Proyecto Integrador Nivel 3

Este proyecto es una aplicación en **Python** para **análisis y limpieza de datos**, desarrollado como parte del integrador de nivel 3.  
El objetivo es demostrar el uso de funciones de preprocesamiento, operaciones de análisis y un flujo de trabajo con **Git Flow**.

---

## 📂 Estructura del proyecto 
```
mi_proyecto/
│
├── data/ # Archivos de datos
│ ├── productos.csv # Información de productos
│ └── ventas.csv # Información de ventas
│
├── modulo_limpieza.py # Módulo con funciones de limpieza
├── analisis.py # Script principal de análisis
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación

```

---

## ⚙️ Instalación y configuración

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tuUsuario/mi_proyecto.git
   cd mi_proyecto
---

## ▶️ Ejecución del proyecto

Ejecutar el análisis principal:

```bash
python analisis.py

---

## 🧹 Funciones implementadas

En `modulo_limpieza.py` se encuentran las funciones principales:

- **cargar_datos(ruta)** → carga archivos CSV o JSON en un DataFrame de pandas.  
- **manejar_nulos(df, metodo, valor)** → permite eliminar o rellenar valores nulos.  
- **estandarizar_texto(df, columnas)** → convierte texto a minúsculas y quita espacios.  
- **limpiar_precios(df, columna)** → elimina símbolos de moneda ($) y convierte precios a numéricos.  


---

## ❓ Preguntas de análisis

El script `analisis.py` responde las siguientes preguntas:

1. **Frecuencia** → ¿Cuál es el producto más vendido?  
2. **Agregación** → ¿Cuál es el total de unidades por categoría?  
3. **Filtrado** → ¿Cuántas ventas tienen más de 2 unidades?  

---

## 🌳 Git Flow

Este proyecto se gestionó con el flujo de ramas:

- `main` → rama principal (protegida).  
- `develop` → rama base de desarrollo.  
- `feature/*` → ramas para funcionalidades específicas.  
- Se integran cambios a través de Pull Requests.  

---
✅ Proyecto completado con éxito 🚀