from django.db import models

# Create your models here.

class Season(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=200, default='ROHO')

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    upc = models.CharField(max_length=200, null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default='ROHO', blank=True)
    description = models.TextField(blank=True, null=True)
    qty = models.IntegerField(default=0, null=True, blank=True)
    request_date = models.DateField(null=True, blank=True)
    request_name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    participants = models.ManyToManyField(Participant, blank=True, null=True)
    organizer_email = models.EmailField(null=True, blank=True, default='lucasmatthews@hotmail.com')


    def __str__(self):
        return f'{self.title} - {self.slug}' 
        