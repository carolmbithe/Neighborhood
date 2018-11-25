from django.contrib import admin
from .models import NeighborHood,Userprofile,Business,Post,PoliceCenters,HealthCenter

# Register your models here.

admin.site.register(NeighborHood)
admin.site.register(Userprofile)
admin.site.register(Business)
admin.site.register(Post)

admin.site.register(PoliceCenters)
admin.site.register(HealthCenter)
