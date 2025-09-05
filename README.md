# Proyecto: Búsqueda Shodan - Guatemala

## Descripción
Este proyecto es un script en Python que realiza búsquedas en Shodan filtrando por ciudad y país (por ejemplo, Jalapa, Guatemala). Muestra las direcciones IP encontradas, los puertos abiertos y un resumen de los resultados, además de incluir información del estudiante.

En esta versión de prueba, se simulan los resultados para no necesitar créditos de la API gratuita de Shodan.

## Requisitos
- Python 3.6 o superior
- Librerías de Python:
  - shodan (solo si usas la API real)
  - python-dotenv (para cargar la API Key desde `.env`)
  
Para instalar dependencias:
```bash
pip install shodan python-dotenv
