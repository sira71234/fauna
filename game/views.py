from django.shortcuts import render
from django.utils import timezone
from .models import Animal, LeconDuJour, ModeJeu, Score
import random


def accueil(request):
    if request.method == 'GET':
        score = request.session.pop('score', None)
        mode_slug = request.session.pop('mode_slug', None)
        if score is not None and mode_slug:
            try:
                mode_jeu, _ = ModeJeu.objects.get_or_create(
                    slug=mode_slug, defaults={'nom': mode_slug.replace('_', ' ').title()}
                )
                Score.objects.create(mode=mode_jeu, points=score)
            except Exception:
                pass
    return render(request, 'game/accueil.html')


def culture_g(request):
    animaux = list(Animal.objects.all())

    if len(animaux) < 4:
        return render(request, 'game/culture_g.html', {'erreur': "Pas assez d'animaux dans la base."})

    if request.method == 'POST':
        if 'score' not in request.session:
            request.session['score'] = 0
            request.session['mode_slug'] = 'culture_g'

        reponse = request.POST.get('reponse')
        bonne_reponse = request.POST.get('bonne_reponse')
        if reponse == bonne_reponse:
            resultat = '✅ Bonne réponse !'
            request.session['score'] = request.session.get('score', 0) + 1
        else:
            resultat = f'❌ Mauvaise réponse. La bonne réponse était : {bonne_reponse}'
        return render(request, 'game/culture_g.html', {
            'resultat': resultat,
            'score': request.session.get('score', 0),
        })

    animal = random.choice(animaux)

    champs = [
        ('habitat', "Quel est l'habitat du {} ?".format(animal.nom)),
        ('continent', "Sur quel continent vit le {} ?".format(animal.nom)),
        ('regime_alimentaire', "Quel est le régime alimentaire du {} ?".format(animal.nom)),
        ('categorie', "Dans quelle catégorie classe-t-on le {} ?".format(animal.nom)),
        ('famille_nom_commun', "À quelle famille appartient le {} ?".format(animal.nom)),
        ('ordre', "À quel ordre appartient le {} ?".format(animal.nom)),
    ]

    champs_valides = [(champ, question) for champ, question in champs if getattr(animal, champ)]
    champ, question = random.choice(champs_valides)
    bonne_reponse = getattr(animal, champ)

    autres = [a for a in animaux if getattr(a, champ) and getattr(a, champ) != bonne_reponse]
    mauvaises = random.sample(autres, min(3, len(autres)))
    mauvaises_reponses = [getattr(a, champ) for a in mauvaises]

    choix = mauvaises_reponses + [bonne_reponse]
    random.shuffle(choix)

    context = {
        'animal': animal,
        'question': question,
        'choix': choix,
        'bonne_reponse': bonne_reponse,
        'score': request.session.get('score', 0),
    }
    return render(request, 'game/culture_g.html', context)


def fmp(request):
    animaux = list(Animal.objects.all())

    if len(animaux) < 4:
        return render(request, 'game/fmp.html', {'erreur': "Pas assez d'animaux dans la base."})

    if request.method == 'POST':
        if 'score' not in request.session:
            request.session['score'] = 0
            request.session['mode_slug'] = 'fmp'

        reponse = request.POST.get('reponse')
        bonne_reponse = request.POST.get('bonne_reponse')
        if reponse == bonne_reponse:
            resultat = '✅ Bonne réponse !'
            request.session['score'] = request.session.get('score', 0) + 1
        else:
            resultat = f'❌ Mauvaise réponse. La bonne réponse était : {bonne_reponse}'
        return render(request, 'game/fmp.html', {
            'resultat': resultat,
            'score': request.session.get('score', 0),
        })

    animal = random.choice(animaux)

    champs = [
        ('nom_femelle', "Comment appelle-t-on la femelle du {} ?".format(animal.nom)),
        ('nom_male', "Comment appelle-t-on le mâle du {} ?".format(animal.nom)),
        ('nom_petit', "Comment appelle-t-on le petit du {} ?".format(animal.nom)),
        ('nom_groupe', "Comment appelle-t-on un groupe de {} ?".format(animal.nom)),
    ]

    champs_valides = [(champ, question) for champ, question in champs if getattr(animal, champ)]
    champ, question = random.choice(champs_valides)
    bonne_reponse = getattr(animal, champ)

    autres = [a for a in animaux if getattr(a, champ) and getattr(a, champ) != bonne_reponse]
    mauvaises = random.sample(autres, min(3, len(autres)))
    mauvaises_reponses = [getattr(a, champ) for a in mauvaises]

    choix = mauvaises_reponses + [bonne_reponse]
    random.shuffle(choix)

    context = {
        'animal': animal,
        'question': question,
        'choix': choix,
        'bonne_reponse': bonne_reponse,
        'score': request.session.get('score', 0),
    }
    return render(request, 'game/fmp.html', context)


