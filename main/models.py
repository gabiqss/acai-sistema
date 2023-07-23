from django.db import models


class Sorvete(models.Model):

    mesa_numero = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    mesa = models.CharField(
        max_length=3,
        choices=mesa_numero,
        default='',
    )

    sabor_creme = (
        ('.', '.'),
        ('Açaí', 'Açaí'),
        ('Cupuaçu', 'Cupuaçu')
    )

    sabor = models.CharField(
        max_length=10,
        choices=sabor_creme,
        default='.',
    )

    sabor_cobertura = (
        ('.', '.'),
        ('Chocolate', 'Chocolate'),
        ('Morango', 'Morango'),
        ('Caramelo', 'Caramelo'),
        ('Leite Condensado', 'Leite condensado')
    )

    cobertura = models.CharField(
        max_length=20,
        choices=sabor_cobertura,
        default='.',
    )

    tipo_tamanho = (
        ('.', '.'),
        ('Pequeno', 'Pequeno'),
        ('Médio', 'Médio'),
        ('Grande', 'Grande'),
        ('Barca', 'Barca')
    )

    tamanho = models.CharField(
        max_length=10,
        choices=tipo_tamanho,
        default='.',
    )

    salgado_tipo = (
        ('.', '.'),
        ('Coxinha', 'Coxinha'),
        ('Risole', 'Risole'),
        ('Empada', 'Empada'),
    )

    salgado = models.CharField(
        max_length=10,
        choices=salgado_tipo,
        default='.',
    )

    def __str__(self):
        return self.mesa
    