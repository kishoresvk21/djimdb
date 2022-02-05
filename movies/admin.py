from django.contrib import admin
from .models import Movies,Generes,Language,Actors,Directors,OnlinePlatform,TvSeries
# Register your models here.
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'rating',
        # 'starring',
        'director',
        # 'generes',
        'created_at',
        'updated_at',

    ]
models_list=(Generes,Language,Actors,Directors,OnlinePlatform,TvSeries)

for itr_model in models_list:
    admin.site.register(itr_model)



'''
list_display = (
            'username',
            'id',
            'email',
            'firstname',
            'lastname',
            'mobile',
            'created_at',
            'updated_at',
            'is_staff',
            'is_active',
            'is_superuser',
        )
    list_filter = ('is_admin',)
'''