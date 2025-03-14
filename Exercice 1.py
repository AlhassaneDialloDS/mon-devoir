import csv
import matplotlib.pyplot as plt


#Question 1 Lecture du fichier CSV
def lectureFic(ebola_guinea):
    #Lecture du fichier ebola_guinea.csv et stockage des donnees dans une liste de dictionnaires.
    donnees = []
    with open('ebola_guinea.csv','r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter=',')
        for ligne in lecteur:
            # Conversion des nombres en entiers
            ligne['Cas'] = int(ligne['Cas'])
            ligne['Dèces'] = int(ligne['Dèces' ])
            donnees.append(ligne)
    return donnees


# Question 2 Calculs statistiques
def calculer_statistiques(donnees):
    nombre = {}
    for i in donnees:
        prefecture = i['Préfecture']
        if prefecture not in nombre:
            nombre[prefecture] = {'cas': 0, 'deces': 0}
        nombre[prefecture]['cas'] += i['Cas']
        nombre[prefecture]['deces'] += i['Dèces']

    # Calcul du taux de mortalité
    for prefecture in nombre:
        cas = nombre[prefecture]['cas']
        deces = nombre[prefecture]['deces']
        nombre[prefecture]['taux'] = deces / cas if cas > 0 else 0.0
    return nombre


# Question 3 : Visualisation
def visualiser_donnees(nombre):
    #Génère deux diagrammes à barres : cas totaux et taux de mortalité.

    prefectures = list(nombre.keys())
    cas = [nombre[prefecture]['cas'] for prefecture in prefectures]
    taux = [nombre[prefecture]['taux'] for prefecture in prefectures]

    # Diagramme des cas
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, cas, color='red')
    plt.title('Nombre total de cas par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Cas')

    # Diagramme du taux de mortalité
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, taux, color='green')
    plt.title('Taux de mortalité par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Taux (Décès/Cas)')
    plt.ylim(0, 1)

    plt.show()


# main
if __name__ == "__main__":
    donnees = lire_csv('ebola_guinea.csv')
    nombre = calculer_statistiques(donnees)
    visualiser_donnees(nombre)