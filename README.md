# Sistema Inteligente de Rutas

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema inteligente de rutas para el transporte masivo de Bogotá, utilizando el lenguaje de programación Python.

El sistema permite ingresar una estación de origen y una estación de destino, y posteriormente busca una ruta entre ambas estaciones utilizando una base de conocimiento formada por hechos y reglas lógicas.

Para realizar la búsqueda se implementa el algoritmo A*, utilizando una función heurística para estimar el costo restante hasta el destino.

## 2. Objetivo

Desarrollar un sistema basado en conocimientos que permita encontrar una ruta entre dos estaciones de transporte, aplicando conceptos de inteligencia artificial como representación del conocimiento, reglas lógicas, motor de inferencia y búsqueda heurística.

## 3. Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub
- Algoritmo de búsqueda A*
- Reglas lógicas
- Base de conocimiento

## 4. Funcionamiento del sistema

El sistema está compuesto por diferentes elementos.

### Hechos

Los hechos representan las estaciones conocidas por el sistema.

Entre ellas se encuentran:

- Portal Norte
- Toberín
- Calle 100
- Calle 72
- Calle 63
- Calle 53
- Calle 45
- Calle 26
- Portal El Dorado
- Portal Américas

### Reglas

Las reglas representan las conexiones entre las estaciones.

Por ejemplo:

- Portal Norte → Calle 100
- Portal Norte → Toberín
- Calle 100 → Calle 72
- Calle 72 → Calle 63

Estas reglas permiten al sistema determinar hacia qué estaciones puede desplazarse.

### Base de conocimiento

La base de conocimiento contiene los hechos y las reglas que utiliza el sistema para realizar la búsqueda.

### Motor de inferencia

El motor de inferencia consulta las reglas para identificar las estaciones conectadas con una estación determinada.

### Algoritmo A*

El algoritmo A* utiliza el costo real recorrido y una estimación del costo restante para seleccionar las estaciones que debe explorar.

La función utilizada es:

f(n) = g(n) + h(n)

Donde:

- g(n) representa el costo real desde el origen.
- h(n) representa la estimación del costo restante.
- f(n) representa el costo estimado total.

## 5. Ejecución

Para ejecutar el sistema se debe tener instalado Python 3.

Desde una terminal, ubicarse en la carpeta donde se encuentra el archivo y ejecutar:

python sistema_rutas.py

El programa solicitará:

Ingrese la estación de origen:
Ingrese la estación de destino:

Después de ingresar los datos, el sistema realizará la búsqueda y mostrará la ruta encontrada y su costo total.

## 6. Ejemplo de ejecución

Ejemplo:

Origen: Portal Norte
Destino: Portal Américas

Resultado:

Ruta:

1. Portal Norte
2. Calle 100
3. Calle 72
4. Calle 63
5. Calle 53
6. Calle 45
7. Calle 26
8. Portal El Dorado
9. Portal Américas

Costo total: 8
Número de estaciones: 9

El costo es 8 porque la ruta requiere ocho desplazamientos entre las nueve estaciones.

## 7. Pruebas realizadas

Se realizaron diferentes pruebas para comprobar el funcionamiento del sistema:

1. Portal Norte → Portal Américas.
2. Portal Américas → Portal Norte.
3. Portal Norte → Toberín.
4. Estación inexistente → Portal Américas.
5. Portal Norte → Portal Norte.

Estas pruebas permiten comprobar rutas normales, rutas en sentido contrario, rutas cortas, validación de estaciones inexistentes y el caso en que el origen y el destino son iguales.

## 8. Archivos del proyecto

- sistema_rutas.py: código fuente del sistema inteligente.
- README.md: documentación e instrucciones del proyecto.
- pruebas.pdf: documento con las pruebas realizadas.
- video.txt: enlace al video de presentación del proyecto.

## 9. Video de presentación

El video de presentación del proyecto se encuentra disponible en el siguiente enlace:

PENDIENTE: https://drive.google.com/drive/folders/1vFLYUfwJh18x--uSX9LBUEQbVxMJ-pbe?usp=sharing

## 10. Autores

Proyecto desarrollado como actividad académica de Inteligencia Artificial.