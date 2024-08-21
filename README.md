# Librería de Computación Cuántica

Este proyecto proporciona una librería para realizar operaciones con números complejos utilizando Python. Está diseñada para simplificar el manejo y la manipulación de números complejos en el contexto de la computación cuántica.

## Requisitos

Para utilizar esta librería, necesitas:

- **Python**: Un intérprete de Python 3.8 o superior. Puedes descargarlo desde [python.org](https://www.python.org/).
- **Editor de Código o IDE**: Aunque el proyecto se desarrolló con Visual Studio, puedes usar cualquier editor o IDE que soporte Python, como PyCharm, VS Code, o Atom.



## Instalación y Uso

### Instalación

1. Clona uno de los repositorios disponibles:
    ```bash
    git clone https://github.com/usuario/repo.git
    ```

2. Copia el módulo de operaciones que necesites en tu proyecto. 



### Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

- **Operaciones**: Contiene los módulos para realizar diversas operaciones con números complejos.
  - **SumC**: Módulo para sumar números complejos.
  - **ProductoC**: Módulo para multiplicar números complejos.
  - Otros módulos pueden estar presentes para operaciones adicionales.

- **Pruebas**: Contiene los scripts de prueba que verifican la funcionalidad de los módulos en la carpeta Operaciones.

### Ejemplo de Uso

    Aquí se muestra un ejemplo básico de cómo usar el módulo para calcular la fase de un número complejo:
    En este ejemplo, la función fase toma una lista que representa un número complejo, donde la posición [0] es la parte real y [1] es la parte imaginaria. La salida de fase([1, 1]) es la fase del número complejo 1 + i.
    
    ```python
    import math

    def fase(a):
        
        teta = math.atan2(a[1],a[0])
        
        return teta
        
    if __name__ == "__main__":
        
        print(fase([1,1]))
            
    




## Construido con:

- **Python**: El lenguaje de programación principal utilizado para implementar la lógica de la librería.
- **Visual Studio**: Entorno de desarrollo integrado utilizado para el desarrollo del proyecto. También se puede utilizar cualquier otro editor de código compatible con Python.

## Autor

- **Jacobo Díaz Alvarado**: Desarrollador principal del proyecto.

