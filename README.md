# DERMA SCAN IA: Prediagnóstico de Enfermedades de la Piel con Inteligencia Artificial

Realizado por: Samantha Suquilanda, Felipe Peralta, Andres Torres y Kevin Chipantiza.

## Descripción General

Video explicativo del sistema: https://www.youtube.com/watch?v=_Ygy0iDfcXA

DERMA SCAN IA es un sistema inteligente de prediagnóstico dermatológico que utiliza técnicas de aprendizaje profundo para el análisis automatizado de imágenes de la piel. El sistema es capaz de identificar y clasificar 36 afecciones dermatológicas diferentes con alta precisión, proporcionando a los usuarios un análisis preliminar detallado que incluye diagnóstico principal, condiciones alternativas, explicaciones generadas por IA y síntomas asociados.

La aplicación está diseñada como una herramienta de apoyo que facilita la detección temprana de problemas cutáneos, aunque siempre recalca que no sustituye la evaluación médica profesional.

## Arquitectura del Sistema

El proyecto implementa una arquitectura de tres capas claramente diferenciadas:

- **Frontend**: Aplicación web interactiva desarrollada en Angular
- **Backend**: API REST desarrollada con FastAPI (Python)
- **Base de Datos**: Sistema de persistencia PostgreSQL con información médica estructurada
- **Modelo de IA**: Red neuronal convolucional basada en EfficientNet-B3

## Estructura del Proyecto

```
proyecto/
├── backend/                          # API REST con FastAPI
│   ├── api/                         # Endpoints de la API
│   ├── services/                    # Lógica de negocio y servicios
│   ├── database/                    # Modelos y conexión a BD
│   ├── models/                      # Esquemas de Pydantic
│   ├── modelo/                      # Archivos del modelo entrenado
│   └── credentials/                 # Credenciales de servicios externos
├── frontend/dermascan-front/        # Aplicación Angular
│   ├── src/app/components/          # Componentes de la interfaz
│   ├── src/app/services/           # Servicios de Angular
│   └── src/app/environments/       # Configuración de entornos
├── modelo-final/                    # Notebook y datos del modelo
├── db/                             # Scripts de base de datos
└── presentacion/                   # Documentación del proyecto
```

## Modelo de Inteligencia Artificial

### Arquitectura y Entrenamiento

El sistema utiliza un modelo de clasificación de imágenes basado en **EfficientNet-B3**, una arquitectura de red neuronal convolucional altamente eficiente que balancea precisión y velocidad de inferencia.

**Características del modelo:**
- **Arquitectura base**: EfficientNet-B3 preentrenado en ImageNet
- **Modificaciones**: Capa final reemplazada con Dropout(0.4) y Linear(1536, 36)
- **Clases de salida**: 36 categorías dermatológicas diferentes
- **Tamaño de entrada**: Imágenes RGB de 224x224 píxeles
- **Normalización**: Media [0.5, 0.5, 0.5], Desviación [0.5, 0.5, 0.5]

### Dataset y Rendimiento

**Dataset utilizado**: Massive Skin Disease Balanced Dataset
- **Imágenes totales**: Aproximadamente 262,874 imágenes
- **Clases**: 36 categorías dermatológicas balanceadas
- **División**: 70% entrenamiento, 15% validación, 15% prueba
- **Preprocesamiento**: Redimensionado a 224x224, data augmentation aplicado

**Métricas de rendimiento:**
- **Épocas de entrenamiento**: 10 épocas
- **Precisión alcanzada**: 92%+ en conjunto de validación
- **Optimizador**: Adam con learning rate adaptativo
- **Función de pérdida**: CrossEntropyLoss

### Categorías Detectables

El modelo es capaz de identificar las siguientes 36 afecciones dermatológicas:

1. Acné y Rosácea
2. Queratosis Actínica, Carcinoma Basocelular y Otras Lesiones Malignas
3. Dermatitis Atópica
4. Celulitis Bacteriana
5. Impétigo Bacteriano
6. Lesiones Malignas
7. Melanoma, Cáncer de Piel, Nevos y Lunares
8. Hongos en las Uñas y Otras Enfermedades Ungueales
9. Larva Migrans Cutánea
10. Hiedra Venenosa y Otras Dermatitis de Contacto
11. Lesiones Benignas
12. Psoriasis, Liquen Plano y Enfermedades Relacionadas
13. Enfermedades Ampollares
14. Erupciones Cutáneas
15. Celulitis, Impétigo y Otras Infecciones Bacterianas
16. Sarna, Enfermedad de Lyme y Otras Infestaciones y Picaduras
17. Eccema
18. Queratosis Seborreica y Otros Tumores Benignos
19. Exantemas y Erupciones por Medicamentos
20. Enfermedades Sistémicas con Manifestaciones Cutáneas
21. Pie de Atleta
22. Tatuajes
23. Hongos en las Uñas
24. Tiña, Candidiasis y Otras Infecciones Fúngicas
25. Tiña Corporis (Dermatofitosis)
26. Urticaria (Ronchas)
27. Pérdida de Cabello, Alopecia y Otras Enfermedades Capilares
28. Tumores Vasculares
29. Piel Sana
30. Vasculitis
31. Herpes, VPH y Otras ETS
32. Varicela
33. Enfermedades de la Luz y Trastornos de la Pigmentación
34. Herpes Zóster (Culebrilla)
35. Lupus y Otras Enfermedades del Tejido Conectivo
36. Verrugas, Molusco Contagioso y Otras Infecciones Virales

