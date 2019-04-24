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


class Cesta(models.Model):
	descricao = models.CharField(max_length=20)  
	estabelecimento = models.CharField(max_length=20) 

	def __str__(self):
		return self.descricao


class ItemCesta(models.Model): 
	marca = models.CharField(max_length=20) 
	unidade = models.CharField(max_length=7) 
	filtro = models.CharField(max_length=15) 
	valor = models.FloatField(); 
	cesta_id = models.ForeignKey("Cesta",related_name='itens',on_delete=models.CASCADE)

	def __str__(self):
		return self.marca