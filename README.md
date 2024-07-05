# Map My World API

## Descripción

Map My World es una API RESTful para explorar y revisar diferentes ubicaciones y categorías en todo el mundo, como restaurantes, parques y museos. La API está construida utilizando Python y FastAPI.

## Características

- Gestión de Ubicaciones y Categorías
- Recomendaciones de Exploración basadas en revisiones no recientes
- Endpoints para crear, leer y gestionar ubicaciones y categorías

## Tecnologías

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Pytest

## Instalación

1. Clona el repositorio:
    ```sh
    git clone git@github.com:juliancms/mmw.git
    cd mmw
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Inicia el servidor:
    ```sh
    uvicorn app.main:app --reload
    ```

## Uso

### Endpoints

- **Crear una ubicación**
    - `POST /locations/`
    - Body:
        ```json
        {
            "latitude": 40.712776,
            "longitude": -74.005974
        }
        ```

- **Obtener ubicaciones**
    - `GET /locations/`

- **Crear una categoría**
    - `POST /categories/`
    - Body:
        ```json
        {
            "name": "Restaurant"
        }
        ```

- **Obtener categorías**
    - `GET /categories/`

- **Crear una revisión de ubicación-categoría**
    - `POST /reviews/`
    - Body:
        ```json
        {
            "location_id": 1,
            "category_id": 1,
            "last_reviewed": "2023-07-01T12:00:00"
        }
        ```

- **Obtener recomendaciones**
    - `GET /recommendations/`

## Pruebas

Ejecuta las pruebas utilizando `pytest`:
```sh
pytest
