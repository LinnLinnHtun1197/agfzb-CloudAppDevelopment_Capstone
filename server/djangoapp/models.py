from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='BMW 2023')
    description = models.CharField(null=False, max_length=30, default='BMW 2023 is new model in 2023')
    price = models.IntegerField(null=True)
    
    # Create a toString method for object string representation
    def __str__(self):
        return self.name + " " + self.description + " " + self.price


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    # Many-To-Many relationship with CarMake
    carmake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100, default='BMW')
    dealerid = models.IntegerField(null=False)
    type = models.CharField(max_length=200, default="Sedan")
    year = models.DateField(null=True)

    def __str__(self):
        return "Name: " + self.name + "," + \
            "type: " + self.type


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

