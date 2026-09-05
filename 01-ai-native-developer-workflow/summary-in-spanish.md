# Summary — Homework 1: AI-Native Developer Workflow

## 1. Objetivo del Homework

El objetivo del Homework 1 del AI Dev Tools Zoomcamp es aprender a utilizar herramientas de desarrollo asistidas por IA dentro de un flujo de trabajo real de desarrollo de software.

Durante el ejercicio se ha utilizado Cursor como agente de programación para diseñar, implementar, probar, documentar y versionar una aplicación web.

El proyecto desarrollado es:

**Family Chore Manager v1**

Una aplicación web para gestionar las tareas domésticas de una familia, permitiendo asignarlas, completarlas y obtener puntos mediante un sistema de ranking.

---

## 2. Entorno utilizado

| Herramienta         | Versión          |
| ------------------- | ---------------- |
| Sistema operativo   | Windows          |
| Git                 | 2.54.0.windows.1 |
| Python global       | 3.14.5           |
| Python del proyecto | 3.13.15          |
| uv                  | 0.12.10          |
| Cursor              | 3.9.8 x64        |
| Django              | 6.1.1            |
| Base de datos       | SQLite           |

El proyecto utiliza `uv` para gestionar Python, el entorno virtual y las dependencias.

---

## 3. Repositorio Git

Repositorio GitHub:

https://github.com/restimartinez/ai-dev-tools-zoomcamp.git

La estructura final del repositorio es:

```text
ai-dev-tools-zoomcamp/
├── .git/
└── 01-ai-native-developer-workflow/
    ├── .gitignore
    ├── .python-version
    ├── README.md
    ├── pyproject.toml
    ├── uv.lock
    ├── manage.py
    ├── _docs/
    │   ├── plan.md
    │   └── backlog.md
    ├── config/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── chores/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── migrations/
    │   │   └── 0001_familymember.py
    │   └── templates/
    ├── static/
    │   └── css/
    │       └── styles.css
    └── templates/
        ├── base.html
        └── registration/
            └── login.html
```

El repositorio tiene un único directorio `.git` en la raíz.

El proyecto Django se encuentra dentro de:

```text
01-ai-native-developer-workflow/
```

---

## 4. Producto desarrollado

### Family Chore Manager v1

La aplicación permite a una familia gestionar las tareas domésticas mediante un sistema de tareas y puntos.

El objetivo es que cualquier miembro de la familia pueda consultar y completar las tareas pendientes y que el sistema mantenga un historial de las tareas realizadas.

---

## 5. Funcionalidades definidas

Las principales funcionalidades acordadas en la especificación son:

1. **Gestión y asignación de tareas**

   * El padre/madre puede crear tareas.
   * Las tareas pueden asignarse a un miembro concreto.
   * También pueden quedar sin asignar para que cualquier miembro pueda realizarlas.
   * Las tareas tienen una puntuación fija.

2. **Tareas recurrentes**

   * Recurrencia diaria.
   * Recurrencia semanal.
   * Selección de determinados días de la semana.
   * Cuando una tarea recurrente se completa se crea automáticamente la siguiente ocurrencia.

3. **Puntos y ranking familiar**

   * El miembro que realmente completa la tarea obtiene los puntos.
   * Existe ranking semanal.
   * El ranking semanal utiliza la semana natural de lunes a domingo.
   * Los puntos de toda la historia se utilizan como desempate.
   * También existe un ranking histórico.

4. **Historial de tareas**

   * Se conserva quién estaba originalmente asignado.
   * Se conserva quién realizó finalmente la tarea.
   * Se conserva la fecha de realización.
   * El historial de tareas completadas es inmutable.

---

## 6. Reglas de negocio principales

La aplicación contempla las siguientes reglas:

* Existe exactamente un padre/madre administrador.
* El padre/madre también es un miembro de la familia y puede completar tareas y obtener puntos.
* Todos los miembros activos tienen usuario y contraseña.
* El padre/madre puede crear y asignar tareas.
* Cualquier miembro activo puede completar una tarea abierta.
* Si una tarea está asignada a una persona y otra persona la completa, los puntos los obtiene quien la ha completado.
* Una tarea completada genera la siguiente ocurrencia si es recurrente.
* Una tarea recurrente que no se completa permanece pendiente.
* Una tarea cancelada no genera puntos.
* Una tarea cancelada no genera una nueva ocurrencia.
* Los miembros desactivados conservan su historial y sus puntos.
* Los miembros desactivados no pueden iniciar sesión ni recibir nuevas tareas.
* No existen notificaciones en la versión 1.

---

## 7. Arquitectura

Se decidió utilizar una arquitectura sencilla y apropiada para el ejercicio:

