from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem('Usuarios', icon='fa fa-user', children=[
            ChildItem(model='auth.user'),
            ChildItem(model='auth.group'),
        ]),
        ParentItem('Landing Page', icon='fa fa-file', children=[
            ChildItem(model='landing' + '.AboutMe'.lower()),
            ChildItem(model='landing' + '.Service'.lower()),
            ChildItem(model='landing' + '.Entrepreneurial'.lower()),
            ChildItem(model='landing' + '.TechnicalSkill'.lower()),
            ChildItem(model='landing' + '.ProfessionalSkill'.lower()),
            ChildItem(model='landing' + '.Education'.lower()),
            ChildItem(model='landing' + '.WorkExperience'.lower()),
            ChildItem(model='landing' + '.Portfolio'.lower()),
            ChildItem(model='landing' + '.ClientReview'.lower()),
        ]),
        ParentItem('Mensajes', icon='fa fa-envelope', children=[
            ChildItem(model='landing.ContactMessage'.lower()),
        ]),
        ParentItem('Reportes', icon='fa fa-list-alt', children=[
            ChildItem(model='admin.logentry'),
        ]),
        ParentItem('Configuración', icon='fa fa-cog', children=[
            ChildItem(model='landing' + '.SiteConfig'.lower()),
            ChildItem(model='landing' + '.SocialNetwork'.lower()),
            #ChildItem(model='rest_framework_api_key.apikey'),
        ]),
    )
