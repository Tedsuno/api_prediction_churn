# API de Prédiction du Churn Client

Ce dépôt contient une API en production développée avec FastAPI pour prédire le churn client à partir d'un modèle d'apprentissage automatique entraîné (Random Forest) avec scikit-learn. L'API prend en entrée les données d'un client et retourne une prédiction indiquant s'il est susceptible de se désabonner.

## Aperçu

L'API est conçue pour être déployée dans des environnements scalables et s'intègre facilement aux systèmes existants.

## Structure du projet

```
api_prediction_churn/
├── app/
│   ├── main.py
│   ├── predict.py
│   └── schemas.py
├── model/
│   ├── churn.csv
│   ├── model.pkl
│   └── train_model.ipynb
├── tests/
│   └── test_main.py
├── Dockerfile
├── requirements.txt
├── .github/workflows/
│   └── ci.yml
└── README.md
```

## Fonctionnalités

* **FastAPI** : API REST hautes performances.
* **Scikit-learn** : Modèle Random Forest pour la prédiction.
* **Docker** : Déploiement facile dans des conteneurs isolés.
* **CI/CD (GitHub Actions)** : Tests et vérifications automatisées.
* **Tests unitaires** : Garantit la fiabilité des endpoints de l'API.

## Démarrage rapide

### Exécution locale

Cloner le dépôt :

```bash
git clone https://github.com/Tedsuno/api_prediction_churn/
cd api_prediction_churn
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Lancer l'API en local :

```bash
uvicorn app.main:app --reload
```

Accéder à la documentation interactive :

```
http://127.0.0.1:8000/docs
```

### Docker

Construire l'image Docker :

```bash
docker build -t churn-api .
```

Lancer le conteneur Docker :

```bash
docker run -p 8000:8000 churn-api
```

## Utilisation

### Endpoint de l'API

* **POST `/predict`** : Envoie les données client au format JSON et reçoit une prédiction (`Yes` ou `No`).

#### Exemple de requête :

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "Yes",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Credit card (automatic)",
  "MonthlyCharges": 75.5,
  "TotalCharges": 850.2
}
```

#### Exemple de réponse :

```json
{
  "prediction": "Yes"
}
```

## Intégration Continue

GitHub Actions assure la qualité du code en :

* Exécutant des tests automatisés (`pytest`) à chaque push.
* Contrôlant les standards de codage (lint).

## Tests

Lancer les tests en local :

```bash
pytest
```

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
