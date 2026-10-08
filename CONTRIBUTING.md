# Reglas de trabajo del equipo

## 1. Nombres de las ramas

Cada tarea debe desarrollarse en una rama independiente.

**Tipos de ramas**

| Prefijo     | Uso                    |
| ----------- | ---------------------- |
| `feature/`  | Nuevas funcionalidades |
| `fix/`      | Corrección de errores  |
| `hotfix/`   | Errores urgentes       |
| `refactor/` | Mejoras en el código   |
| `docs/`     | Documentación          |
| `test/`     | Pruebas                |
| `chore/`    | Mantenimiento          |

**Ejemplos de nombres**

```
feature/login-google
fix/error-login
hotfix/error-pagos
refactor/servicio-usuarios
docs/actualizar-readme
test/login
chore/actualizar-dependencias
```

**Reglas**

* Utilizar minúsculas y guiones.
* Escribir nombres cortos y descriptivos.
* No utilizar espacios ni tildes.
* No realizar cambios directamente en `main`.

---

## 2. Cómo escribir los commits

Utilizaremos el formato Conventional Commits.

**Formato**

```
tipo(modulo): descripcion del cambio
```

**Tipos de commits**

| Tipo       | Uso                   |
| ---------- | --------------------- |
| `feat`     | Nueva funcionalidad   |
| `fix`      | Corrección de errores |
| `refactor` | Mejora del código     |
| `docs`     | Documentación         |
| `test`     | Pruebas               |
| `chore`    | Mantenimiento         |

**Ejemplos**

```
feat(auth): agregar inicio de sesion
fix(users): corregir validacion del correo
refactor(api): simplificar servicio de usuarios
docs(readme): actualizar instalacion
test(auth): agregar pruebas de login
chore(deps): actualizar dependencias
```

**Reglas**

* Describir claramente el cambio realizado.
* Cada commit debe tener un propósito claro.
* Evitar mensajes como `cambios`, `update`, `arreglos` o `final`.
* No incluir cambios que no correspondan a la tarea.

---

## 3. ¿Quién revisa a quién?

* El autor no puede aprobar su propio Pull Request.
* Todo PR debe tener al menos una aprobación de otro integrante autorizado.
* Los cambios deben ser revisados por alguien que conozca el módulo afectado.
* Los cambios críticos deben ser revisados por un responsable con experiencia en el área.
* Las revisiones deben ser respetuosas y enfocadas en mejorar el código.
* Los comentarios bloqueantes deben resolverse antes de integrar los cambios.

---

## 4. ¿Qué debe cumplir un Pull Request para ser aprobado?

Antes de aprobar un PR, se debe verificar lo siguiente:

* [ ] Cumple el objetivo de la tarea.
* [ ] El código es claro y sigue las convenciones del proyecto.
* [ ] Las pruebas necesarias pasan correctamente.
* [ ] No contiene contraseñas, tokens ni información sensible.
* [ ] La documentación está actualizada cuando corresponde.
* [ ] No existen errores conocidos que bloqueen la integración.
* [ ] Los comentarios bloqueantes están resueltos.
* [ ] Cuenta con las aprobaciones requeridas.
* [ ] Las verificaciones automáticas obligatorias pasan correctamente.

---

## Regla principal

Ningún Pull Request se integra sin cumplir estos requisitos y recibir la revisión correspondiente.
