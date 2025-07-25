from django.db import models




class Library_literature(models.Model):
    name = models.CharField(max_length=100, blank=False)
    number = models.IntegerField(primary_key=True)
    description = models.TextField(blank=False, help_text="Write a short description of the book.")
    genre = models.CharField(blank=False)
    publication_date = models.DateField(blank=False)
    author = models.CharField(blank=False)


class Student_Cart(models.Model):
    number_cart = models.IntegerField(primary_key=True)
    date_of_issue = models.DateField(blank=False, auto_now_add=True)
    end_date = models.DateField(blank=False)

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    student_card_number = models.OneToOneField(Student_Cart, on_delete=models.CASCADE, related_name="student")
    mail = models.EmailField(blank=False)
    specialty = models.CharField(max_length=70)

class Student_group(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="students_group", verbose_name='students')
    group_name = models.CharField(max_length=25, blank=False)
    group_slogan = models.TextField(blank=False)
    meeting_group = models.IntegerField(blank=False)

class Process_of_taking_book(models.Model):
    taker = models.ForeignKey(Student_Cart, on_delete=models.CASCADE, related_name="students_taker")
    literature = models.ForeignKey(Library_literature, on_delete=models.CASCADE, related_name="literatures")
    date_of_giving = models.DateField(blank=False)
    full_name_issued = models.CharField(blank=False)



class UniversitySport(models.Model):
    sport_name = models.CharField(blank=False, max_length=100)


    def __str__(self):
        return self.sport_name


class Sportsman(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    sport = models.ForeignKey(UniversitySport, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.student.name} - {self.sport}"



class University_Competitions(models.Model):
    name_competitions = models.CharField(blank=False, max_length=100)
    sport = models.OneToOneField(UniversitySport, on_delete=models.CASCADE)
    sportsman = models.ManyToManyField(Sportsman)
    date_start = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.name_competitions}  {self.sport} - {self.date_start}"









