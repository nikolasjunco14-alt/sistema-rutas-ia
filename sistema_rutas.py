# ============================================================
# SISTEMA INTELIGENTE DE RUTAS
# Transporte Masivo de Bogotá
# ============================================================

import unicodedata


# ============================================================
# 1. HECHOS
# ============================================================
# Los hechos representan las estaciones conocidas
# por nuestro sistema.

estaciones = [
    "Portal Norte",
    "Toberín",
    "Calle 100",
    "Calle 72",
    "Calle 63",
    "Calle 53",
    "Calle 45",
    "Calle 26",
    "Portal El Dorado",
    "Portal Américas"
]


# ============================================================
# 2. REGLAS LÓGICAS
# ============================================================
# Las reglas representan las conexiones entre estaciones.
#
# Regla:
# Si una estación está conectada con otra estación,
# entonces es posible desplazarse entre ellas.

reglas = [
    ("Portal Norte", "Calle 100"),
    ("Portal Norte", "Toberín"),

    ("Toberín", "Portal Norte"),
    ("Toberín", "Calle 100"),

    ("Calle 100", "Portal Norte"),
    ("Calle 100", "Calle 72"),

    ("Calle 72", "Calle 100"),
    ("Calle 72", "Calle 63"),

    ("Calle 63", "Calle 72"),
    ("Calle 63", "Calle 53"),

    ("Calle 53", "Calle 63"),
    ("Calle 53", "Calle 45"),

    ("Calle 45", "Calle 53"),
    ("Calle 45", "Calle 26"),

    ("Calle 26", "Calle 45"),
    ("Calle 26", "Portal El Dorado"),

    ("Portal El Dorado", "Calle 26"),
    ("Portal El Dorado", "Portal Américas"),

    ("Portal Américas", "Portal El Dorado")
]


# ============================================================
# 3. BASE DE CONOCIMIENTO
# ============================================================
# La base de conocimiento contiene los hechos y las reglas.

base_conocimiento = {
    "estaciones": estaciones,
    "reglas": reglas
}


# ============================================================
# 4. FUNCIÓN PARA NORMALIZAR TEXTO
# ============================================================
# Permite aceptar mayúsculas, minúsculas y palabras
# con o sin tildes.

def normalizar_texto(texto):

    texto = texto.strip().lower()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    return texto


# ============================================================
# 5. MOTOR DE INFERENCIA
# ============================================================
# Utiliza las reglas de la base de conocimiento para
# determinar qué estaciones están conectadas.

def obtener_vecinos(estacion):

    vecinos = []

    for origen, destino in base_conocimiento["reglas"]:

        if origen == estacion:
            vecinos.append(destino)

    return vecinos


# ============================================================
# 6. COSTO DE LOS DESPLAZAMIENTOS
# ============================================================
# Cada desplazamiento entre dos estaciones tiene un costo
# de 1.

def obtener_costo(origen, destino):

    for estacion_origen, estacion_destino in base_conocimiento["reglas"]:

        if (
            estacion_origen == origen
            and estacion_destino == destino
        ):
            return 1

    return float("inf")


# ============================================================
# 7. FUNCIÓN HEURÍSTICA
# ============================================================
# La heurística proporciona una estimación del costo
# restante hasta el destino.

heuristica = {
    "Portal Norte": 5,
    "Toberín": 5,
    "Calle 100": 4,
    "Calle 72": 3,
    "Calle 63": 2,
    "Calle 53": 2,
    "Calle 45": 1,
    "Calle 26": 1,
    "Portal El Dorado": 1,
    "Portal Américas": 0
}


def estimar_distancia(estacion):

    return heuristica.get(estacion, 0)


# ============================================================
# 8. ALGORITMO DE BÚSQUEDA A*
# ============================================================
# A* combina:
#
# g(n) = costo real desde el origen
# h(n) = estimación hasta el destino
#
# f(n) = g(n) + h(n)

