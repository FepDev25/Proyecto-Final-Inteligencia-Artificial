# DERMA SCAN IA: Prediagnóstico de Enfermedades de la Piel con Inteligencia Artificial

Realizado por: Samantha Suquilanda, Felipe Peralta, Andres Torres y Kevin Chipantiza.

## Descripción

Este proyecto es un sistema de prediagnóstico para enfermedades de la piel que utiliza un modelo de aprendizaje profundo para clasificar imágenes dermatológicas. La aplicación consta de un frontend desarrollado en Angular, un backend en FastAPI y un modelo de clasificación de imágenes entrenado con PyTorch.

## Estructura del Proyecto

-   `backend/`: Contiene el código fuente de la API desarrollada con FastAPI (Python), que se encarga de servir el modelo y gestionar las predicciones.
-   `frontend/`: Contiene el código fuente de la aplicación web desarrollada con Angular, desde donde los usuarios pueden interactuar con el sistema.
-   `modelo/`: Incluye el Jupyter Notebook (`Modelo completo 8000 copy.ipynb`) con todo el proceso de análisis, preprocesamiento, entrenamiento y evaluación del modelo de clasificación.
-   `modelo-final/`: Contiene los datos procesados y divididos en conjuntos de entrenamiento, validación y prueba.

## Detalles del Modelo

El núcleo de este proyecto es un modelo de clasificación de imágenes basado en la arquitectura **EfficientNet-B0**, preentrenado en ImageNet y ajustado para este caso de uso específico.

-   **Dataset:** Se utilizó el `Skin Diseases Dataset`, una compilación de varias fuentes de datos abiertas que contiene imágenes de 6 categorías dermatológicas distintas:
    1.  Acné y Rosácea
    2.  Eczema
    3.  Tumores Benignos
    4.  Tumores Malignos
    5.  Afecciones Pigmentarias
    6.  Infecciones de la Piel

-   **Entrenamiento:**
    -   Para evitar el sesgo, el dataset fue **balanceado** mediante técnicas de *data augmentation*, asegurando que cada clase tuviera 8000 imágenes para el entrenamiento.
    -   El modelo fue entrenado durante 20 épocas, logrando una **precisión (accuracy) final del 92%** en el conjunto de prueba.
    -   El notebook detallado del proceso se encuentra en `modelo/Modelo completo 8000 copy.ipynb`.

## Tecnologías Utilizadas

-   **Modelo IA:**
    -   Python
    -   PyTorch
    -   EfficientNet
    -   Scikit-learn
-   **Backend:**
    -   FastAPI
-   **Frontend:**
    -   Angular
    -   TypeScript

## Cómo Empezar

A continuación, se describen los pasos básicos para ejecutar el proyecto.

### Prerrequisitos

-   Node.js y npm/yarn
-   Python 3.8+ y pip
-   Git

### Backend

1.  Navega al directorio del backend:
    ```bash
    cd backend/
    ```
2.  Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  Inicia el servidor de FastAPI:
    ```bash
    uvicorn main:app --reload
    ```

### Frontend

1.  Navega al directorio del frontend:
    ```bash
    cd frontend/dermascan-front/
    ```
2.  Instala las dependencias del proyecto:
    ```bash
    npm install
    ```
3.  Inicia la aplicación de Angular:
    ```bash
    ng serve
    ```
4.  Abre tu navegador y visita `http://localhost:4200/`.
