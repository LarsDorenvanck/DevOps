### Packages installeren
Om alle Python packages te installeren voer je het volgende commando uit in de root directory van het project.
```
pip install -r requirements.txt

```

### Database opzetten
Om de database op te zetten moet je eerst de juist database gegevens in de .env zetten.

Vervolgens kan je in de main.py de volgende functies aanroepen:

```python
create_database()
create_schema()
```

Voeg het volgende commando uit om de migratie door te voeren 
```
alembic upgrade head
```


### Niet zomaar de bedoeling (Vraag Niek ff)
Versions aanmaken
```
alembic revision --autogenerate -m "Create the initialization tables"
```

Alembic version delete
```sql
DELETE FROM alembic_version;
```

