from django.forms import CharField, Form, URLInput, ValidationError
from .validators import ValidatorUrl


class AddBlankForm(Form):
    url = CharField(label='Ссылка', widget=URLInput(attrs={'class': 'form-control'}))

    def clean_url(self):
        url = self.cleaned_data['url']

        if ValidatorUrl.request_validation(url) is None:
            raise ValidationError(f"Не получилось получить информацию с сайта {url}, попробуйте указать другую ссылку")

        if ValidatorUrl.db_validation(url) is None:
            raise ValidationError(f"Данный сайт уже есть в закладках")
