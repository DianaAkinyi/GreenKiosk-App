from django.shortcuts import render, redirect
from .models import Cart


    def add_product(self,product):
        self.products.add(product)
        self.save()
        return self
        
    def get_total(self):
        products =self.products.all()
        total=0
        for product in products:
            total + = product.price
        return total

