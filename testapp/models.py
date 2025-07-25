from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    page = models.PositiveIntegerField()
    published_date = models.DateField()

    def str(self):
        return f"{self.title} by {self.author}"



class Author(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    year_of_birth = models.DateField(verbose_name="Date of birth")
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")