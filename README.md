# ⚜ 1111. Szent István cserkészcsapat új weboldala

<p align="center">
<img src="https://user-images.githubusercontent.com/47941079/130056456-67ac8987-df33-473f-a2c1-8b6d1b77ec7b.png">


![Licence Badge](https://img.shields.io/github/license/pmihaly/cserkweb) 
   
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-crayons.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/contains-cat-gifs.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)
   
[Kanban tábla](https://github.com/pmihaly/cserkweb/projects/)
</p>

---

A budakalászi cserkészeknek terveztem ezt a weboldalt, hogy attraktívabb külsővel illessem meg az online jelenlétüket.

## Funkciók

* 🍃 Igényes design, amivel még jobb első benyomást okozhatunk a látogatóknak
* ⚜ Mutassuk be a csapatot
* 🏡 ..., és mutassuk be a bérelhető cserkészházat is
* ✏ Szervezők eseményeket (pl. táborok) és közleményeket írhatnak ki
* 🤖 Automatizálás lehetősége, mivel saját adatbázissal dolgozunk
    * ÚECS integráció
    * Weboldal közleményeit közösségi média oldalakon is kiírni
    * Tagdíj automatikus beszedése
    * 🌠 Határ a csillagos ég


## Használat

### Telepítés éles használatra

1. Másold le és szerkeszd szükség szerint a környezeti változókat

   ```shell
   cp .env.example .env
   vim .env
   ```

1. Hozz létre pár szükséges mappát, és töltsd meg a `cover_images` mappát minimum 1 képpel

   ```shell
   mkdir -p static media/blog/cover_images
   ```
   
1. Építsd meg a Docker konténereket és indítsd el a szervert a háttérben

   ```shell
   docker-compose up --build -d
   ```
   
1. Teszteld a projektet, hogy helyesen működik-e minden

   ```
   docker-compose exec web python manage.py test
   ```

1. Hozd létre az első szervezőt

   ```
   docker-compose exec web python manage.py createsuperuser
   ```

### Fejlesztőkörnyezet előállítása

1. Töltsd le a repot

    ``` shell
    git clone https://github.com/pmihaly/konyvhegy
    cd konyvhegy
    ```

1. Telepítsd a függőségeket és lépj be a viruális környezetbe

   ```
   pipenv install
   pipenv shell
   ```


1. Hozd létre az adatbázisstruktúrát és indítsd el a szervert

   ```
   python manage.py makemigrations
   python manage.py migrate 
   python manage.py runserver
   ```

## Fájlstruktúra

<!-- tree about blog cserkweb -I 'assets' -->

```
about
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── templates
│   └── about
│       ├── about_us.html
│       ├── homepage.html
│       └── house.html
├── tests.py
├── urls.py
└── views.py
blog
├── admin.py
├── apps.py
├── forms.py
├── __init__.py
├── migrations
│   ├── 0001_initial.py
│   └── __init__.py
├── models.py
├── templates
│   └── blog
│       ├── post_detail.html
│       └── post_list.html
├── tests
│   ├── __init__.py
│   ├── test_models.py
│   └── test_views.py
├── urls.py
└── views.py
cserkweb
├── __init__.py
├── settings.py
├── templates
│   ├── base.html
│   ├── errors
│   │   ├── 404.html
│   │   └── 500.html
│   ├── footer.html
│   ├── includes.html
│   ├── nav.html
│   └── post_card.html
├── urls.py
└── wsgi.py

9 directories, 36 files
```

## Köszönetnyílvánítás

A cserkészcsapatnak, akik:
- adták a projekt ihletét
- rengeteg jó élményt okoztak

## Licenc

Copyright © 2021 Papp Mihály

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
