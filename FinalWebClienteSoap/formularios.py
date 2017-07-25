from django import forms

CHOICES =(('1', '1',), ('2', '2',), ('3', '3',), ('4', '4',),('5', '5',), ('6', '6',), ('7', '7',), ('8', '8',), ('9', '9',),('10', '10',), ('11', '11',), ('12', '12',))
CHOICES2 =(('1', '1',), ('2', '2',), ('3', '3',), ('4', '4',),('5', '5',), ('6', '6',), ('7', '7',), ('8', '8',), ('9', '9',),('10', '10',), ('11', '11',), ('12', '12',), ('13', '13',),('14', '14',), ('15', '15',), ('16', '16',), ('17', '17',), ('18', '18',), ('19', '19',), ('20', '20',))
#choice_field = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
class realizarJugadaPale(forms.Form):
    usuario = forms.CharField(label='Usuario', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    clave = forms.CharField(label='Clave', required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'password'}))
    monto = forms.CharField(label='Monto a apostar', required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    primero = forms.ChoiceField(choices = CHOICES, label="Primero", initial='',
                                widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    segundo = forms.ChoiceField(choices=CHOICES, label="Segundo", initial='',
                                widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    tercero = forms.ChoiceField(choices=CHOICES, label="Tercero", initial='',
                                widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    ganar = forms.CharField(label='Ganar', required=False,
                              widget=forms.TextInput(attrs={'type': 'checkbox'}))

class realizarJugadaLoto(forms.Form):
    usuario = forms.CharField(label='Usuario', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    clave = forms.CharField(label='Clave', required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'type' : 'password'}))
    primero = forms.ChoiceField(choices = CHOICES2, label="Primero", initial='',
                                widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    segundo = forms.ChoiceField(choices=CHOICES2, label="Segundo", initial='',
                                widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    tercero = forms.ChoiceField(choices=CHOICES2, label="Tercero", initial='',
                                widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    cuarto = forms.ChoiceField(choices=CHOICES2, label="Cuarto", initial='',
                                widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    quinto = forms.ChoiceField(choices=CHOICES2, label="Quinto", initial='',
                                widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    ganar = forms.CharField(label='Ganar', required=False,
                              widget=forms.TextInput(attrs={'type': 'checkbox'}))
