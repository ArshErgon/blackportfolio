from django.contrib import admin

from .models import SkillModel, AboutModel, LearntModel, SeoModel, Project, SocialMedia

admin.site.register(SkillModel)
admin.site.register(AboutModel)
admin.site.register(SeoModel)
admin.site.register(LearntModel)
admin.site.register(Project)
admin.site.register(SocialMedia)
