### Info de la Materia: Topicos Especiales en Telematica-st0263

### Estudiantes:
- Miguel Angel Martinez Florez, mamartinef@eafit.edu.co
- Mateo Muñoz Cadavid, mmunozc4@eafit.edu.co

### Profesor:  Edwin Nelson Montoya Munera, emontoya@eafit.edu.co  

# Proyecto 1: Sistema de Archivos Distribuidos

## 1. Breve descripción de la actividad:
Este proyecto presenta el diseño e implementación de un Sistema de Archivos Distribuidos (DFS) minimalista, enfocado en ofrecer una solución eficiente para compartir y acceder de 
forma concurrente a un conjunto de archivos almacenados en diferentes nodos. Inspirado por sistemas consolidados como NFS (Network File System), AFS (Andrew File System), y SMB 
(Server Message Block), este DFS adopta un enfoque intermedio entre los sistemas basados en bloques y los basados en objetos, integrando la flexibilidad del acceso a bloques con 
la eficiencia y la simplicidad del modelo WORM (Write Once, Read Many), característico de los sistemas de almacenamiento por objetos como AWS S3.

### 1.1 Motivación 
El proyecto surge de la necesidad de comprender y aplicar los conceptos fundamentales de los sistemas de archivos distribuidos en un contexto práctico y actual. Frente a la creciente 
demanda de sistemas capaces de manejar grandes volúmenes de datos de manera eficiente, segura y escalable, este proyecto busca explorar las capacidades de un DFS minimalista que
combine lo mejor de los mundos de almacenamiento basado en bloques y en objetos, ofreciendo una alternativa robusta para el almacenamiento y acceso distribuido de archivos.

### 1.2 Caracteristicas
- **Basado en Bloques con Enfoque WORM:** Aprovecha la eficiencia del almacenamiento por bloques y la simplicidad del enfoque WORM para optimizar el acceso y la gestión de datos.
- **Replicación y Distribución de Datos:** Implementa un algoritmo para la distribución y replicación de bloques, asegurando que cada bloque se almacene en al menos dos DataNodes para la tolerancia a fallos.
- **Comunicaciones Eficientes:** Utiliza dos tipos de protocolos, el Canal de Control y el Canal de Datos, para manejar las operaciones entre los clientes y DataNodes, así como entre los diferentes componentes del sistema.
- **Integración Transparente:** Aunque el sistema se orienta principalmente hacia la replicación y distribución basada en bloques, ofrece una transparencia similar a la de los sistemas operativos en el acceso a archivos, tanto locales como remotos.
- **Optimización de Recursos:** El NameNode desempeña un papel crucial en la selección de DataNodes para la escritura de archivos, basándose en criterios de optimización para mejorar el rendimiento y la eficiencia.

- ## 2. Informe general de Diseño de Alto Nivel, Arquitectura, Patronesy Mejores prácticas utilizadas
El diseño de nuestro Sistema de Archivos Distribuidos Minimalista sigue un enfoque modular y escalable, priorizando la eficiencia, la robustez y la facilidad de mantenimiento. A continuación, se describen los componentes principales del diseño, 
la arquitectura general y las metodologías aplicadas:

### Arquitectura y Componentes Principales
- **Cliente (client.py):** Interfaz para la interacción del usuario con el sistema de archivos distribuidos. Implementa funcionalidades para la escritura y lectura de archivos, interactuando directamente con los DataNodes a través de los protocolos definidos.
- **GRPC Server (grpc_server.py):** Facilita la comunicación entre los diferentes nodos del sistema utilizando gRPC, un marco de comunicación de alto rendimiento desarrollado por Google. Permite una comunicación eficiente, segura y escalable entre clientes y servidores, así como entre los servidores mismos.
- **Message-Oriented Middleware (MOM) Server (mom_server.py):** Utiliza un enfoque basado en mensajes para la gestión de comunicaciones, soportando así una arquitectura orientada a servicios y la desacoplamiento de componentes. Este enfoque mejora la escalabilidad y la flexibilidad del sistema.
- **Configuración (config_file.py):** Centraliza la configuración del sistema, facilitando su adaptación y escalabilidad. Almacenar la configuración de forma centralizada permite ajustes rápidos y coherentes en todo el sistema.
- **Gestión de Archivos (data_files.py):** Encargado de la gestión de los bloques de datos, incluyendo su creación, almacenamiento, y recuperación. Implementa el algoritmo de distribución y replicación de datos, asegurando su disponibilidad y tolerancia a fallos.
- **Main (main.py):** Punto de entrada principal del sistema, coordina la inicialización y la interacción entre los diferentes componentes del sistema.

