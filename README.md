# Librería de Computación Cuántica

Este proyecto proporciona una librería para realizar operaciones con números complejos utilizando Python. Está diseñada para simplificar el manejo y la manipulación de números complejos en el contexto de la computación cuántica.

## Requisitos

Para utilizar esta librería, necesitas:

- **Python**: Un intérprete de Python 3.8 o superior. Puedes descargarlo desde [python.org](https://www.python.org/).
- **Editor de Código o IDE**: Aunque el proyecto se desarrolló con Visual Studio, puedes usar cualquier editor o IDE que soporte Python, como PyCharm, VS Code, o Atom.



## Instalación y Uso

### Instalación

1. Clona uno de los repositorios.

2. Copia una de las operaciones en un editor de Python.



### Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

- **`Operaciones`**: Contiene los módulos para realizar diversas operaciones con números complejos.
  - **`SumC`**: Módulo para sumar números complejos.
  - **`ProductoC`**: Módulo para multiplicar números complejos.
  - Otros módulos pueden estar presentes para operaciones adicionales.

- **`Pruebas`**: Contiene los scripts de prueba que verifican la funcionalidad de los módulos en la carpeta `Operaciones`.

### Ejemplo de Uso

    En el caso de querer usar "Fase de un número complejo".
    Para obtener la fase de un número complejo con el programa desarrollado, se debe modificar la lista dentro del print dentro de la función main. La posición [0] de esta lista representa la parte real, mientras que [1] representa la parte imaginaría. 
    En esta ocasión quiero la fase del número c = 1 + i, es decir, escribo la tupla [1,1] en la función main.
    
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

