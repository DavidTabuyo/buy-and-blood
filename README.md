
# 💸 Buy and Blood

### 🧪 Proyecto Final – Ingeniería del Software II  
**Grado en Ingeniería Informática**

---

## 👨‍💻 Autores

- **David Tabuyo Mallo** – FullStack Developer & Software Architect  
- **Darío Martín Muñoz** – Backend Developer & Database Modeler  
- **Daniel Gregori Guerra** – Project Manager & QA  

---

## 📌 Índice

1. [🔍 Introducción](#-introducción)  
2. [👥 Equipo de trabajo](#-equipo-de-trabajo)  
3. [🧩 Requisitos y organización](#-requisitos-y-organización)  
4. [🏗️ Diseño y arquitectura](#-diseño-y-arquitectura)  
5. [🛠️ Desarrollo e implementación](#-desarrollo-e-implementación)  
6. [🚀 CI/CD y despliegue](#-cicd-y-despliegue)  
7. [📸 Resultados y capturas](#-resultados-finales-y-capturas)  
8. [🧠 Conclusiones](#-conclusiones-y-lecciones-aprendidas)  
9. [🔗 Enlaces útiles](#-enlaces-relevantes)

---

## 🔍 Introducción

### ¿Qué es Buy and Blood?

Una plataforma de inversión accesible e inteligente para comprar activos financieros, gestionar carteras y recibir recomendaciones personalizadas.

### Problemas que resuelve

- ⚠️ Complejidad en la selección de activos  
- ❌ Falta de personalización en plataformas  
- 🧩 Herramientas separadas y poco integradas

### Público objetivo

Desde principiantes hasta expertos en inversión, con una interfaz clara y funciones adaptadas.

### Objetivo

Facilitar el acceso al mercado financiero con **planes personalizados**, **seguimiento visual** y **experiencia fluida**.

---

## 👥 Equipo de trabajo

| Integrante              | Rol                                   |
|-------------------------|----------------------------------------|
| David Tabuyo Mallo      | FullStack Developer / Architect        |
| Darío Martín Muñoz      | Backend Developer / DB Modeler         |
| Daniel Gregori Guerra   | Project Manager / QA                   |

**🌀 Metodología ágil (Scrum):** planificación semanal, tareas por iteraciones, revisión continua.

---

## 🧩 Requisitos y organización

### ✅ Requisitos funcionales

- **RF1:** Login con Google  
- **RF2:** Gestión de planes de inversión  
- **RF3:** Compra de activos  
- **RF4:** Comprobación de estado y rendimiento  
- **RF5:** Historial de transacciones

### 📋 Organización con GitHub Projects

- Flujo Kanban: `Backlog → To Do → In Progress → In Review → Done`  
- Tareas priorizadas y validadas por el Project Manager  
- Solo él puede mover tareas a "Done" tras revisión

---

## 🏗️ Diseño y arquitectura

### 🧱 Arquitectura

- Backend: **Django**  
- Frontend: **Vue.js**  
- Base de datos: **PostgreSQL**  
- Despliegue: **Render + GitHub Pages**

### 🔧 Patrones aplicados

- **Command Pattern** en peticiones HTTP (Django)  
- **Template Method** en vistas genéricas (Django)  
- **MVT Pattern** en toda la estructura

### 📊 Diagrama de arquitectura

> *(Aquí iría el diagrama, si lo tienes en imagen)*

---

## 🛠️ Desarrollo e implementación

### 🧼 Buenas prácticas

- Gitflow (`main`, `develop`, `feature/`, `fix/`)  
- Pull Requests con revisión previa  
- Versionado con tags en producción

### 🧪 Pruebas

- Backend: **Tests unitarios con `pytest`**  
- Frontend: No implementadas por simplicidad y tamaño del proyecto

---

## 🚀 CI/CD y despliegue

### 🧪 Tests automáticos con GitHub Actions

- Pipeline en cada push/PR a `main`  
- Tests ejecutados en backend antes de hacer merge

### 🌐 Despliegue

- **Frontend**: GitHub Pages (`npm run build → deploy`)  
- **Backend**: Render (despliegue automático en `main`)

---

## 📸 Resultados Finales y Capturas

- ✔️ Funcionalidades operativas: login, compra, planes  
- 📊 Visualizaciones claras y actualizadas  
- 🌍 Plataforma accesible desde navegador

**🔗 Demo (despliegue):**  
> *(Inserta aquí la URL de la app desplegada)*

---

## 🧠 Conclusiones y lecciones aprendidas

### 📚 Aprendizaje

- Vue.js, workflows reales, coordinación en equipo  
- Estructura profesional de un proyecto software

### 💥 Dificultades

- Falta de experiencia previa en JS/frontend  
- Superadas con aprendizaje colaborativo y autoformación

### 📈 Mejoras futuras

- Añadir compra automática  
- Integrar pasarela de pago fiable

---

## 🔗 Enlaces relevantes

- 📁 Repositorio GitHub:  
  [https://github.com/DavidTabuyo/buy-and-blood](https://github.com/DavidTabuyo/buy-and-blood)

- 📋 GitHub Projects:  
  [https://github.com/users/DavidTabuyo/projects/4](https://github.com/users/DavidTabuyo/projects/4)

- 📄 Guion de la entrega:  
  [docs.google.com](https://docs.google.com/document/d/1BrX1d-0r2X9T_0t28JS8yNtaTAlFFza-obDZPjZGOTQ/edit?tab=t.0)
