from biblioteca.models import Autor, Libro, Resena
import random

# Autores

autor1 = Autor.objects.create(nombre="Gabriel García Marquez", nacionalidad = "Colombiano")
autor2 = Autor.objects.create(nombre="Juancho de la espriella", nacionalidad = "Colombiano")
autor3 = Autor.objects.create(nombre="Maduro Cabrales", nacionalidad = "Venezolano")
autor4 = Autor.objects.create(nombre="Jackie Chan", nacionalidad = "China")
autor5 = Autor.objects.create(nombre="Augusto Tinieblas", nacionalidad = "Argentino")


# Libros

libro1 = Libro.objects.create(
    titulo="Las ventanas del cielo",
    autor=autor1,
    fecha_publicacion="1988-10-22",
    resumen="Gran libro que nos cuenta la historia del paraiso."
)

libro2 = Libro.objects.create(
    titulo="Sombras en la biblioteca",
    autor=autor2,
    fecha_publicacion="1991-07-14",
    resumen="Una extraña presencia ronda la biblioteca después del anochecer."
)

libro3 = Libro.objects.create(
    titulo="El misterio del libro perdido",
    autor=autor3,
    fecha_publicacion="2003-03-11",
    resumen="Un bibliotecario debe encontrar un libro perdido antes de que sea demasiado tarde."
)

libro4 = Libro.objects.create(
    titulo="Historias de un lector nocturno",
    autor=autor4,
    fecha_publicacion="2015-09-27",
    resumen="Relatos de un lector que encuentra respuestas a su vida en los libros."
)

libro5 = Libro.objects.create(
    titulo="Crónicas del archivo prohibido",
    autor=autor5,
    fecha_publicacion="1999-01-08",
    resumen="Una sala secreta guarda textos que nunca debieron ser leídos."
)

libro6 = Libro.objects.create(
    titulo="La última página",
    autor=autor1,
    fecha_publicacion="2007-12-04",
    resumen="La vida de un escritor cambia al terminar su última novela."
)

libro7 = Libro.objects.create(
    titulo="Secretos entre estanterías",
    autor=autor2,
    fecha_publicacion="2020-05-19",
    resumen="Entre estantes polvorientos se esconden secretos familiares."
)

libro8 = Libro.objects.create(
    titulo="El guardián de los libros",
    autor=autor3,
    fecha_publicacion="1995-11-03",
    resumen="Un joven descubre su destino al ser nombrado guardián de una biblioteca."
)

libro9 = Libro.objects.create(
    titulo="Relatos de tinta y papel",
    autor=autor4,
    fecha_publicacion="2012-04-16",
    resumen="Cuentos cortos sobre lectores y sus libros favoritos."
)

libro10 = Libro.objects.create(
    titulo="Cartas desde el silencio",
    autor=autor5,
    fecha_publicacion="2000-02-28",
    resumen="Cartas antiguas revelan una historia de amor olvidada."
)

libro11 = Libro.objects.create(
    titulo="El códice olvidado",
    autor=autor1,
    fecha_publicacion="1984-08-17",
    resumen="Un códice antiguo pone en peligro a quien lo lee."
)

libro12 = Libro.objects.create(
    titulo="La pluma y el destino",
    autor=autor2,
    fecha_publicacion="2019-06-05",
    resumen="La pluma de un autor decide cambiar el final de su historia."
)

libro13 = Libro.objects.create(
    titulo="Memorias de una biblioteca antigua",
    autor=autor3,
    fecha_publicacion="1990-03-24",
    resumen="Una biblioteca antigua guarda la memoria de sus visitantes."
)

libro14 = Libro.objects.create(
    titulo="La sombra del escritor",
    autor=autor4,
    fecha_publicacion="2018-10-30",
    resumen="Un escritor anónimo deja pistas en los márgenes de los libros."
)

libro15 = Libro.objects.create(
    titulo="Los susurros del papel",
    autor=autor5,
    fecha_publicacion="2021-07-12",
    resumen="Se dice que algunos libros susurran a quienes los leen de noche."
)

libro16 = Libro.objects.create(
    titulo="El índice infinito",
    autor=autor1,
    fecha_publicacion="1994-09-09",
    resumen="Un índice interminable que guía a un libro imposible."
)

libro17 = Libro.objects.create(
    titulo="Las crónicas del lector errante",
    autor=autor1,
    fecha_publicacion="2009-12-22",
    resumen="Un lector recorre el mundo buscando una historia perfecta."
)

libro18 = Libro.objects.create(
    titulo="La biblioteca encantada",
    autor=autor1,
    fecha_publicacion="2010-01-13",
    resumen="Se rumorea que algunos libros cambian de contenido cada luna llena."
)

libro19 = Libro.objects.create(
    titulo="Ecos de historias pasadas",
    autor=autor4,
    fecha_publicacion="2005-04-25",
    resumen="Las historias del pasado resuenan en cada rincón de la biblioteca."
)

libro20 = Libro.objects.create(
    titulo="El libro de los caminos",
    autor=autor2,
    fecha_publicacion="1997-08-02",
    resumen="Un libro misterioso que muestra distintos caminos según el lector."
)

libros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10,
          libro11, libro12, libro13, libro14, libro15, libro16, libro17, libro18, libro19, libro20]

# Resenas

resenas = {1:"Muy malo", 2:"Malo", 3:"Regular", 4:"Bueno", 5:"Excelente"}

for i in range(100):
    ind_libro = random.randint(0,19)
    valor_calificacion = random.randint(1,5)
    ResenaX = Resena.objects.create(libro=libros[ind_libro], texto=resenas[valor_calificacion], calificacion=valor_calificacion)
