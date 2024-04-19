from django.db import models

class Speciality(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="course/speciality")
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"


class Course(models.Model):
    class PriceType(models.Model):
        choices = None
        s = "USD", "$"
        sum = "UZS", "so'm"

    title = models.TextField(max_length=50)
    description = models.TextField()
    active_users = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    price_type = models.CharField(max_length=10, choices=PriceType.choices, default=PriceType.sum)
    reyting = models.FloatField()
    speciality = models.ManyToManyField(Speciality)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

class Position(models.Model):
    name = models.CharField(max_length=100)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="course/teacher")
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    x_link = models.URLField(null=True, blank=False)
    m_link = models.URLField(null=True, blank=False)
    l_link = models.URLField(null=True, blank=False)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"