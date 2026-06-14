from django.contrib import admin
from .models import RangerTypes, RangerReview, RangerAbility,RangerStores

# Register your models here.
class RangerReviewInline(admin.TabularInline):
    model = RangerReview
    extra = 2

class RangerTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [RangerReviewInline]

class RangerStoresAdmin(admin.ModelAdmin):
    list_display = ('storeName', 'storeLocated')
    filter_horizontal = ('ranger_type_available',)

class RangerAbilityAdmin(admin.ModelAdmin):
    list_display = ('abilityName','abilityEffects')
    



admin.site.register(RangerTypes, RangerTypesAdmin)
admin.site.register(RangerStores, RangerStoresAdmin)
admin.site.register(RangerAbility, RangerAbilityAdmin)

