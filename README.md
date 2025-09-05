# Proyecto Shodan 

## Descripción
Este proyecto realiza búsquedas en Shodan filtrando por ciudad y país (Jalapa, Guatemala). Incluye:

- Script real (`busqueda_shodan1.py`) usando la API de Shodan.
- Script simulado (`busqueda_shodan_test.py`) para pruebas sin API Key.
- Resumen de resultados: total de IPs y total de puertos abiertos.
- Datos del estudiante integrados: número de carnet, nombre, curso y sección.

## Archivos del proyecto
- `busqueda_shodan1.py` → Script con API real.
- `busqueda_shodan_test.py` → Script simulado para pruebas.
- `.env` → Contiene la API Key (no se sube a GitHub).
- `.gitignore` → Ignora `.env` y archivos del sistema.
- `README.md` → Este archivo.

## Uso
1. Crear archivo `.env` con tu API Key de Shodan:
SHODAN_API_KEY=TU_API_KEY

markdown
Copiar código
2. Ejecutar el script simulado:
python3 busqueda_shodan_test.py

go
Copiar código
3. Para usar el script real, reemplazar con tu API Key válida:
python3 busqueda_shodan1.py

yaml
Copiar código

## Autor
**Kevin Adolfo Tepaz Buc**  
Curso: Ingeniería en Sistemas, Decimo Semestre  
Número de carnet: 1990-21-8618
Fecha: Septiembre 2025