from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length = 250)
    year = models.TextField(max_length = 4, null = True)
    color = models.TextField(max_length = 100, null = True)
    
    # El modelo __str__ permite mostrar en consola textualmente lo que queremos ver de la clase, en este caso podemos ver el título y el año sin ningún problema
    def __str__(self):
        return f"{self.color}, {self.title} - {self.year}"


class Publisher(models.Model):
    name = models.TextField(max_length = 200)
    address = models.TextField(max_length = 200)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.TextField(max_length = 200)
    birth_date = models.DateField()
    
    def __str__(self):
        return {'name':self.name, 'website': self.website, 'biography': self.biography}

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete = models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length = 500)

class Book(models.Model):
    title = models.TextField(max_length = 200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) # Relación entre modelos Book y Publisher.
                                                                        # Con ForeignKey podemos hacer esa relación con Publisher como primer parámetro
                                                                        # y on_delete que nos permite establecer que pasará si se borra el modelo Publisher en este case, también se borrará
    authors = models.ManyToManyField(Author, related_name = "authors")
    
    def __str__(self):
        return self.title