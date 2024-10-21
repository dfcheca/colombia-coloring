# Diccionario que mapea los nombres de departamentos a sus abreviaturas
department_mapping = {
    "Amazonas": "AM", "Antioquia": "AN", "Arauca": "AR", "Atlántico": "AT", "Bogotá": "BG", 
    "Bolívar": "BL", "Boyacá": "BY", "Caldas": "CL", "Caquetá": "CQ", "Casanare": "CS", 
    "Cauca": "CC", "Cesar": "CE", "Chocó": "CH", "Córdoba": "CO", "Cundinamarca": "CU", 
    "Guainía": "GN", "Guaviare": "GV", "Huila": "HU", "La Guajira": "LG", "Magdalena": "MA", 
    "Meta": "ME", "Nariño": "NA", "Norte": "NS", "Putumayo": "PU", "Quindío": "QU", 
    "Risaralda": "RI", "San Andrés y Providencia": "SP", "Santander": "SA", "Sucre": "SU", 
    "Tolima": "TO", "Valle": "VC", "Vaupés": "VP", "Vichada": "VI"
}

def replace_departments(input_file, output_file):
    # Leer el archivo de entrada
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Realizar las sustituciones iniciales de "Norte de Santander" por "Norte" y "Valle del Cauca" por "Valle"
    content = content.replace("Norte de Santander", "Norte")
    content = content.replace("Valle del Cauca", "Valle")

    # Realizar las sustituciones para cada departamento usando las abreviaturas
    for full_name, abbr in department_mapping.items():
        content = content.replace(full_name, abbr)

    # Crear una lista final de pares
    result = set()  # Usamos un conjunto para evitar duplicados considerando permutaciones
    
    # Procesar línea por línea
    lines = content.splitlines()
    for line in lines:
        # Remover numerales y cualquier espacio adicional
        line = line.split('.', 1)[-1].strip()  # Elimina el numeral si existe y deja la parte después
        # Separar la parte antes del colon (el departamento) de la parte después (los vecinos)
        if ':' in line:
            dept, neighbors = line.split(':', 1)  # Solo tomar la primera parte
            dept = dept.strip()  # Eliminar posibles espacios en blanco

            # Omitir la línea de "SP" si no tiene vecinos
            if dept == "SP":
                continue

            # Crear pares del formato "X Y" donde X es el departamento y Y es cada vecino
            neighbor_list = [n.strip() for n in neighbors.split(',')]
            for neighbor in neighbor_list:
                # Asegurar que solo quede el par que es alfabéticamente menor
                if neighbor:  # Solo agregar si hay un vecino
                    pair = tuple(sorted([dept, neighbor]))  # Ordenar alfabéticamente
                    result.add(pair)

    # Ordenar las parejas alfabéticamente
    sorted_result = sorted(result)

    # Escribir la lista resultante en el archivo de salida, sin numerales ni formato adicional
    with open(output_file, 'w', encoding='utf-8') as f:
        # Escribir solo las parejas sin línea en blanco al final
        f.write('\n'.join(f"{pair[0]} {pair[1]}" for pair in sorted_result))

# Nombres de archivo
input_filename = "raw.txt"
output_filename = "colombia.dat"

# Ejecutar el proceso de sustitución
replace_departments(input_filename, output_filename)