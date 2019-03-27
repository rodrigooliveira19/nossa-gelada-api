from django.db import models

# Create your models here.


class Estabelecimento(models.Model):
	descricao = models.CharField(max_length=30)  

	def __str__(self):
		return self.descricao



class Marca(models.Model):
	descricao = models.CharField(max_length=20)  

	def __str__(self):
		return self.descricao


class Unidade(models.Model):
	descricao = models.CharField(max_length=7)  

	def __str__(self):
		return self.descricao



class Filtro(models.Model):
	descricao = models.CharField(max_length=15)  

	def __str__(self):
		return self.descricao