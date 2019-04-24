from django.contrib import admin

# Register your models here.

from .models import Estabelecimento
from .models import Marca
from .models import Unidade
from .models import Filtro
from .models import Cesta
from .models import ItemCesta

admin.site.register(Estabelecimento)
admin.site.register(Marca)
admin.site.register(Unidade)
admin.site.register(Filtro)
admin.site.register(Cesta)
admin.site.register(ItemCesta)

