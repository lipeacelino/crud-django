from django.db import models

'''nome, categoria, quantidade, preço'''
class Produto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=40)
    categoria = models.CharField(max_length=40)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)


    class Meta:
        verbose_name_plural = 'Produtos'


    def __str__(self):
        return 'Nome: ' + str(self.nome) + ' - ' + 'Qtd: ' + str(self.quantidade) +  ' - Categoria: ' + str(self.categoria) + ' - Quantidade: ' + str(self.quantidade) \
               + str(self.quantidade) + ' - Preço: ' + str(self.preco)
