
# Online obchod s administrátorským panelem

## Stručný popis systému
Součástí tohoto projektu je vytvoření aplikace, která umožní přidávat produkty do nabídky obchodu skrze administrátorský panel, umožní registraci uživatele, přihlašování do uživatelského účtu a vytváření objednávek.

git clone https://github.com/alifuk/CZ20_Obchod.git


## Užitečné příkazy
`git clone https://github.com/alifuk/CZ20_Obchod.git`

`python -m pip install django==4.1.1`

`django-admin startproject SDAcia .`

`python3 manage.py runserver` - spuštění serveru

`python3 manage.py startapp viewer` - přidání aplikace

`python3 manage.py makemigrations` - vytvoření migrací

`python3 manage.py migrate` - aplikování migrací

`python3 manage.py shell`

`python manage.py createsuperuser` - vytvoření uživatele pro admin rozhraní

[Dokumentace QuerySet](https://docs.djangoproject.com/en/5.1/ref/models/querysets/)

# Přehled django aplikace
![django_overview](django_overview.jpg)

## Musím umět

- Stáhnout Python, nainstalovat django
- Vytvořit django projekt, vytvořit django applikaci
- Vytvořit ORM model ( `models.py` )
- Vytvořit a aplikovat migraci databáze/modelu `python3 manage.py makemigrations` a `python3 manage.py migrate`
- Přidat objekt do DB `Genre.objects.create(name='Horror')`
- Upravit objekt v DB ( vyhledej v prezentaci `.save()` )
- Smazat objekt v DB ( vyhledej v prezentaci `.delete()` ) 
- Vytvořit url v djangu ( `urls.py` )
- Vrátit html šablonu naplněnou daty  ( `view.py` - funkce `hello` )
- Dědění html šablony (v šabloně `form.html` je děděno od `base.html`)
- Filtrování objektů z DB, získání jednoho konkrétního objektu 
- Vytvořit HTML formulář - viz `form.html`
- Vytvořit formulář pomocí třídy (příklad v `forms.py`) a poté ho vykreslit pomocí FormView (viz prezentace vyhledej 'FormView')
- Vložit do šablony statický soubor (css, js, jpg, svg)

## Tipy
- id/primární klíč konkrétního záznamu získám jako **car.pk**
- nalezení tohoto záznamu pak mohu udělat jako **Car.objects.get(pk=car_pk)**

### Ukázka odškrtávacího seznamu!
- [x] Inicializovat djagno
- [ ] Přidat stránku aukce
- [ ] Úkol 3
- [ ] Úkol 4
- [ ] Úkol 5

