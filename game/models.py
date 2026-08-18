from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    nom = models.CharField(max_length=100)
    nom_scientifique = models.CharField(max_length=150, blank=True)
    famille = models.CharField(max_length=100, blank=True)
    famille_nom_commun = models.CharField(max_length=100, blank=True)
    ordre = models.CharField(max_length=100, blank=True)
    nom_femelle = models.CharField(max_length=100, blank=True)
    nom_male = models.CharField(max_length=100, blank=True)
    nom_petit = models.CharField(max_length=100, blank=True)
    nom_groupe = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='animaux/')
    cri = models.FileField(upload_to='cris/', blank=True, null=True)
    nom_cri = models.CharField(max_length=100, blank=True)
    habitat = models.CharField(max_length=200, blank=True)
    continent = models.CharField(max_length=100, blank=True)
    regime_alimentaire = models.CharField(max_length=100, blank=True)
    categorie = models.CharField(max_length=100, blank=True)
    anecdote = models.TextField(blank=True)
    niveau_difficulte = models.IntegerField(default=1)

    def __str__(self):
        return self.nom


class LeconDuJour(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField(unique=True)
    contenu_supplementaire = models.TextField(blank=True)

    def __str__(self):
        return f"Leçon du {self.date} — {self.animal.nom}"


class ModeJeu(models.Model):
    nom = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom


class Score(models.Model):
    joueur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mode = models.ForeignKey(ModeJeu, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    date_partie = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.joueur} — {self.mode.nom} — {self.points} pts"