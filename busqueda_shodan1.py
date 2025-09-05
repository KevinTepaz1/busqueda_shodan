# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import shodan
from collections import Counter

# Datos del estudiante
numero_carnet = "19-90-21-8618"
nombre_completo = "Kevin Adolfo Tepaz Buc"
curso = "Ingeniería en Sistemas"
seccion = "9no Semestre"

# API Key de Shodan
SHODAN_API_KEY = "GWD3u6Yds1HfhOfGrsM37OEuA3YEIGyu"

# Inicializar cliente
api = shodan.Shodan(SHODAN_API_KEY)

# Filtro de búsqueda (Ciudad: Jalapa, País: Guatemala)
query = 'city:"Jalapa" country:"GT"'

try:
    # Buscar en Shodan
    results = api.search(query)
    
    print(f"\n=== Resultados de Shodan para '{query}' ===\n")
    
    # Contadores
    total_ips = len(results['matches'])
    puertos = []

    for match in results['matches']:
        ip = match.get('ip_str', 'N/A')
        port = match.get('port', 'N/A')
        puertos.append(port)
        print(f"IP: {ip} | Puerto: {port}")

    # Resumen
    puerto_counts = Counter(puertos)
    
    print("\n=== Resumen ===")
    print(f"Total de direcciones IP identificadas: {total_ips}")
    print("Total de IPs por puerto abierto:")
    for port, count in puerto_counts.items():
        print(f"Puerto {port}: {count} IPs")

    print("\n=== Datos del estudiante ===")
    print(f"Número de carnet: {numero_carnet}")
    print(f"Nombre completo: {nombre_completo}")
    print(f"Curso: {curso}")
    print(f"Sección: {seccion}")

except shodan.APIError as e:
    print(f"Error de Shodan: {e}")
