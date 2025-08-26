# 🔡 MorseConverter

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)


**MorseConverter** es una aplicación web que traduce texto a código **Morse** y viceversa. El proyecto combina **Python + Flask** para la lógica y la interfaz web, utiliza **Regex** para validar las entradas de usuario y está preparado con **Docker** para facilitar su despliegue en cualquier entorno.

---

## ⚡ Funcionalidades

* 🔤 **Texto → Morse**: Conversión rápida de texto a código Morse.
* 🖋️ **Morse → Texto**: Conversión inversa de código Morse a texto plano.
* ✅ **Validación con Regex**: Control de entradas para evitar caracteres no soportados.
* 🌐 **Interfaz Web**: Formulario simple desarrollado con Flask Templates.
* 🐳 **Docker Ready**: Implementación Docker con `Dockerfile` y `docker-compose`.

---

## 🛠️ Tecnologías Clave

* **Python** → Lenguaje base para la lógica de conversión.
* **Flask** → Framework web ligero para unir backend y frontend.
* **Regex** → Validación de datos eficiente y segura.
* **Docker & Docker Compose** → Contenedores reproducibles y despliegue simplificado.

---

## 📚 Aprendizajes

Este proyecto me permitió:

* Profundizar en **Python** aplicando buenas prácticas de programación y gestión de dependencias, enfrentando tanto problemas de lógica como desafíos de configuración de entornos, sentando una base sólida para proyectos más complejos.
* Desarrollar e integrar el backend y frontend usando **Flask**, construyendo una aplicación web funcional y coherente.
* Implementar Docker, asegurando portabilidad y ejecución consistente en distintos entornos, facilitando la prueba y despliegue de la aplicación.

---

## 🐳 Ejecución con Docker

Este proyecto incluye una imagen de Docker lista para usar y también se puede **iniciar con Docker Compose**.

### Opción 1: Usar imagen pre-construida
```bash
# Descargar y ejecutar la imagen desde Docker Hub
docker pull ivangomezdellosa/morseconvertor:v1
docker run -p 5000:5000 ivangomezdellosa/morseconvertor:v1
```

### Opción 2: Construir localmente
```bash
# Clonar el repositorio
git clone https://github.com/IvanGomezDellOsa/MorseConverter.git
cd MorseConverter

# Construir y ejecutar con docker-compose
docker-compose up --build
```

### Acceder a la aplicación
Una vez iniciado el contenedor, la aplicación estará disponible en:
**http://localhost:5000**

### Requisitos
- Docker instalado
- Docker Compose (para construcción local)

# Clonar el repositorio
git clone https://github.com/IvanGomezDellOsa/MorseConverter.git
cd MorseConverter

# Construir y ejecutar con docker-compose
docker-compose up --build
# Clonar el repositorio
git clone https://github.com/IvanGomezDellOsa/MorseConverter.git
cd MorseConverter

# Construir y ejecutar con docker-compose
docker-compose up --build
