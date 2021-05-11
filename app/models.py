from django.db import models


class PizzaType(models.Model):
  types = models.CharField(primary_key=True, max_length=50)

  def __str__(self):
    return f'{self.types}'

  class Meta:
    verbose_name_plural = 'PizzaType'


class SizeType(models.Model):
  sizes = models.CharField(primary_key=True, max_length=50)

  def __str__(self):
    return f'{self.sizes}'

  class Meta:
    verbose_name_plural = 'SizeType'


class ToppingType(models.Model):
  toppings = models.CharField(primary_key=True, max_length=50)

  def __str__(self):
    return f'{self.toppings}'

  class Meta:
    verbose_name_plural = 'ToppingType'

class Pizza(models.Model):
  type = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
  size = models.ForeignKey(SizeType, on_delete=models.CASCADE)
  topping = models.ManyToManyField(ToppingType)

  def __str__(self):
    return f'{self.type} : {self.size} : {self.topping}'

  class Meta:
    verbose_name_plural = 'Pizza'