* Django.
* Una única aplicación Django llamada `chores`.
* Templates renderizados en servidor.
* HTML y CSS responsive.
* SQLite para desarrollo.
* Autenticación estándar de Django.
* Django ORM.
* Tests mediante `django.test.TestCase`.
* Sin API REST.
* Sin SPA.
* Sin Celery.
* Sin colas externas.

La aplicación está diseñada para funcionar tanto en ordenador como en dispositivos móviles.

---

## 8. Instalación inicial

Se instaló Python 3.13.15 mediante `uv`:

```bash
uv python install 3.13.15
```

Se estableció Python 3.13.15 como versión del proyecto:

```bash
uv python pin 3.13.15
```

El proyecto se encuentra en:

```text
C:\Users\resti\source\ai-dev-tools-zoomcamp\01-ai-native-developer-workflow
```

Desde ese directorio se sincronizan las dependencias con:

```bash
uv sync
```

Django se añadió como dependencia:

```bash
uv add django
```

La versión final utilizada es:

```text
Django 6.1.1
```

---

## 9. Configuración inicial de uv

Inicialmente `uv init` creó una estructura orientada a un paquete/CLI de Python, incluyendo:

* Directorio `src/`.
* `[project.scripts]`.
* `[build-system]`.
* Configuración de `uv_build`.

Como el proyecto era una aplicación Django y no un paquete CLI instalable, se eliminó esa estructura innecesaria.

Se eliminaron:

* `src/`.
* `[project.scripts]`.
* `[build-system]`.

El proyecto pasó a funcionar como un proyecto virtual gestionado por `uv`.

El `pyproject.toml` contiene actualmente las dependencias del proyecto y la versión de Python requerida.

---

## 10. Comprobar el proyecto Django

Para comprobar que la configuración de Django es correcta:

```bash
uv run python manage.py check
```

El resultado obtenido fue:

```text
System check identified no issues (0 silenced).
```

Esto confirma que Django no detecta problemas de configuración.

---

## 11. Base de datos

La aplicación utiliza SQLite durante el desarrollo.

La base de datos se crea mediante las migraciones de Django:

```bash
uv run python manage.py migrate
```

El fichero:

```text
db.sqlite3
```

se encuentra excluido del repositorio mediante `.gitignore`.

---

## 12. Crear el superusuario

Para crear el usuario administrador inicial:

```bash
uv run python manage.py createsuperuser
```

Django solicita:

* Username.
* Email.
* Password.

Después se puede acceder al panel de administración mediante:

```text
http://127.0.0.1:8000/admin/
```

El usuario administrador puede utilizarse inicialmente para configurar el primer miembro padre de la familia.

---

## 13. Ejecutar la aplicación

Desde:

```text
01-ai-native-developer-workflow
```

ejecutar:

```bash
uv run python manage.py runserver
```

La aplicación queda disponible normalmente en:

```text
http://127.0.0.1:8000/
```

El panel de administración está disponible en:

```text
http://127.0.0.1:8000/admin/
```

---

# 14. Tests

Los tests se ejecutan con:

```bash
uv run python manage.py test chores
```

Después de implementar las primeras funcionalidades se obtuvo:

```text
Found 11 test(s).

Ran 11 tests

OK
```

Los tests cubren actualmente:

* Acceso anónimo.
* Redirección al login.
* Login correcto.
* Credenciales incorrectas.
* Logout.
* Creación de `FamilyMember`.
* Relación entre `User` y `FamilyMember`.
* Usuario padre.
* Usuario activo/inactivo.
* Nombre visible del miembro.
* Comportamiento del modelo.

---

# 15. Task 1 — Project Foundation and Authentication

La primera tarea del backlog fue:

**Finish project foundation and authentication**

Incluía:

* Configuración de Django.
* Configuración de templates.
* Configuración de static files.
* Configuración de zona horaria.
* Layout base responsive.
* Login.
* Logout.
* Protección de las vistas mediante autenticación.
* Tests de autenticación.

---

## 15.1 Configuración

Se modificó:

```text
config/settings.py
```

Se configuraron:

* Directorios de templates.
* Directorios de archivos estáticos.
* `TIME_ZONE`.
* `LOGIN_URL`.
* `LOGIN_REDIRECT_URL`.
* `LOGOUT_REDIRECT_URL`.

---

## 15.2 URLs

Se configuró:

```text
config/urls.py
```

utilizando las vistas de autenticación proporcionadas por Django:

* `LoginView`.
* `LogoutView`.

También se configuraron las URLs de la aplicación `chores`.

---

## 15.3 Vista protegida

La vista principal utiliza:

```python
@login_required
```

Por tanto, un usuario no autenticado es redirigido al formulario de login.

---

## 15.4 Templates

Se crearon:

```text
templates/base.html
templates/registration/login.html
chores/templates/chores/home.html
```

El layout principal es responsive.

---

## 15.5 CSS

Se creó:

