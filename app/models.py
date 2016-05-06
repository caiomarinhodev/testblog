from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Produto(models.Model):
#     EMPTY = ''
#     KILO = 'Kg'
#     UNIDADE = 'Un.'
#     ITEM = 'Item'
#
#     TIPOS = (
#         (EMPTY, ''),
#         (KILO, 'Kilo'),
#         (UNIDADE, 'Unidade'),
#         (ITEM, 'Item'),
#     )
#
#     nome = models.CharField(max_length=100)
#     foto = models.CharField(max_length=300, default='')
#     descricao = models.TextField(default='')
#     valor_venda = models.CharField(max_length=10)
#     valor_promo = models.CharField(max_length=10)
#     tipo = models.CharField(max_length=30, choices=TIPOS)
#     categoria = models.ForeignKey(Categoria)
#
#     def __str__(self):  # __unicode__ on Python 2
#         return str(self.nome).upper()