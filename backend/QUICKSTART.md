# 🚀 FinanceFlow Backend - Quick Start

El backend está completamente implementado y listo para usar. Todos los 26 endpoints están funcionales.

## ⚡ Inicio Rápido (3 pasos)

### 1. Instalar dependencias
```bash
cd backend
pip install -r requirements.txt
```

### 2. Ejecutar el servidor
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará en: **http://localhost:8000**

### 3. Explorar la documentación
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📋 Endpoints Implementados (26 total)

### ✅ Autenticación (4)
- `POST /api/v1/auth/register` - Registrar usuario
- `POST /api/v1/auth/login` - Iniciar sesión
- `GET /api/v1/auth/me` - Obtener usuario actual
- `POST /api/v1/auth/refresh-token` - Renovar token

### ✅ Usuarios (3)
- `GET /api/v1/users/{user_id}` - Obtener usuario
- `PUT /api/v1/users/{user_id}` - Actualizar usuario
- `DELETE /api/v1/users/{user_id}` - Eliminar usuario

### ✅ Rachas (3)
- `GET /api/v1/streaks/{user_id}` - Obtener racha actual
- `POST /api/v1/streaks/{user_id}/increment` - Incrementar racha
- `GET /api/v1/streaks/leaderboard/top` - Obtener leaderboard

### ✅ Perfiles (3)
- `GET /api/v1/profiles/{user_id}` - Obtener perfil
- `POST /api/v1/profiles/quiz/submit` - Enviar quiz
- `PUT /api/v1/profiles/{user_id}` - Actualizar perfil

### ✅ Chat (3)
- `POST /api/v1/chat/message` - Enviar mensaje
- `GET /api/v1/chat/{conversation_id}/history` - Historial
- `DELETE /api/v1/chat/{conversation_id}` - Eliminar chat

### ✅ Juegos (3)
- `GET /api/v1/games/scenarios` - Listar escenarios
- `GET /api/v1/games/scenarios/{id}` - Obtener escenario
- `POST /api/v1/games/responses` - Enviar respuesta

### ✅ Conceptos (4)
- `GET /api/v1/concepts` - Listar conceptos
- `GET /api/v1/concepts/{id}` - Obtener concepto
- `GET /api/v1/concepts/search?q=query` - Buscar
- `GET /api/v1/concepts/category/{cat}` - Por categoría

## 🔑 Autenticación

Los endpoints protegidos requieren el header:
```
Authorization: Bearer <token>
```

**Ejemplo con curl:**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/v1/auth/me
```

## 📦 Estructura del Proyecto

```
backend/
├── app/
│   ├── api/v1/              # Routers (26 endpoints)
│   ├── models/              # Modelos de datos
│   ├── schemas/             # Validación Pydantic
│   ├── repositories/        # Acceso a datos
│   ├── services/            # Lógica de negocio
│   ├── core/                # Config y seguridad
│   ├── utils/               # Utilidades
│   └── main.py              # App FastAPI
├── test_backend.py          # Tests de integración
├── requirements.txt         # Dependencias
├── .env.example             # Variables de entorno
├── README.md                # Documentación
└── FRONTEND_INTEGRATION.js  # Ejemplos para frontend
```

## 🔌 Conectar desde Frontend

Ver `FRONTEND_INTEGRATION.js` para ejemplos completos de uso desde React/TypeScript.

**Ejemplo rápido:**
```javascript
// Registrarse
const data = await registerUser("user@example.com", "pass123", "John");

// Login
const token = await loginUser("user@example.com", "pass123");

// Obtener conceptos
const concepts = await getConcepts(10);

// Jugar escenario
const result = await submitGameResponse(scenarioId, answerIndex);
```

## 💾 Almacenamiento

Actualmente usa almacenamiento en memoria. Para producción:

1. **MongoDB**: Descomentar en `mongodb.py` y conectar con motor
2. **PostgreSQL**: Usar SQLAlchemy con `app.db` module
3. **Firebase**: Reemplazar repositorios

## 🧪 Tests

Ejecutar tests de integración:
```bash
python test_backend.py
```

## 🛠️ Variables de Entorno

Copiar `.env.example` a `.env`:
```bash
cp .env.example .env
```

Editar según necesario:
- `APP_NAME` - Nombre de la app
- `DEBUG` - Modo debug
- `MONGODB_URI` - URI de MongoDB (cuando uses BD real)
- `JWT_SECRET` - Clave para tokens (cambiar en producción)

## 📝 Notas Importantes

✅ **Implementado:**
- Autenticación con tokens (7 días de expiración)
- Hashing de contraseñas (SHA256 - mejorar a bcrypt en prod)
- CORS habilitado para desarrollo
- Validación con Pydantic v2
- Estructura escalable listo para MongoDB

⚠️ **Por mejorar para producción:**
- Cambiar hashing a bcrypt
- Conectar a MongoDB real
- Agregar rate limiting
- Agregar logging
- Tests unitarios más completos
- Variables de entorno seguras (uso de secretos)

## 🚀 Próximos Pasos

1. **Integrar con frontend React** - Usar ejemplos en `FRONTEND_INTEGRATION.js`
2. **Conectar MongoDB** - Configurar en `.env` y activar en `database/mongodb.py`
3. **Agregar más escenarios/conceptos** - Editar `game_repository.py` y `concept_repository.py`
4. **Implementar autenticación social** - OAuth con Google/GitHub
5. **Deploy** - Usar Heroku, Railway, Render o similar

## 📞 Support

Todos los routers están en `app/api/v1/`:
- `auth.py` - Autenticación
- `users.py` - Gestión de usuarios
- `profiles.py` - Perfiles
- `streaks.py` - Rachas
- `chat.py` - Chat
- `games.py` - Juegos
- `concepts.py` - Conceptos educativos

¡El backend está listo para usar! 🎉
