from django.db import models

# Create your models here.
class Book(models.Model):
    books1 = (
        ('hb','hobbit'),
        ('lotr','lords of the ring')
    )
    title = models.CharField(max_length = 500,choices=books1)
    description = models.TextField(max_length=256, blank=True)

    price = models.DecimalField(default=0, max_digits =3, decimal_places=2)

    published = models.DateField(blank=True,null=True,default=None)
    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/',blank =True)

    def __str__(self):
        return self.title
