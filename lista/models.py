from django.db import models

class Item(models.Model):



#essa classe tem uma função que retorna o nome do item {
# }
    def __str__(self):
        return self.item