def mode_image(request):
    animaux = list(Animal.objects.all())

    if len(animaux) < 4:
        return render(request, 'game/mode_image.html', {'erreur': "Pas assez d'animaux dans la base."})

    if request.method == 'POST':
        if 'score' not in request.session:
            request.session['score'] = 0
            request.session['mode_slug'] = 'mode_image'

        reponse = request.POST.get('reponse')
        bonne_reponse = request.POST.get('bonne_reponse')
        if reponse == bonne_reponse:
            resultat = '✅ Bonne réponse !'
            request.session['score'] = request.session.get('score', 0) + 1
        else:
            resultat = f'❌ Mauvaise réponse. La bonne réponse était : {bonne_reponse}'
        return render(request, 'game/mode_image.html', {
            'resultat': resultat,
            'score': request.session.get('score', 0),
        })

    animal = random.choice(animaux)
    question = "Quel est le nom de cet animal ?"
    bonne_reponse = animal.nom

    autres = [a for a in animaux if a.nom != bonne_reponse]
    mauvaises = random.sample(autres, min(3, len(autres)))
    mauvaises_reponses = [a.nom for a in mauvaises]

    choix = mauvaises_reponses + [bonne_reponse]
    random.shuffle(choix)

    context = {
        'animal': animal,
        'question': question,
        'choix': choix,
        'bonne_reponse': bonne_reponse,
        'score': request.session.get('score', 0),
    }
    return render(request, 'game/mode_image.html', context)


def mode_image_inverse(request):
    animaux_avec_image = list(Animal.objects.exclude(image=''))

    if len(animaux_avec_image) < 4:
        return render(request, 'game/mode_image_inverse.html', {
            'erreur': "Pas assez d'animaux avec image dans la base."
        })

    if request.method == 'POST':
        if 'score' not in request.session:
            request.session['score'] = 0
            request.session['mode_slug'] = 'mode_image_inverse'

        reponse = request.POST.get('reponse')
        bonne_reponse = request.POST.get('bonne_reponse')
        if reponse == bonne_reponse:
            resultat = '✅ Bonne réponse !'
            request.session['score'] = request.session.get('score', 0) + 1
        else:
            resultat = f'❌ Mauvaise réponse. La bonne réponse était : {bonne_reponse}'
        return render(request, 'game/mode_image_inverse.html', {
            'resultat': resultat,
            'score': request.session.get('score', 0),
        })

    animal = random.choice(animaux_avec_image)
    question = "Quel est cet animal ?"

    autres = [a for a in animaux_avec_image if a.nom != animal.nom]
    mauvaises = random.sample(autres, min(3, len(autres)))
    animaux_choisis = mauvaises + [animal]
    random.shuffle(animaux_choisis)

    choix_images = []
    for a in animaux_choisis:
        choix_images.append({
            'nom': a.nom,
            'image_url': a.image.url,
        })

    context = {
        'question': question,
        'bonne_reponse': animal.nom,
        'choix_images': choix_images,
        'score': request.session.get('score', 0),
    }
    return render(request, 'game/mode_image_inverse.html', context)


def mode_cri(request):
    animaux_avec_cri = list(Animal.objects.exclude(cri=''))

    if len(animaux_avec_cri) < 4:
        return render(request, 'game/mode_cri.html', {
            'erreur': "Pas assez d'animaux avec cri dans la base."
        })

    if request.method == 'POST':
        if 'score' not in request.session:
            request.session['score'] = 0
            request.session['mode_slug'] = 'mode_cri'

        reponse = request.POST.get('reponse')
        bonne_reponse = request.POST.get('bonne_reponse')
        if reponse == bonne_reponse:
            resultat = '✅ Bonne réponse !'
            request.session['score'] = request.session.get('score', 0) + 1
        else:
            resultat = f'❌ Mauvaise réponse. La bonne réponse était : {bonne_reponse}'
        return render(request, 'game/mode_cri.html', {
            'resultat': resultat,
            'score': request.session.get('score', 0),
        })

    animal = random.choice(animaux_avec_cri)
    question = "Quel animal fait ce cri ?"

    autres = [a for a in animaux_avec_cri if a.nom != animal.nom]
    mauvaises = random.sample(autres, min(3, len(autres)))
    mauvaises_reponses = [a.nom for a in mauvaises]

    choix = mauvaises_reponses + [animal.nom]
    random.shuffle(choix)

    context = {
        'animal': animal,
        'question': question,
        'choix': choix,
        'bonne_reponse': animal.nom,
        'score': request.session.get('score', 0),
    }
    return render(request, 'game/mode_cri.html', context)


def lecon_du_jour(request):
    today = timezone.now().date()
    lecon = LeconDuJour.objects.filter(date=today).select_related('animal').first()

    if not lecon:
        return render(request, 'game/lecon_du_jour.html', {
            'aucune_lecon': True,
            'date': today,
        })

    context = {
        'lecon': lecon,
        'animal': lecon.animal,
        'date': today,
    }
    return render(request, 'game/lecon_du_jour.html', context)
