from django.contrib import admin
from .models import AboutMe, ClientReview, ContactMessage, Education, Entrepreneurial, Institution, \
    Portfolio, ProfessionalSkill, ProjectCategory, Service, SiteConfig, SocialNetwork, TechnicalSkill, \
    WorkExperience
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


# Register your models here.

class SocialNetworkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'icon', 'url', 'order']


class ServiceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'icon', 'description', 'order']


class TechnicalSkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'score', 'order']


class ProfessionalSkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'score', 'order']


admin.site.register(AboutMe)
admin.site.register(ClientReview)
admin.site.register(ContactMessage)
admin.site.register(Education)
admin.site.register(Entrepreneurial)
admin.site.register(Institution)
admin.site.register(Portfolio)
admin.site.register(ProfessionalSkill, ProfessionalSkillAdmin)
admin.site.register(ProjectCategory)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SiteConfig)
admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(TechnicalSkill, TechnicalSkillAdmin)
admin.site.register(WorkExperience)
