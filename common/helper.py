

class StaticTemplates:
    app = 'books'
    create_template = '{}/forms/create/{}.html'
    view_template = '{}/views/{}.html'
    update_template = '{}/forms/update/{}.html'

    @staticmethod
    def create(link):
        return StaticTemplates.create_template.format(StaticTemplates.app, link)

    @staticmethod
    def view(link):
        return StaticTemplates.view_template.format(StaticTemplates.app, link)

    @staticmethod
    def update(link):
        return StaticTemplates.update_template.format(StaticTemplates.app, link)
