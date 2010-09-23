from django.forms.widgets import Input


class SubmitButtonWidget(Input):
    """
    A widget that handles a submit button.
    """
    input_type = 'submit'
    
    def __init__(self, attrs=None):
        self.attrs = {'value': 'Submit'}
        if not attrs == None:
            self.attrs.update(attrs)
    
    def render(self, name, value, attrs=None):
        return super(SubmitButtonWidget, self).render(self.attrs['name'],
            self.attrs['value'], attrs)
