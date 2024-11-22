### Database opzetten
Om de database op te zetten moet je eerst de juist database gegevens in de .env zetten.

Vervolgens kan je in de main.py de volgende functies aanroepen:

```python
    create_database()
    create_schema()
```
Wanneer dat gedaan is kan je de alembic migrations uitvoeren door het volgende in de terminal in te voeren. 
Hierdoor worden de tables aangemaakt
```
    alembic revision --autogenerate -m "Create the initialization tables"
```
Voeg het volgende commando uit om de migratie door te voeren 
```
    alembic upgrade head
```
