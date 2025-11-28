# Student Score Prediction using Linear Regression

##  Description du Projet
Ce projet utilise une régression linéaire pour prédire le score d’un étudiant en fonction du nombre d’heures étudiées.  
C’est un projet simple et classique de Machine Learning supervisé permettant d’apprendre :

- La préparation des données  
- Le split train/test  
- L'entraînement d’un modèle de régression  
- L’évaluation avec RMSE et R²  
- La visualisation des prédictions  

---

##  Objectifs du Projet
- Explorer le dataset `student_scores.csv`
- Visualiser la relation entre les heures étudiées et les scores obtenus
- Entraîner un modèle de **régression linéaire**
- Évaluer sa performance sur des données de test
- Visualiser les performances (Actual vs Predicted, Regression Line)

---

##  Approche
1. Chargement et visualisation des données  
2. Analyse statistique simple (shape, colonnes, valeurs manquantes)  
3. Séparation des données en train/test  
4. Entraînement du modèle LinearRegression  
5. Calcul des métriques :
   - **R² Score**
   - **RMSE**
6. Visualisations :
   - Scatter plot Hours vs Score  
   - Actual vs Predicted  
   - Ligne de régression

---

##  Dataset
Le dataset utilisé est `student_scores.csv` et contient deux colonnes :

```
Hours, Score
```

- **Hours** : nombre d’heures étudiées  
- **Score** : note obtenue  

---

##  Résultats
Après entraînement du modèle :

- **R² Score** : montre la qualité de la prédiction  
- **RMSE** : erreur moyenne de prédiction  
- Graphiques générés :  
  - Relation Hours vs Score  
  - Comparaison scores réels vs prédits  
  - Ligne de régression  

---

##  Fichiers Principaux
- `main.py` — Script complet du modèle  
- `student_scores.csv` — Dataset  
- `README.md` — Documentation du projet  

---

## 👤 Auteur
Projet réalisé par **Chahboune Ismail**
