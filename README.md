# Café Express — PIA Fundamentos de Desarrollo Web

Proyecto académico desarrollado con Django.

## Requisitos
- Python 3.11 o superior
- Internet para cargar Bootstrap e imagen del hero

## Instalación
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Panel administrativo
http://127.0.0.1:8000/admin/

Desde el administrador puedo agregar noticias solo que se me fue la luz y no pude ponerlas a la hora de subir el pia ._.

## Puntos del PIA cubiertos
- Sitio completo con Django.
- Front End HTML + CSS + Bootstrap.
- Back End Python/Django.
- Validación y almacenamiento de formulario de contacto.
- Página de inicio.
- Quiénes somos.
- Blog/Noticias.
- Menú superior.
- Datos dinámicos desde base de datos relacional SQLite.
