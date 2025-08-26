# 🔡 MorseConverter

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)


**MorseConverter** es una aplicación web para traducir texto a código Morse y viceversa, diseñada con Python y Flask, y empaquetada con Docker para un despliegue sencillo. Este proyecto muestra mi capacidad para construir aplicaciones web funcionales, validar entradas de usuario con Regex y garantizar portabilidad con contenedores.

---

## ⚡ Funcionalidades

* 🔤 **Texto → Morse**: Conversión rápida de texto a código Morse.
* 🖋️ **Morse → Texto**: Conversión inversa de código Morse a texto plano.
* ✅ **Validación con Regex**: Control de entradas para evitar caracteres no soportados.
* 🌐 **Interfaz Web**: Formulario intuitivo creado con Flask Templates para una interacción sencilla.
* 🐳 **Docker Ready**: Implementación Docker con `Dockerfile` y `docker-compose`.

---

## 🛠️ Tecnologías Clave

* **Python** → Lógica de conversión robusta y manejo de dependencias.
* **Flask** → Framework ligero para integrar backend y frontend.
* **Regex** → Validación eficiente de entradas de usuario.
* **Docker & Docker Compose** → Contenedores para un despliegue portátil y consistente.

---

## 📚 Aprendizajes

Este proyecto me permitió:

* Python y Flask: Desarrollé una aplicación web completa, desde la lógica de conversión hasta la renderización de plantillas, aplicando buenas prácticas como modularidad y manejo de errores.
* Regex: Diseñé expresiones regulares para validar entradas, resolviendo problemas como el manejo de caracteres no soportados y entradas de usuario defectuosas.
* Docker: Configuré Dockerfile / Docker-compose y optimicé la imagen para despliegues eficientes, enfrentando situaciones como la reducción del tamaño de la imagen.
* Gestión de dependencias: Creé un requirements.txt para garantizar reproducibilidad en entornos locales y contenedores.

---

# 🐳 Ejecución con Docker

Este proyecto incluye una imagen de Docker lista para usar.

## Ejecutar la imagen

```bash
# Descargar y ejecutar la imagen desde Docker Hub
docker pull ivangomezdellosa/morseconvertor:v1
docker run -p 5000:5000 ivangomezdellosa/morseconvertor:v1
```

## Acceder a la aplicación

Una vez iniciado el contenedor, la aplicación estará disponible en:  
**<http://localhost:5000>**

## Requisitos

- Docker instalado
