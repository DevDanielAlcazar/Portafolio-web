from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Escribe tu email'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje, si lo deseas tambien un teléfono o WhatsApp para que yo pueda contactarte. Mi WhatsApp es +52 (477)-569-4198'}))