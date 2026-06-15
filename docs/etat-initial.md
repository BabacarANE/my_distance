# État initial du projet (avant modifications)

## Dette technique

Mesurée avec `radon` (complexité cyclomatique et indice de maintenabilité) :

- `radon cc app.py -s -a` : 4 fonctions, toutes en grade A, complexité moyenne 1.5
- `radon mi app.py` : indice de maintenabilité A

Ces outils indiquent un code structurellement simple. Cependant, une lecture
manuelle révèle une dette technique non capturée par ces métriques :

- Le script ne lance aucun serveur (`app.run()` manquant), l'application
  ne démarre donc pas.
- Code mort : un `print()` placé après un `return` dans `already_calculated`.
- Incohérences de typage entre la route HTML (`/`) et la route API
  (`/api/distance`) pour des opérations équivalentes.
- Aucune validation des entrées utilisateur (risque de plantage sur
  entrée malformée).
- Absence totale de tests automatisés.

## Couverture de tests

Mesurée avec `pytest --cov=. --cov-report=term-missing` :

- 0 test collecté
- Couverture : 0% (0/35 instructions exécutées)