```text
static/css/styles.css
```

para proporcionar una interfaz sencilla y responsive.

---

## 15.6 Tests de autenticación

Se añadieron tests para comprobar:

* Un usuario anónimo es redirigido al login.
* Un usuario autenticado puede acceder a la página principal.
* Las credenciales incorrectas son rechazadas.
* El logout elimina la sesión.
* El acceso autenticado funciona correctamente.

La implementación de autenticación fue posteriormente versionada en Git.

---

# 16. Task 2 — FamilyMember

La segunda tarea implementada fue el modelo de miembros de la familia.

Se creó:

```text
chores/models.py
```

con el modelo:

```text
FamilyMember
```

---

## 16.1 Modelo FamilyMember

El modelo contiene:

* `user`
* `is_parent`
* `is_active`
* `display_name`

La relación con el usuario de Django es:

```python
OneToOneField(User)
```

Esto permite mantener separadas:

* La autenticación proporcionada por Django.
* La información específica de la familia.

---

## 16.2 Campos del modelo

### user

Relación uno a uno con el usuario de Django.

Utiliza:

```python
related_name='family_member'
```

y eliminación en cascada.

### is_parent

Indica si el miembro es el padre/madre administrador.

Por defecto:

```text
False
```

### is_active

Indica si el miembro está activo.

Por defecto:

```text
True
```

### display_name

Nombre que se mostrará en la aplicación.

Es opcional.

---

## 16.3 Nombre visible

El modelo dispone de un método:

```python
get_display_name()
```

Si el usuario tiene un `display_name`, se utiliza ese nombre.

Si no está definido, se utiliza el username de Django.

El método `__str__` utiliza también este nombre visible.

---

## 16.4 Migración

Se generó:

```text
chores/migrations/0001_familymember.py
```

y se aplicó mediante:

```bash
uv run python manage.py migrate
```

---

## 16.5 Django Admin

El modelo `FamilyMember` se registró en:

```text
chores/admin.py
```

El administrador puede crear miembros y marcar uno de ellos como:

```text
is_parent = True
```

También puede marcar si el miembro está activo:

```text
is_active = True
```

Para facilitar la selección del usuario se configuró `autocomplete_fields`.

---

## 16.6 Decisión sobre el primer padre

Se decidió no implementar un sistema de registro público.

El primer miembro padre se configura inicialmente desde Django Admin:

1. Crear el usuario Django.
2. Crear su `FamilyMember`.
3. Marcar `is_parent=True`.
4. Marcar `is_active=True`.

La regla de negocio que garantiza que solamente exista un padre se podrá implementar posteriormente.

No se añadió de momento una restricción de base de datos que fuerce exactamente un padre.

---

## 16.7 Login de usuarios desactivados

Aunque el modelo ya dispone de `is_active`, la lógica completa para impedir el login y la participación de miembros desactivados se deja para la tarea de gestión de miembros.

Esto evita adelantar lógica de negocio que corresponde a una tarea posterior del backlog.

---

# 17. Documentación interna

Se crearon dos documentos para trabajar con Cursor de forma estructurada.

## `_docs/plan.md`

Contiene el plan general de implementación:

1. Project skeleton.
2. Members.
3. Tasks non-recurring.
4. History/ranking.
5. Recurrence.
6. Polish.

También define la estrategia de testing.

---

## `_docs/backlog.md`

Contiene las tareas concretas:

1. Finish project foundation and authentication.
2. FamilyMember model and parent bootstrap.
3. Member management.
4. Task model and open-task board.
5. Parent task management.
6. Task completion and history.
7. Recurring tasks.
8. Weekly and all-time ranking.
9. Permissions polish and responsive UI.
10. Automated tests and README.

---

# 18. Respuestas del Homework

## Q1 — Coding agent

El coding agent utilizado fue:

**Cursor**

---

## Q2 — 2-4 features

Las principales funcionalidades obtenidas de la especificación fueron:

> The main features are task management and assignment, recurring chores, points and family ranking, and completion history showing who completed each task and when.

---

## Q3 — Archivo donde incluir la aplicación

Para registrar la aplicación Django se debe modificar:

```text
settings.py
```

concretamente:

```python
INSTALLED_APPS
```

---

## Q4 — Primera tarea del backlog

La primera tarea de:

```text
_docs/backlog.md
```

es:

> Finish project foundation and authentication

Incluye completar la configuración de Django, añadir un layout responsive, implementar login/logout y requerir autenticación en las vistas de la aplicación.

---

## Q5 — Ejecutar Django

El servidor se ejecuta mediante:

```bash
uv run python manage.py runserver
```

Los tests se ejecutan mediante:

```bash
uv run python manage.py test chores
```

---

# 19. `.gitignore`

Se configuró `.gitignore` para evitar subir al repositorio archivos generados o específicos del entorno local.

