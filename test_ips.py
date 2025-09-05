# -*- coding: utf-8 -*-

from collections import Counter

# Datos del estudiante
numero_carnet = "1990-21-8618"
nombre_completo = "Kevin Adolfo Tepaz Buc"
curso = "Ingenieria en Sistemas"
seccion = "decimo Semestre"
fecha = "septiembre 2025"

# Resultados simulados (como si vinieran de Shodan)
results = {
    'matches': [
        {'ip_str': '192.168.1.1', 'port': 80},
        {'ip_str': '192.168.1.2', 'port': 22},
        {'ip_str': '192.168.1.3', 'port': 80},
        {'ip_str': '192.168.1.4', 'port': 443},
        {'ip_str': '192.168.1.5', 'port': 22},
    ]
}

# Mostrar resultados simulados
print(f"\n=== Resultados simulados de Shodan ===\n")

total_ips = len(results['matches'])
puertos = []

for match in results['matches']:
    ip = match.get('ip_str', 'N/A')
    port = match.get('port', 'N/A')
    puertos.append(port)
    print(f"IP: {ip} | Puerto: {port}")

# Resumen por puerto
puerto_counts = Counter(puertos)

print("\n=== Resumen ===")
print(f"Total de direcciones IP identificadas: {total_ips}")
print("Total de IPs por puerto abierto:")
for port, count in puerto_counts.items():
    print(f"Puerto {port}: {count} IPs")

# Datos del estudiante
print("\n=== Datos del estudiante ===")
print(f"Número de carnet: {numero_carnet}")
print(f"Nombre completo: {nombre_completo}")
print(f"Curso: {curso}")
print(f"Sección: {seccion}")
