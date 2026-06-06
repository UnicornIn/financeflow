# FinanceFlow Backend

API backend para la aplicación web de educación financiera FinanceFlow.

## Instalación

### 1. Crear un entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Copiar `.env.example` a `.env` y ajustar según sea necesario:

```bash
cp .env.example .env
```

## Ejecución

Ejecutar el servidor de desarrollo:

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en `http://localhost:8000`

## Documentación

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Endpoints

### Autenticación (4)
- `POST /api/v1/auth/register` - Registrar nuevo usuario
- `POST /api/v1/auth/login` - Iniciar sesión
- `GET /api/v1/auth/me` - Obtener usuario actual
- `POST /api/v1/auth/refresh-token` - Renovar token

### Usuarios (3)
- `GET /api/v1/users/{user_id}` - Obtener usuario
- `PUT /api/v1/users/{user_id}` - Actualizar usuario
- `DELETE /api/v1/users/{user_id}` - Eliminar usuario

### Rachas (3)
- `GET /api/v1/streaks/{user_id}` - Obtener racha actual
- `POST /api/v1/streaks/{user_id}/increment` - Incrementar racha
- `GET /api/v1/streaks/leaderboard/top` - Obtener leaderboard

### Perfiles (3)
- `GET /api/v1/profiles/{user_id}` - Obtener perfil
- `POST /api/v1/profiles/quiz/submit` - Enviar respuestas del quiz
- `PUT /api/v1/profiles/{user_id}` - Actualizar perfil

### Chat (3)
- `POST /api/v1/chat/message` - Enviar mensaje
- `GET /api/v1/chat/{conversation_id}/history` - Obtener historial de chat
- `DELETE /api/v1/chat/{conversation_id}` - Eliminar conversación

### Juegos (3)
- `GET /api/v1/games/scenarios` - Listar escenarios
- `GET /api/v1/games/scenarios/{id}` - Obtener escenario
- `POST /api/v1/games/responses` - Enviar respuesta a escenario

### Conceptos (4)
- `GET /api/v1/concepts` - Listar conceptos
- `GET /api/v1/concepts/{id}` - Obtener concepto
- `GET /api/v1/concepts/search?q=query` - Buscar conceptos
- `GET /api/v1/concepts/category/{cat}` - Obtener conceptos por categoría

## Autenticación

Incluir el token en el header `Authorization`:

```
Authorization: Bearer <token>
```

## Estructura del Proyecto

```
backend/
├── app/
│   ├── api/v1/          # Routers (endpoints)
│   ├── models/          # Modelos de datos
│   ├── schemas/         # Esquemas Pydantic
│   ├── repositories/    # Capa de acceso a datos
│   ├── services/        # Lógica de negocio
│   ├── core/            # Configuración y seguridad
│   ├── utils/           # Utilidades
│   └── main.py          # Aplicación FastAPI
├── requirements.txt     # Dependencias
└── .env.example         # Ejemplo de variables de entorno
```

## Notas

- El backend ahora usa MongoDB para persistencia de usuarios, chat, perfiles y rachas.
- Los tokens expiran en 7 días.
- Las contraseñas se hashean con SHA256 (usar bcrypt en producción).

