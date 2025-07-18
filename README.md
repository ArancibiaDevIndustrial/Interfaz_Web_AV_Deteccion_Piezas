# **Interfaz Web con Visión Artificial para Detección y Conteo de Piezas**  

**Proyecto basado en OpenCV y Flask para la detección de piezas de color rojo en una cinta transportadora, con visualización de resultados en una interfaz web en tiempo real.**  

---

## **Características Principales**  
- **Detección de piezas rojas**: Utiliza técnicas avanzadas de procesamiento de imágenes con OpenCV para identificar piezas de color rojo en movimiento.  
- **Zona de conteo definida**: Implementa un área específica de detección para contar únicamente las piezas que cruzan la región de interés.  
- **Transmisión en tiempo real**: Muestra el video procesado directamente en la interfaz web con anotaciones de detección.  
- **Dashboard interactivo**: Incluye gráficos dinámicos generados con Chart.js para visualizar métricas de producción actualizadas en tiempo real.  
- **Backend eficiente**: Desarrollado con Flask para gestionar las solicitudes web y el procesamiento de datos.  

---

## **Estructura del Proyecto**  
```
/mi_dashboard
│── /static
│   └── /css
│       └── style.css       # Archivos CSS para estilización de la interfaz
│── /templates
│   └── index.html          # Plantilla HTML principal del dashboard
│── app.py                  # Lógica principal del backend (Flask y OpenCV)
│── requirements.txt        # Dependencias del proyecto (Python)
│── README.md               # Documentación técnica
```

---

## **Instalación y Configuración**  
### **Requisitos previos**  
- Python 3.8 o superior  
- Gestor de paquetes Pip  

### **Pasos de instalación**  
1. Clonar el repositorio:  
   ```sh
   git clone https://github.com/ArancibiaDevIndustrial/Interfaz_Web_AV_Deteccion_Piezas.git
   cd Interfaz_Web_AV_Deteccion_Piezas
   ```  
2. Instalar dependencias:  
   ```sh
   pip install -r requirements.txt
   ```  

---

## **Ejecución del Sistema**  
Inicie el servidor Flask ejecutando:  
```sh
python app.py
```  
Acceda a la interfaz desde un navegador web en:  
```
http://127.0.0.1:5000/
```  

---

## **Demostración Visual**  
- **Vista de la cámara procesada**: Con superposición de áreas de detección y conteo.
<img width="1365" height="678" alt="Screenshot 2025-02-16 065535" src="https://github.com/user-attachments/assets/9e5b970a-e964-4efc-b27b-a809eaf021b6" />

- **Dashboard operativo**: Gráficos de producción, historial de conteo y estadísticas.  
<img width="677" height="599" alt="Screenshot 2025-02-16 065552" src="https://github.com/user-attachments/assets/5c075716-f48a-4482-9620-7a438e02fc08" />

---

## **Tecnologías Implementadas**  
- **Lenguaje**: Python 3  
- **Procesamiento de imágenes**: OpenCV  
- **Framework web**: Flask  
- **Visualización de datos**: Chart.js  
- **Frontend**: HTML5, CSS3, JavaScript  

---

## **Roadmap y Mejoras Planificadas**  
- **Persistencia de datos**: Integración con bases de datos (SQLite/PostgreSQL) para almacenar historiales de producción.  
- **Detección multicriterio**: Extender la solución para reconocer piezas por color, forma o tamaño.  
- **Monitoreo remoto**: Conexión con plataformas IoT para acceso en tiempo real desde dispositivos externos.  

---

## **Contribuciones**  
Se aceptan contribuciones bajo el siguiente flujo:  
1. Realice un *fork* del repositorio.  
2. Cree una rama para su feature: `git checkout -b nombre-de-la-funcionalidad`.  
3. Envíe un *Pull Request* con una descripción detallada de los cambios.  

---

## **Licencia**  
Distribuido bajo licencia MIT. Consulte el archivo `LICENSE` para términos completos.  

---

## **Contacto**  
Para consultas técnicas o colaboraciones:  
- **Correo**: arancibia.dev@outlook.com  
- **GitHub**: @ArancibiaDevIndustrial  

---
