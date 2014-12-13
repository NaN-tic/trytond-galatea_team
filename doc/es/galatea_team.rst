.. inheritref:: galatea_team/galatea:section:equipo_empleados

------------------
Equipo o empleados
------------------

Esta App dispone la funcionalidad de la generación de fichas de cada empleado o
col·laborador de su empresa (el equipo). En muchos sitios web se publican la ficha
de cada empleado con su fotografia (o avatar) y una descripcion de su trayectoria profesional.

Para la gestión de empleados accede a |menu_galatea_team|. Como todo registro
web deberá tener en cuenta:

* Slug: Es el ID o clave del vuestro registro. Sólo debe usar los carácteres az09-
  (sin acentos ni espacios). Este campo debe ser único ya que no pueden haber más
  de dos o más slugs en sus empleados. Recuerde que es un campo multi idioma.
  Cuando introduzca un título se le propone un slug a partir del título que después
  lo podrá cambiar. Un slug podría ser 'mi-articulo-sobre-tryton' y crearia una dirección como
  http://www.midominio.com/es/equipo/raimon-esteve
* SEO MetaKeyword. Introduce las palabras clave de su artículo separados por comas
  (no más de 155 carácteres) que se usará para los buscadores. Un ejemplo de MetaKeyword
  podría ser "tryton,diseñador,programador". Recuerde que es un campo multi idioma.
* SEO MetaDescription. Introduce una descripción breve del artículo (el resumen)
  (no más de 155 carácteres) que se usará para los buscadores. Un ejemplo de MetaDescription
  podria ser "Diseñador y programador de Zikzakmedia". Recuerde que es un
  campo multi idioma.
* SEO MetaTitle. Si el título del artículo en los buscadores desea que sea diferente del nombre
  del empleado puede usar este campo para cambiarlo. Recuerde que es un campo multi idioma.

Para el contenido de un empleado puede usar los campos descripciones. Usa el campo "Descripción larga"
para descripciones con contenido extenso. Para el formato HTML usa los tags de Wiki para dar formato a su contendido.
Los tags de wiki le permite formatear el texto para después sea mostrado con HTML. Para
información de los tags de wiki puede consultar `MediaWiki <http://meta.wikimedia.org/wiki/Help:Editing>`_

Como siempre recuerde que si edita un empleado y su web es multi idioma, debe de cambiar
el contenido por cada idioma con el campo de la "bandera".

Para acceder a un empleado en concreto accede a:

* Español: http://www.midominio.com/es/equipo/<SLUG>
* Catalan: http://www.midominio.com/ca/equip/<SLUG>
* Inglés: http://www.midominio.com/en/team/<SLUG>

.. inheritref:: galatea_team/galatea:section:todos_empleados

Todos los empleados
-------------------

Como toda app dispone de un listado de todos los empleados. Estos siempre
se listaran por el nombre en orden descendiente.

Para acceder a todos los empleados accede a:

* Español: http://www.midominio.com/es/equipo/
* Catalan: http://www.midominio.com/ca/equip/
* Inglés: http://www.midominio.com/en/team/

.. |menu_galatea_team| tryref:: galatea_team.menu_galatea_team/complete_name