## Backend (FastAPI)

### Arquitectura y Servicios

El backend está implementado con FastAPI y sigue una arquitectura modular con separación clara de responsabilidades:

**Servicios principales:**
- **Prediction Service**: Manejo del modelo de IA y procesamiento de imágenes
- **Explanation Service**: Generación de explicaciones médicas usando Google Gemini
- **TTS Service**: Conversión de texto a audio para accesibilidad
- **Database Service**: Gestión de datos médicos y historial de predicciones

### Endpoints de la API

**Predicción y análisis:**
- `POST /predict`: Análisis de imagen con diagnóstico completo
- `POST /tts`: Generación de audio a partir de texto

**Gestión de enfermedades:**
- `GET /enfermedades/`: Lista todas las enfermedades registradas
- `GET /enfermedades/{id}`: Información detallada de una enfermedad
- `GET /enfermedades/{id}/sintomas`: Síntomas asociados a una enfermedad

**Historial de predicciones:**
- `GET /predicciones/`: Historial paginado de predicciones
- `GET /predicciones/{id}`: Detalles de una predicción específica
- `GET /predicciones/{id}/posibles_condiciones`: Condiciones alternativas

### Base de Datos

**Estructura relacional en PostgreSQL:**
- **Enfermedades**: Catálogo de afecciones con descripciones detalladas
- **Síntomas**: Base de síntomas asociados a cada enfermedad
- **Predicciones**: Historial de análisis realizados por usuarios
- **Posibles Condiciones**: Diagnósticos alternativos con probabilidades

### Integración con Servicios Externos

- **Google Gemini AI**: Generación de explicaciones médicas contextualizadas
- **Google Text-to-Speech**: Conversión de explicaciones a audio
- **Google Maps API**: Localización de dermatólogos cercanos

## Frontend (Angular)

### Arquitectura de la Aplicación

La interfaz de usuario está desarrollada en Angular con TypeScript, implementando una arquitectura basada en componentes reutilizables y servicios compartidos.

**Componentes principales:**
- **Main Component**: Interfaz principal para carga y análisis de imágenes
- **Historial Component**: Visualización del historial de predicciones
- **Enfermedades Component**: Catálogo dinámico de afecciones detectables
- **Encontrar Dermatólogo Component**: Localización de especialistas

### Características de la Interfaz

**Análisis de imágenes:**
- Carga por drag & drop o selección manual
- Vista previa en tiempo real
- Validación de formatos (JPG, PNG)
- Indicadores de progreso durante el análisis

**Presentación de resultados:**
- Diagnóstico principal con porcentaje de confianza
- Top 3 condiciones alternativas ordenadas por probabilidad
- Explicación detallada generada por IA
- Lista de síntomas asociados obtenidos de la base de datos
- Reproducción de audio para accesibilidad

**Gestión de historial:**
- Visualización paginada de predicciones anteriores
- Información completa de cada análisis
- Navegación intuitiva y búsqueda

**Diseño responsive:**
- Adaptación automática a dispositivos móviles
- Interfaz optimizada para tablets y escritorio
- Uso de Tailwind CSS para consistencia visual

### Servicios de Angular

- **Prediccion Service**: Comunicación con API de análisis
- **Historial Service**: Gestión del historial de predicciones
- **Enfermedad Service**: Obtención de información médica
- **Google Maps Service**: Integración con servicios de ubicación

## Tecnologías Utilizadas

### Inteligencia Artificial y Machine Learning
- **PyTorch**: Framework principal para deep learning
- **EfficientNet**: Arquitectura de red neuronal convolucional
- **Torchvision**: Transformaciones y utilidades para imágenes
- **Scikit-learn**: Métricas de evaluación y utilidades
- **Pillow (PIL)**: Procesamiento de imágenes

### Backend
- **FastAPI**: Framework web moderno para APIs REST
- **SQLAlchemy**: ORM para gestión de base de datos
- **PostgreSQL**: Sistema de gestión de base de datos relacional
- **Pydantic**: Validación y serialización de datos
- **Google AI SDK**: Integración con servicios de Google

### Frontend
- **Angular 18**: Framework de desarrollo web
- **TypeScript**: Lenguaje de programación tipado
- **Tailwind CSS**: Framework de estilos utilitarios
- **RxJS**: Programación reactiva y manejo de observables
- **Font Awesome**: Biblioteca de iconos

