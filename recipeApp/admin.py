from django.contrib import admin

from recipeApp.models import custom_user, add_recipe_model

# Register your models here.
class custom_user_display(admin.ModelAdmin):
    list_display=['username', 'country']
admin.site.register(custom_user, custom_user_display)
admin.site.register(add_recipe_model)
