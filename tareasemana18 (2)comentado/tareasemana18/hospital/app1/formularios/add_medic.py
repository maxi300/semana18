from django import forms

class Add_medic(forms.Form):
    nombre= forms.CharField(max_length=100)
    apellido= forms.CharField(max_length=100)
    especialidad=forms.CharField(max_length=100)


class Add_pac(forms.Form):
    nombre= forms.CharField(max_length=100)
    apellido= forms.CharField(max_length=100)
    cumple=forms.DateField()
    sexo= forms.CharField(max_length=100)
    altura= forms.FloatField()
    medico= forms.CharField()
    
   
