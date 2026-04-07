contenedores = [
    {"numero": "ABC1234567", "estado": "Vacío"},
    {"numero": "DEF7654321", "estado": "Lleno"},
    {"numero": "GHI1122334", "estado": "Vacío"}
]

for contenedor in contenedores:
    if contenedor["estado"] == "Vacío":
        contenedor["estado"] = "Lleno"

for contenedor in contenedores:
    print("Número:", contenedor["numero"])
    print("Estado:", contenedor["estado"])
    print("-----")
