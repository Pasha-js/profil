from django.contrib import admin
from.models import TechSkill, SoftSkill, Profession, ProfessionInfo, UserInfo
from modeltranslation.admin import TranslationAdmin

class ProfessionInfoInline(admin.TabularInline):
    model = ProfessionInfo
    extra = 0

# Register your models here.
class ProfessionAdmin(TranslationAdmin):
    inlines = [
        ProfessionInfoInline
    ]

admin.site.register(TechSkill)
admin.site.register(SoftSkill)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(ProfessionInfo)
admin.site.register(UserInfo)