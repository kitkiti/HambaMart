from django import forms
from apps.products.models import Product, ProductTags

class ProductForm(forms.ModelForm):
    tags = forms.CharField(max_length=255, required=False, help_text="Comma-separated tags")

    class Meta:
        model = Product
        fields = ['Title', 'Description', 'Stock', 'Price', 'product_img', 'AdminID']

    def save(self, commit=True):
        product = super().save(commit)
        tags_data = self.cleaned_data.get('tags')
        if tags_data:
            tags = [tag.strip() for tag in tags_data.split(',')]
            for tag in tags:
                ProductTags.objects.create(Product_ID=product, Tag=tag)
        return product