### Patrones de Diseño y Mejores Prácticas
- **Microservicios:** Cada componente del sistema funciona como un microservicio independiente, facilitando la escalabilidad horizontal y la mantenibilidad del sistema.
- **Comunicaciones basadas en gRPC y MOM:** Estos enfoques modernos para la comunicación entre procesos permiten una alta eficiencia y fiabilidad en las operaciones distribuidas, además de ofrecer compatibilidad con múltiples lenguajes de programación.
- **Configuración Externa:** La externalización de la configuración permite una mayor flexibilidad y facilita las operaciones en diferentes entornos sin necesidad de modificar el código fuente.
- **Separación de responsabilidades:** Cada módulo del sistema se centra en una única responsabilidad, siguiendo el principio de responsabilidad única. Esto simplifica el desarrollo, las pruebas y el mantenimiento del sistema.
- **Robustez y Tolerancia a Fallos:** La implementación de replicación de datos y la selección cuidadosa de DataNodes para almacenamiento garantizan la disponibilidad y la integridad de los datos.

- ## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones:
  El desarrollo de este Sistema de Archivos Distribuidos Minimalista se ha llevado a cabo utilizando tecnologías modernas y probadas para garantizar un rendimiento óptimo, facilidad de
  mantenimiento y alta escalabilidad. A continuación, se detalla el entorno de desarrollo y técnico:

  ### Lenguaje de Programación
- **Python:** La elección de Python como lenguaje principal se debe a su simplicidad, flexibilidad y el amplio ecosistema de librerías disponibles. Este proyecto se ha desarrollado utilizando Python 3.8 o superior, aprovechando sus características más
  recientes para el manejo asincrónico y la tipificación estática.

  ### Librerias y Paquetes 
- **gRPC:** Utilizado para la implementación de los servidores gRPC, permitiendo la comunicación entre los distintos componentes del sistema de una manera eficiente y con soporte para múltiples lenguajes de programación.
  - Versión: Se recomienda utilizar gRPC 1.30.0 o superior.
- **Protocol Buffers (protobuf):** Usado en conjunto con gRPC para la definición de los protocolos de comunicación entre servicios. Protocol Buffers ofrece un mecanismo extensible para la serialización de datos estructurados.
  - Versión: Acorde con la versión de gRPC utilizada, generalmente se incluye con gRPC.
- **Flask (opcionalmente para APIs REST):** En caso de que el proyecto utilice REST para algún componente de comunicación, Flask es una elección común por su simplicidad y flexibilidad para desarrollar APIs web en Python.
  - Versión: 1.1.2 o superior.
- **RabbitMQ (para MOM server):** Como intermediario de mensajes para implementar el patrón de Message-Oriented Middleware (MOM), RabbitMQ es una opción robusta y escalable para manejar comunicaciones basadas en mensajes dentro del sistema.
  - Versión: 3.8 o superior.
- **Pika (Cliente RabbitMQ para Python):** Utilizado para la integración con RabbitMQ desde el lado del cliente Python.
  - Versión: 1.1.0 o superior.

### Herramientas de Desarrollo 
- **Git:** Para el control de versiones y colaboración en el desarrollo.
- **Virtualenv o Conda:** Para la gestión de entornos virtuales y dependencias, asegurando que las librerías y sus versiones específicas estén aisladas y sean consistentes entre los entornos de desarrollo y producción.

