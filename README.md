# Librería de Computación Cuántica

Este proyecto proporciona una librería para realizar operaciones con números complejos utilizando Python. Está diseñada para simplificar el manejo y la manipulación de números complejos en el contexto de la computación cuántica.

## Requisitos

Para utilizar esta librería, necesitas:

- **Python**: Un intérprete de Python 3.8 o superior. Puedes descargarlo desde [python.org](https://www.python.org/).
- **Editor de Código o IDE**: Aunque el proyecto se desarrolló con Visual Studio, puedes usar cualquier editor o IDE que soporte Python, como PyCharm, VS Code, o Atom.



## Instalación y Uso

### Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/repo.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd repo
    ```

3. Instala las dependencias necesarias (si hay un archivo `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```

### Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

- **`Operaciones`**: Contiene los módulos para realizar diversas operaciones con números complejos.
  - **`SumC`**: Módulo para sumar números complejos.
  - **`ProductoC`**: Módulo para multiplicar números complejos.
  - Otros módulos pueden estar presentes para operaciones adicionales.

- **`Pruebas`**: Contiene los scripts de prueba que verifican la funcionalidad de los módulos en la carpeta `Operaciones`.

### Ejemplo de Uso

A continuación se muestra un ejemplo básico de cómo usar los módulos de la librería:

```python
from operaciones.SumC import sumar
from operaciones.ProductoC import multiplicar

# Sumar números complejos
resultado_suma = sumar([1, 2], [3, 4])
print("Resultado de la suma:", resultado_suma)

# Multiplicar números complejos
resultado_producto = multiplicar([1, 2], [3, 4])
print("Resultado del producto:", resultado_producto)

## Construido Con

- **Python**: El lenguaje de programación principal utilizado para implementar la lógica de la librería.
- **Visual Studio**: Entorno de desarrollo integrado utilizado para el desarrollo del proyecto. También se puede utilizar cualquier otro editor de código compatible con Python.

## Autor

- **Jacobo Díaz Alvarado**: Desarrollador principal del proyecto.

