from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser
# Create your models here.


class CategoryFootwears(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_footwears'

    def __str__(self):
        return self.name


class Footwears(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(CategoryFootwears, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='footwers/', default='')
    country = models.CharField(max_length=100)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'footwears'

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return f'{self.company_name}'


class FootwearCompany(models.Model):
    footwear = models.ForeignKey(Footwears, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'footwear_company'

    def __str__(self):
        return f'{self.footwear.name} - {self.company.company_name}'


class Review(models.Model):
    comment = models.CharField(max_length=200)
    star_given = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    footwear = models.ForeignKey(Footwears, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table ='review'

    def __str__(self):
        return f'{self.star_given} - {self.footwear.name} - {self.user.username}'

class DetailInfo(models.Model):
    first_name = models.CharField(max_length=100)
    footwears = models.ForeignKey(Footwears, on_delete=models.CASCADE)

    class Meta:
        db_table = 'detail_info'
