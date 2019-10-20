# Cserkweb

## Fejlesztői környezet létrehozása

1. Hozd létre a virtuális környezetet és telepítsd a függőségeket Pipenv-el:

```
pipenv install
```

2. Lépj be a virtuális környezetbe:

```
pipenv shell
```

3. Hozd létre az adatbázisstruktúrát és indítsd el a szervert:

```
python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```

## Production szerver létrehozása

1. Másold le és szerkeszd szükség szerint a környezeti változókat:

```
cp .env.example .env
```

2. Építsd meg a Docker konténereket és indítsd el a szervert a háttérben (`-d` zászló):

```
docker-compose up -d
```
