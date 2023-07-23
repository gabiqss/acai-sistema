# Generated by Django 4.2.3 on 2023-07-22 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorvete',
            name='mesa',
            field=models.CharField(choices=[], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='sorvete',
            name='cobertura',
            field=models.CharField(choices=[('Chocolate', 'Chocolate'), ('Morango', 'Morango'), ('Caramelo', 'Caramelo'), ('Leite Condensado', 'Leite condensado')], default='Leite Condensado', max_length=20),
        ),
        migrations.AlterField(
            model_name='sorvete',
            name='sabor',
            field=models.CharField(choices=[('Açaí', 'Açaí'), ('Cupuaçu', 'Cupuaçu')], default='Açaí', max_length=10),
        ),
        migrations.AlterField(
            model_name='sorvete',
            name='tamanho',
            field=models.CharField(choices=[('Pequeno', 'Pequeno'), ('Médio', 'Médio'), ('Grande', 'Grande'), ('Barca', 'Barca')], default='Médio', max_length=10),
        ),
    ]