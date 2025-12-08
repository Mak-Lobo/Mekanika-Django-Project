from django.db import models

# Create your models here.

# feedback model
class FeedBack(models.Model):
    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]


    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)

    def __str__(self):
        return f"Feedback from {self.name} <{self.email}>"

# customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} has registered."
    


