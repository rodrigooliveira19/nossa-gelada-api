from rest_framework import serializers 
from cerveja import models



class EstabelecimentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Estabelecimento
		fields = ('id','descricao',)
		depth = 1 



class MarcaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Marca
		fields = ('id','descricao',)
		depth = 1 



class UnidadeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Unidade
		fields = ('id','descricao',)
		depth = 1 


class FiltroSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Filtro
		fields = ('id','descricao',)
		depth = 1 
