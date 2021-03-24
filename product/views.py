import json
from django.http        import JsonResponse

from django.views       import View
from product.models     import SubCategory, Product

class SubCategoryView(View):
    def get(self, request):
        sub_categories    = SubCategory.objects.all()
        sub_category_list = [{
            'sub_category'    : sub_category.id,
            'name'            : sub_category.name,
        } for sub_category in sub_categories]
        return JsonResponse({'sub_category_list_data' : sub_category_list}, status = 200)

class ProductListView(View):
    def get(self, request):
        products     = Product.objects.all()
        product_list = [{
            'product_id'      : product.id,
            'sub_category'    : product.sub_category.name,
            'name'            : product.name,
            'images'          : [image.image_url for image in product.image_set.all()],
            'price'           : product.price,
            'is_vegan'        : product.is_vegan,
            'is_new'          : product.is_new,
            'is_soldout'      : product.is_soldout,
            'product_labels'  : [label.label.name for label in product.productlabel_set.all()],
        } for product in products]
        return JsonResponse({'product_list_data' : product_list}, status = 200)