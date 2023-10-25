from django import forms
from .models import status , categoria, duracion, curso, clase


class statusForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del status",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = status
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(status, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Estado"


class categoriaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de la Categoria",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = categoria
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(status, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Categoría"




class duracionForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de la duracion",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = duracion
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(status, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Duración"        


class cursoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del curso",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = curso
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(status, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Curso"   



class claseForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de la clase",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = clase
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(status, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Clase"                