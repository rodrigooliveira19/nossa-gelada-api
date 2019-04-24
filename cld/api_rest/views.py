from django.shortcuts import render
from cerveja import models 
from api_rest import serializers
from rest_framework import generics

from rest_framework.views import APIView 
from rest_framework.response import Response


# Create your views here.

#GET
class EstabelecimentoListServiceView(generics.ListCreateAPIView):
	queryset = models.Estabelecimento.objects.all()
	serializer_class = serializers.EstabelecimentoSerializer


class MarcaListServiceView(generics.ListCreateAPIView):
	queryset = models.Marca.objects.all()
	serializer_class = serializers.MarcaSerializer


class UnidadeListServiceView(generics.ListCreateAPIView):
	queryset = models.Unidade.objects.all()
	serializer_class = serializers.UnidadeSerializer



class FiltroListServiceView(generics.ListCreateAPIView):
	queryset = models.Filtro.objects.all()
	serializer_class = serializers.FiltroSerializer


class CestaListServiceView(generics.ListCreateAPIView):
	queryset = models.Cesta.objects.all()
	serializer_class = serializers.CestaSerializer

class ItemCestaListServiceView(generics.ListCreateAPIView):
	queryset = models.ItemCesta.objects.all()
	serializer_class = serializers.ItemCestaSerializer



#Post
class CadastrarEstabelecimentoServiceView(APIView):

	def post(self,request,format=None):

		descricao = request.data.get('descricao')
		
		estabelecimento = models.Estabelecimento.objects.create(descricao = descricao)

		serializer = serializers.EstabelecimentoSerializer(estabelecimento)
		return Response(serializer.data)



class CadastrarMarcaServiceView(APIView):

	def post(self,request,format=None):

		descricao = request.data.get('descricao')
		
		marca = models.Marca.objects.create(descricao = descricao)

		serializer = serializers.MarcaSerializer(marca)
		return Response(serializer.data)



class CadastrarUnidadeServiceView(APIView):

	def post(self,request,format=None):

		descricao = request.data.get('descricao')
		
		unidade = models.Unidade.objects.create(descricao = descricao)

		serializer = serializers.UnidadeSerializer(unidade)
		return Response(serializer.data)


class CadastrarFiltroServiceView(APIView):

	def post(self,request,format=None):

		descricao = request.data.get('descricao')
		
		filtro = models.Filtro.objects.create(descricao = descricao)

		serializer = serializers.UnidadeSerializer(filtro)
		return Response(serializer.data)


class CadastrarCestaServiceView(APIView):

	def post(self,request,format=None):

		descricao = request.data.get('descricao')
		estabelecimento = request.data.get('estabelecimento')
		
		cesta = models.Cesta.objects.create(descricao = descricao,estabelecimento = estabelecimento)

		serializer = serializers.CestaSerializer(cesta)
		return Response(serializer.data)



class CadastrarItemServiceView(APIView):

	def post(self,request,format=None):

		marca = request.data.get('marca')
		unidade = request.data.get('unidade')
		filtro = request.data.get('filtro')
		valor = request.data.get('valor')
		cesta_id= request.data.get('cesta_id')
		
		
		item = models.ItemCesta.objects.create(marca = marca,
											unidade = unidade, 
											filtro = filtro, 
											valor = valor, 
											cesta_id = cesta_id)

		serializer = serializers.ItemCestaSerializer(item)
		return Response(serializer.data)



#Update
class AtualizarEstabelecimentoServiceView(APIView):

	def post(self,request,format=None):

		estabelecimento = models.Estabelecimento.objects.get(id=request.data.get('id'))
		estabelecimento.descricao = request.data.get('descricao')

		estabelecimento.save()

		serializer = serializers.EstabelecimentoSerializer(estabelecimento)
		return Response(serializer.data)



class AtualizarMarcaServiceView(APIView):

	def post(self,request,format=None):

		marca = models.Marca.objects.get(id=request.data.get('id'))
		marca.descricao = request.data.get('descricao')

		marca.save()

		serializer = serializers.MarcaSerializer(marca)
		return Response(serializer.data)



class AtualizarUnidadeServiceView(APIView):

	def post(self,request,format=None):

		unidade = models.Unidade.objects.get(id=request.data.get('id'))
		unidade.descricao = request.data.get('descricao')

		unidade.save()

		serializer = serializers.UnidadeSerializer(unidade)
		return Response(serializer.data)



class AtualizarFiltroServiceView(APIView):

	def post(self,request,format=None):

		filtro = models.Filtro.objects.get(id=request.data.get('id'))
		filtro.descricao = request.data.get('descricao')

		filtro.save()

		serializer = serializers.FiltroSerializer(filtro)
		return Response(serializer.data)



class AtualizarCestaServiceView(APIView):

	def post(self,request,format=None):

		cesta = models.Cesta.objects.get(id=request.data.get('id'))
		cesta.descricao = request.data.get('descricao')
		cesta.estabelecimento = request.data.get('estabelecimento')

		cesta.save()

		serializer = serializers.CestaSerializer(cesta)
		return Response(serializer.data)



class AtualizarItemServiceView(APIView):

	def post(self,request,format=None):

		item = models.ItemCesta.objects.get(id=request.data.get('id'))
		item.marca = request.data.get('marca')
		item.unidade = request.data.get('unidade')
		item.filtro = request.data.get('filtro')
		item.valor = request.data.get('valor')

		item.save()

		serializer = serializers.ItemCestaSerializer(item)
		return Response(serializer.data)

#Exclusão
class ExcluirEstabelecimentoServiceView(APIView):

	def post(self,request,format=None):

		estabelecimento = models.Estabelecimento.objects.get(id=request.data.get('id'))

		estabelecimento.delete()

		serializer = serializers.EstabelecimentoSerializer(estabelecimento)
		return Response(serializer.data)



class ExcluirMarcaServiceView(APIView):

	def post(self,request,format=None):

		marca = models.Marca.objects.get(id=request.data.get('id'))

		marca.delete()

		serializer = serializers.MarcaSerializer(marca)
		return Response(serializer.data)



class ExcluirUnidadeServiceView(APIView):

	def post(self,request,format=None):

		unidade = models.Unidade.objects.get(id=request.data.get('id'))

		unidade.delete()

		serializer = serializers.UnidadeSerializer(unidade)
		return Response(serializer.data)



class ExcluirFiltroServiceView(APIView):

	def post(self,request,format=None):

		filtro = models.Filtro.objects.get(id=request.data.get('id'))

		filtro.delete()

		serializer = serializers.FiltroSerializer(filtro)
		return Response(serializer.data)



class ExcluirCestaServiceView(APIView):

	def post(self,request,format=None):

		cesta = models.Cesta.objects.get(id=request.data.get('id'))

		cesta.delete()

		serializer = serializers.CestaSerializer(cesta)
		return Response(serializer.data)



class ExcluirItemServiceView(APIView):

	def post(self,request,format=None):

		item = models.ItemCesta.objects.get(id=request.data.get('id'))

		item.delete()

		serializer = serializers.ItemCestaSerializer(item)
		return Response(serializer.data)

