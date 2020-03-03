from django.contrib import admin

from .models import SkillModel, AboutModel, ContactModel, LearntModel, SeoModel

admin.site.register(SkillModel)
admin.site.register(AboutModel)
admin.site.register(ContactModel)
admin.site.register(SeoModel)
admin.site.register(LearntModel)
