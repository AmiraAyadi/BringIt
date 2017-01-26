from django.shortcuts import render
from django import forms
from enregistrement.forms import UserForm, AddressForm


def enregistrement_step1(request):
    nom={'nom': request.session.get('nom', None)}
    prenom={'prenom': request.session.get('prenom', None)}
    mdp={'mdp': request.session.get('mdp', None)}
    email={'email': request.session.get('email', None)}

    form = UserForm(request.POST or None)

	if request.method == "POST":
		if form.is_valid():
            request.session['nom'] = form.cleaned_data['nom']
            request.session['prenom'] = form.cleaned_data['prenom']
            request.session['email'] = form.cleaned_data['email']
            request.session['mdp'] = form.cleaned_data['mdp']           
            return HttpResponseRedirect(reverse('step2'))
	return render(request, 'enregistrement.html', {'form': form})




def enregistrement_step2(request):
	telephone={'telephone': request.session.get('telephone', None)}

    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pet = form.save(commit=False)
            person = Person.objects.create(fn=request.session['fn'])
            pet.owner = person
            pet.save()
            return HttpResponseRedirect(reverse('finished'))
    return render(request, 'step2.html', {'form': form})











# from django.shortcuts import render

# from enregistrement.forms import ContactForm

# def Enregistrement(request):
# 	form = Enregistrement()
# 	if request.method == "POST":
# 	    form = Enregistrement(request.POST)
# 	    if form.is_valid():
#         # Ici nous pouvons traiter les données du formulaire
#         	sujet = form.cleaned_data['sujet']
#         	message = form.cleaned_data['message']
#         	envoyeur = form.cleaned_data['envoyeur']
#         	renvoi = form.cleaned_data['renvoi']
#         	envoi = True

# 		# Quoiqu'il arrive, on affiche la page du formulaire.
# 	return render(request, 'contact.html' , {'form': form})