Entre ellos:

```text
.venv/
__pycache__/
*.pyc
db.sqlite3
.env
.idea/
.vscode/
.coverage
.pytest_cache/
```

También se mantienen versionados:

```text
.python-version
pyproject.toml
uv.lock
```

Esto permite reproducir el entorno correctamente.

---

# 20. Estrategia Git

Se decidió realizar commits separados por tareas importantes del Homework.

Algunos commits relevantes son:

```text
Initialize Django project
Add Python and Django gitignore
Q5: Add FamilyMember model
Move Homework 1 into dedicated folder
```

La intención es mantener un historial que permita identificar claramente qué se ha realizado en cada fase.

Después de cada tarea se ejecutan los tests y se comprueba el estado del repositorio antes de hacer push.

---

# 21. Reorganización del repositorio

Inicialmente el proyecto Django estaba en una ubicación diferente.

Posteriormente se reorganizó para que el Homework 1 estuviera dentro de:

```text
01-ai-native-developer-workflow/
```

Esta organización coincide mejor con la estructura del curso.

Es importante que el `.git` permanezca únicamente en:

```text
ai-dev-tools-zoomcamp/.git
```

y que no exista un segundo repositorio Git dentro del directorio del Homework.

---

## 21.1 Verificación después de la reorganización

Se comprobó:

```bash
uv sync
```

y:

```bash
uv run python manage.py check
```

Resultado:

```text
System check identified no issues (0 silenced).
```

También se ejecutaron los tests:

```bash
uv run python manage.py test chores
```

Resultado:

```text
Found 11 test(s).

Ran 11 tests

OK
```

Por tanto, la reorganización no rompió el proyecto.

---

## 21.2 README

El README fue actualizado para indicar que el Homework 1 se encuentra dentro de:

```text
01-ai-native-developer-workflow/
```

También se indicó que los comandos de Django deben ejecutarse desde esa carpeta.

La instalación básica documentada es:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

---

# 22. Flujo de trabajo utilizado con Cursor

El desarrollo se realizó siguiendo un flujo de trabajo orientado a AI-Native Development.

El proceso utilizado fue:

1. Definir una idea inicial.
2. Convertirla en una especificación de producto.
3. Pedir a Cursor que analizara la especificación.
4. Crear un plan de implementación.
5. Crear un backlog.
6. Implementar las tareas de forma incremental.
7. Ejecutar tests.
8. Revisar los cambios.
9. Hacer commits separados.
10. Hacer push al repositorio GitHub.
11. Mantener documentación del proceso.

Esto permite que la IA no se limite a generar código, sino que participe en planificación, implementación, testing y documentación.

---

# 23. Comandos habituales

## Entrar en el proyecto

```bash
cd C:\Users\resti\source\ai-dev-tools-zoomcamp\01-ai-native-developer-workflow
```

## Sincronizar dependencias

```bash
uv sync
```

## Comprobar Django

```bash
uv run python manage.py check
```

## Crear migraciones

```bash
uv run python manage.py makemigrations
```

## Aplicar migraciones

```bash
uv run python manage.py migrate
```

## Ejecutar tests

```bash
uv run python manage.py test chores
```

## Crear superusuario

```bash
uv run python manage.py createsuperuser
```

## Ejecutar servidor

```bash
uv run python manage.py runserver
```

---

# 24. Estado actual

Actualmente el proyecto dispone de:

* Proyecto Django funcional.
* Gestión de dependencias mediante `uv`.
* Python 3.13.15.
* Django 6.1.1.
* Autenticación mediante Django.
* Login.
* Logout.
* Vistas protegidas.
* Layout responsive.
* Modelo `FamilyMember`.
* Migraciones.
* Django Admin.
* Tests automatizados.
* Documentación de planificación.
* Backlog.
* README actualizado.
* `.gitignore`.
* Repositorio Git correctamente organizado.
* Commits y push realizados a GitHub.

La siguiente fase natural es implementar:

**Task 3 — Member management**

para que el padre pueda crear y desactivar miembros de la familia desde la aplicación.

---

# 25. Resultado del Homework

El Homework 1 ha permitido construir la base de una aplicación Django utilizando un flujo de desarrollo asistido por IA.

La aplicación ya tiene una arquitectura funcional, autenticación, modelo de miembros, tests y documentación.

El proyecto se encuentra preparado para continuar con la implementación incremental de:

* Gestión de miembros.
* Gestión de tareas.
* Asignaciones.
* Finalización de tareas.
* Historial.
* Puntos.
* Ranking.
* Recurrencia.
* Mejoras de interfaz.
* Tests adicionales.

El objetivo final es disponer de una aplicación **Family Chore Manager v1** funcional y suficientemente documentada, desarrollada siguiendo un flujo de trabajo AI-Native.