### Herramientas de Desarrollo
- **Jupyter Notebook**: Desarrollo y experimentación del modelo
- **Git**: Control de versiones
- **VS Code**: Entorno de desarrollo integrado

## Instalación y Configuración

### Prerrequisitos del Sistema
- Python 3.11 o superior
- Node.js 18 o superior
- PostgreSQL 12 o superior
- Git

### Configuración del Backend

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/FepDev25/Proyecto-Final-Inteligencia-Artificial.git
   cd Proyecto-Final-Inteligencia-Artificial/backend
   ```

2. **Crear entorno virtual:**
   ```bash
   python -m venv fastapi-ml
   source fastapi-ml/bin/activate  # Linux/Mac
   # fastapi-ml\Scripts\activate   # Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   pip install efficientnet_pytorch
   ```

4. **Configurar base de datos:**
   ```bash
   # Crear base de datos PostgreSQL
   createdb dermascan
   
   # Ejecutar script de inserción
   cd ../db
   python ingresos.py
   ```

5. **Configurar credenciales:**
   - Colocar archivo de credenciales de Google en `backend/credentials/`
   - Configurar API keys en variables de entorno

6. **Ejecutar servidor:**
   ```bash
   cd ../backend
   python main.py
   ```

### Configuración del Frontend

1. **Navegar al directorio:**
   ```bash
   cd frontend/dermascan-front
   ```

2. **Instalar dependencias:**
   ```bash
   npm install
   ```

3. **Configurar environment:**
   ```typescript
   // src/app/environments/environment.ts
   export const environment = {
     production: false,
     apiUrl: 'http://127.0.0.1:8000',
     googleApiKey: 'YOUR_GOOGLE_API_KEY'
   };
   ```

4. **Ejecutar aplicación:**
   ```bash
   ng serve
   ```

5. **Acceder a la aplicación:**
   - Abrir navegador en `http://localhost:4200`

## Uso del Sistema

### Proceso de Análisis

1. **Carga de imagen**: El usuario selecciona o arrastra una imagen de la zona cutánea afectada
2. **Preprocesamiento**: La imagen se redimensiona y normaliza automáticamente
3. **Análisis con IA**: El modelo EfficientNet-B3 procesa la imagen y genera predicciones
4. **Consulta a base de datos**: Se obtienen síntomas y información médica asociada
5. **Generación de explicación**: Google Gemini crea una explicación contextualizada
6. **Presentación de resultados**: Se muestra el diagnóstico con información completa
7. **Almacenamiento**: Los resultados se guardan en el historial del usuario

### Interpretación de Resultados

**Diagnóstico principal:**
- Condición con mayor probabilidad según el modelo
- Porcentaje de confianza basado en la función softmax
- Descripción detallada y síntomas asociados

**Condiciones alternativas:**
- Top 3 diagnósticos con mayor probabilidad después del principal
- Ranking visual con barras de progreso
- Contexto sobre el total de condiciones analizadas

**Explicación médica:**
- Texto generado por IA con información contextual
- Audio opcional para accesibilidad
- Nota de responsabilidad médica

## Consideraciones Importantes

### Limitaciones del Sistema
- El sistema proporciona un análisis preliminar, no un diagnóstico médico definitivo
- La precisión puede variar según la calidad y características de la imagen
- Algunas condiciones pueden requerir evaluación clínica adicional
- El modelo está entrenado con datos específicos y puede no cubrir todas las variantes

### Recomendaciones de Uso
- Utilizar imágenes claras con buena iluminación
- Asegurar que el área afectada sea visible completamente
- Considerar los resultados como orientación inicial
- Consultar siempre con un dermatólogo para diagnóstico definitivo

### Aspectos Éticos y Legales
- El sistema incluye avisos claros sobre sus limitaciones
- Se recomienda supervisión médica profesional
- Los datos de análisis se manejan respetando la privacidad del usuario
- La aplicación cumple con principios de transparencia en IA

## Contribución y Desarrollo

### Estructura de Contribución
Para contribuir al proyecto, seguir las siguientes pautas:
- Fork del repositorio principal
- Crear rama de feature específica
- Implementar cambios con pruebas correspondientes
- Crear pull request con descripción detallada

### Testing y Calidad
- Pruebas unitarias para servicios críticos
- Validación de endpoints de API
- Testing de componentes de frontend
- Evaluación continua del modelo

## Contacto y Soporte

**Equipo de desarrollo:**
- Samantha Suquilanda
- Felipe Peralta
- Andres Torres
- Kevin Chipantiza

**Repositorio**: https://github.com/FepDev25/Proyecto-Final-Inteligencia-Artificial

Para reportar problemas o sugerir mejoras, utilizar el sistema de issues del repositorio de GitHub.
