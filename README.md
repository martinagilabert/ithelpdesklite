# IT Helpdesk Lite para Odoo 18

**IT Helpdesk Lite** es un módulo personalizado para Odoo 18 diseñado para gestionar las incidencias y peticiones de soporte técnico (IT) de una empresa de forma ágil y sencilla.

## 🚀 Características Principales

* **Gestión de Tickets:** Creación y seguimiento de incidencias de soporte técnico.
* **Secuencias Automáticas:** Generación automática de referencias únicas para cada ticket (ej. `TICKET/0001`).
* **Vista Kanban Interactiva:** Gestión visual de los tickets arrastrándolos entre diferentes estados (Nuevo, En Proceso, Resuelto, Cancelado).
* **Vistas Optimizadas para Odoo 18:** Uso de la etiqueta `<list>` (reemplazando al antiguo `<tree>`) y configuración de columnas invisibles (`column_invisible`).
* **Asignación Rápida:** Botón "Asignarme" (`action_assign_me`) para que un técnico se asigne rápidamente un ticket con un solo clic.
* **Filtros Personalizados:** Búsqueda rápida de "Mis Tickets" y "Tickets Vencidos" (calculado dinámicamente según la fecha límite).
* **Reglas de Validación:** Restricción (Constraint) de Python que impide cerrar un ticket si no se ha rellenado una descripción o solución.

## 🔐 Seguridad y Permisos

El módulo incluye un archivo de seguridad (`helpdesk_security.xml`) que divide a los usuarios en dos niveles:
1. **Usuario Helpdesk:** Permisos básicos para crear y leer tickets.
2. **Manager Helpdesk:** Permisos totales sobre el módulo, configuración de estados y borrado de tickets.

## 🛠️ Estructura Técnica del Módulo

* `models/`: Contiene la lógica de negocio en Python (`it_ticket.py`, `it_ticket_stage.py`). Incluye adaptación a Odoo 18 para la expansión de grupos en Kanban (uso del parámetro `order`).
* `views/`: Vistas XML (Formulario, Lista, Kanban, Búsqueda) y definición de los menús (`it_ticket_views.xml`, `menu_views.xml`).
* `security/`: Definición de grupos de acceso y reglas de registro (CSV).
* `data/`: Datos de demostración o configuración inicial (Secuencias automáticas y Estados por defecto).

## 📦 Instalación

1. Copia la carpeta `helpdesk_lite` en tu directorio de addons personalizados (ej. `custom_addons/`).
2. Reinicia el servidor de Odoo.
3. Activa el **Modo Desarrollador** en Odoo.
4. Ve a **Aplicaciones**, haz clic en **Actualizar lista de aplicaciones**.
5. Busca `IT Helpdesk Lite` e instálalo.
 *(Nota: Si no aparece a simple vista, quita el filtro "Apps" en la barra de búsqueda).*

## 💡 Uso Básico

1. Ve al menú principal y selecciona **IT Helpdesk**.
2. Haz clic en **Nuevo** para registrar una incidencia.
3. Rellena los datos básicos (el número de referencia se generará al guardar).
4. Usa la vista Kanban para avanzar el estado del ticket según progresa la resolución.
