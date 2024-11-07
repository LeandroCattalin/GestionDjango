GestionDjango - Gestión de Alumnos y Notas

Bienvenidos al proyecto GestionDjango. Esta aplicación fue desarrollada como parte de un proyecto académico por un equipo de estudiantes de programación con experiencia en otros lenguajes, como VB 6.0, C#, y más. Nuestro objetivo es modernizar una antigua aplicación de gestión de alumnos desarrollada en VB 6.0 y adaptarla a un entorno web utilizando el framework Django.
Descripción

GestionDjango es una herramienta web que permite a las universidades gestionar las notas y los datos personales de los estudiantes de manera eficiente. La aplicación está pensada para ser una solución moderna y flexible, con una interfaz amigable, fácil de usar y completamente funcional.

El sistema permite:

    Gestionar los datos personales de los estudiantes.
    Registrar y actualizar las notas de los estudiantes.
    Verificar y modificar el historial académico de cada alumno.
    Consultar los detalles de las materias y asignaturas cursadas.

Características

    Interfaz moderna y responsiva: Diseñada con HTML, CSS y JavaScript para ser accesible en dispositivos móviles y de escritorio.
    Backend robusto: Usamos Django para manejar el backend y las interacciones con la base de datos.
    Autenticación de usuarios: Sistema de autenticación para administrar diferentes niveles de acceso.
    CRUD completo: Funcionalidades para crear, leer, actualizar y eliminar datos de estudiantes y notas.
    Base de datos optimizada: Utiliza una base de datos SQLite para el almacenamiento local, con planes de migración a bases de datos más grandes según sea necesario.

Tecnologías Utilizadas

    Frontend:
        HTML5
        CSS3 (con un diseño responsivo)
        JavaScript (para funcionalidades interactivas)
    Backend:
        Python
        Django Framework
    Base de Datos:
        SQLite (para pruebas)
        Posible migración futura a PostgreSQL o MySQL

Equipo de Desarrollo

Somos un grupo de estudiantes con experiencia en diversos lenguajes de programación. Aunque estamos empezando en Django, contamos con experiencia en otros lenguajes como VB 6.0, C#, y JavaScript. Esta es nuestra primera incursión seria en el desarrollo web, y este proyecto nos ha permitido mejorar nuestras habilidades y aprender nuevas tecnologías.
Estado del Proyecto

Este proyecto es una modernización de una aplicación previamente construida en VB 6.0 para gestionar datos y notas de alumnos de manera local. Hemos decidido utilizar Django para el backend, ya que ofrece una gran flexibilidad, rapidez y robustez para aplicaciones web.
Instrucciones de Instalación

Para empezar a trabajar con esta aplicación, sigue los pasos a continuación:

    Clona el repositorio:

git clone https://github.com/usuario/GestionDjango.git
cd GestionDjango

Instala las dependencias:

Asegúrate de tener Python 3.x instalado. Luego, crea un entorno virtual y activa el entorno:

python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate

Instala los requisitos:

pip install -r requirements.txt

Migrate la base de datos:

python manage.py migrate

Inicia el servidor de desarrollo:

    python manage.py runserver

    Accede a la aplicación desde tu navegador en http://127.0.0.1:8000.

Colaborar

Si deseas contribuir a este proyecto, ¡serás muy bienvenido! Puedes hacerlo de la siguiente manera:

    Forkea el repositorio.
    Crea una rama para tu funcionalidad (usando git checkout -b feature/nueva-funcionalidad).
    Haz tus cambios y súbelos a tu repositorio.
    Envía un pull request explicando los cambios realizados.

Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

¡Gracias por visitar nuestro proyecto! Si tienes alguna pregunta, no dudes en abrir un issue en este repositorio.
