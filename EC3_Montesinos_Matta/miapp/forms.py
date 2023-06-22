from django import forms
class FormArticulo(forms.Form):
    titulo = forms.CharField(
        label="Titulo"
)
# Usar CharField para generar un campo de texto normal
    contenido = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea
)