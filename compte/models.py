import calendar
import locale
from django.db import models
from custom_user.models import AbstractEmailUser
from django.utils import timezone

#fr 
locale.setlocale(locale.LC_ALL, 'Fra')

GENDER_TYPES = (
    ('H', 'Homme'),
    ('F', 'Femme'),
)
Jours=tuple([(i,j) for (i,j) in zip(range(1,32),range(1,32))])

Mois=tuple([(i,calendar.month_name[j]) for (i,j) in zip(range(1,13),range(1,13))])

Annee=tuple([(i,j) for (i,j) in zip(range(1930,1999),range(1930,1999))])




class Adresse(models.Model):

	numero = models.IntegerField()
	rue = models.CharField(max_length=100, default='')
	cp = models.IntegerField()
	ville = models.CharField(max_length=100, default='')
	pays = models.CharField(max_length=100, default='')
	adresse_principale = models.BooleanField(default=True)






# Base de données Utilisateur


class Utilisateurs(AbstractEmailUser):
	#de User
	email = models.EmailField(verbose_name='adresse mail', max_length=255, unique=True, db_index=True)
	# is_active = models.BooleanField(default=True)
	# is_admin = models.BooleanField(default=False)
	# is_staff = models.BooleanField( default=False)
	# date_joined = models.DateTimeField(default=timezone.now)
	# is_special = models.BooleanField(default=False)
	prenom = models.CharField(max_length=100, default='')
	nom = models.CharField(max_length=100, default='')

    #rajoute
	jour_naissance = models.IntegerField(choices=Jours,default='01')
	mois_naissance = models.IntegerField(choices=Mois,default='01')
	annee_naissance = models.IntegerField(choices=Annee,default='1998')
	sexe=models.CharField(choices=GENDER_TYPES, max_length=10)
	fb_profile = models.URLField(null=True,blank=True)
	tw_profile = models.URLField(null=True,blank=True)
	ln_profile = models.URLField(null=True,blank=True)
	google_plus_url = models.URLField(null=True,blank=True)
	description = models.TextField(null=True, blank=True)
	adresse = models.ManyToManyField(Adresse, blank=True)
	identite = models.ImageField(null=True,blank=True,upload_to="identite/")
	telephone = models.BigIntegerField(null=True, blank=True)
	identite_verifie = models.BooleanField(default=False)
	email_verifie = models.BooleanField(default=False)
	tel_verifie = models.BooleanField(default=False)
	nb_annonce = models.BigIntegerField(null=True, blank=True,default=0)
	nb_livraison = models.IntegerField(null=True, blank=True,default=0)
	nb_cmd = models.IntegerField(null=True, blank=True,default=0)

	

	USERNAME_FIELD = 'email'

	class Meta:
		db_table = 't_utilisateur'
	

	def get_full_name(self):
    	# The user is identified by their email address
		return self.first_name + ' ' + self.last_name

	def get_short_name(self):
        # The user is identified by their email address
		return self.first_name

	# def __unicode__(self):
	# 	return self.first_name + ' (' + self.email + ')'

	def is_site_admin(self):
		if self.user_roles == "Admin" or self.is_superuser:
			return True
		return False







