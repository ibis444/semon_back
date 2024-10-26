from modeltranslation.translator import register, TranslationOptions
from .models import AboutHomePage, ProductHomePage, ProjectHomePage, Statistic, AboutUs

@register(AboutHomePage)
class AboutHomePageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ProductHomePage)
class ProductHomePageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ProjectHomePage)
class ProjectHomePageTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title_1', 'title_2', 'description_1', 'description_2')