def buscar_ruta(origen, destino):

    # Estaciones pendientes de explorar
    abiertos = [origen]

    # Estaciones que ya fueron exploradas
    cerrados = []

    # Guarda el padre de cada estación
    padres = {
        origen: None
    }

    # Costo acumulado desde el origen
    costo_real = {
        origen: 0
    }

    while abiertos:

        # Seleccionamos la estación con menor
        # costo estimado.
        actual = min(
            abiertos,
            key=lambda estacion:
            costo_real[estacion]
            + estimar_distancia(estacion)
        )

        # Si llegamos al destino terminamos
        if actual == destino:
            break

        # Movemos la estación a la lista de cerrados
        abiertos.remove(actual)
        cerrados.append(actual)

        # Obtenemos los vecinos usando las reglas
        vecinos = obtener_vecinos(actual)

        for vecino in vecinos:

            # Ignoramos estaciones ya exploradas
            if vecino in cerrados:
                continue

            # Calculamos el costo de llegar al vecino
            nuevo_costo = (
                costo_real[actual]
                + obtener_costo(actual, vecino)
            )

            # Si encontramos una ruta mejor
            if (
                vecino not in costo_real
                or nuevo_costo < costo_real[vecino]
            ):

                costo_real[vecino] = nuevo_costo

                padres[vecino] = actual

                if vecino not in abiertos:
                    abiertos.append(vecino)

    # Si no se encontró el destino
    if destino not in padres:
        return None, None

    # ========================================================
    # RECONSTRUCCIÓN DE LA RUTA
    # ========================================================

    ruta = []

    actual = destino

    while actual is not None:

        ruta.append(actual)

        actual = padres[actual]

    # Invertimos la ruta
    ruta.reverse()

    return ruta, costo_real[destino]


# ============================================================
# 9. MOSTRAR LA BASE DE CONOCIMIENTO
# ============================================================

def mostrar_base_conocimiento():

    print("\n======================================")
    print("       BASE DE CONOCIMIENTO")
    print("======================================")

    print("\nHechos - Estaciones:")

    for estacion in base_conocimiento["estaciones"]:
        print("-", estacion)

    print("\nReglas - Conexiones:")

    for origen, destino in base_conocimiento["reglas"]:
        print(
            f"Si estoy en {origen}, "
            f"puedo ir a {destino}"
        )


# ============================================================
# 10. PROGRAMA PRINCIPAL
# ============================================================

print("======================================")
print("   SISTEMA INTELIGENTE DE RUTAS")
print("   Transporte Masivo de Bogotá")
print("======================================")


# Mostrar las estaciones disponibles

print("\nEstaciones disponibles:")

for estacion in estaciones:
    print("-", estacion)


# ============================================================
# 11. SOLICITAR ORIGEN Y DESTINO
# ============================================================

entrada_origen = input(
    "\nIngrese la estación de origen: "
)

entrada_destino = input(
    "Ingrese la estación de destino: "
)


# ============================================================
# 12. NORMALIZAR LAS ENTRADAS
# ============================================================

estaciones_normalizadas = {
    normalizar_texto(estacion): estacion
    for estacion in estaciones
}


origen = estaciones_normalizadas.get(
    normalizar_texto(entrada_origen)
)

destino = estaciones_normalizadas.get(
    normalizar_texto(entrada_destino)
)


# ============================================================
# 13. VALIDAR ORIGEN Y DESTINO
# ============================================================

if origen is None:

    print("\nLa estación de origen no existe.")

elif destino is None:

    print("\nLa estación de destino no existe.")

else:

    print("\nBuscando la mejor ruta...")
    print("Aplicando reglas de conocimiento y búsqueda A*...")

    # Ejecutamos el algoritmo
    ruta, costo = buscar_ruta(
        origen,
        destino
    )

    # ========================================================
    # 14. MOSTRAR RESULTADO
    # ========================================================

    if ruta is None:

        print("\nNo se encontró una ruta.")

    else:

        print("\n======================================")
        print("          RUTA ENCONTRADA")
        print("======================================")

        print(f"\nOrigen: {origen}")
        print(f"Destino: {destino}")

        print("\nRuta:")

        for i, estacion in enumerate(
            ruta,
            start=1
        ):

            print(
                f"{i}. {estacion}"
            )

        print("--------------------------------------")

        print(
            f"Costo total: {costo}"
        )

        print(
            f"Número de estaciones: {len(ruta)}"
        )

        print("======================================")