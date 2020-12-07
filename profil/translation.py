from modeltranslation.translator import register, TranslationOptions
from .models import TechSkill, SoftSkill, Profession, ProfessionInfo, UserInfo


@register(TechSkill)
class TechSkillTranslationOptions(TranslationOptions):
    fields = ('descr',)


@register(SoftSkill)
class SoftSkillTranslationOptions(TranslationOptions):
    fields = ('descr',)


@register(Profession)
class ProfessionTranslationOptions(TranslationOptions):
    fields = ('title', 'company_name', 'start', 'end')


@register(ProfessionInfo)
class ProfessionInfoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(UserInfo)
class UserInfoTranslationOptions(TranslationOptions):
    fields = ('name', 'vacancy', 'descr')
