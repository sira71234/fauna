from django.contrib import admin
from .models import Animal, LeconDuJour, ModeJeu, Score


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'famille', 'continent', 'niveau_difficulte')
    search_fields = ('nom', 'famille', 'ordre')
    list_filter = ('categorie', 'continent', 'regime_alimentaire', 'niveau_difficulte')


@admin.register(LeconDuJour)
class LeconDuJourAdmin(admin.ModelAdmin):
    list_display = ('date', 'animal')
    ordering = ('-date',)


@admin.register(ModeJeu)
class ModeJeuAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug')
    prepopulated_fields = {'slug': ('nom',)}


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('joueur', 'mode', 'points', 'date_partie')
    ordering = ('-date_partie',)