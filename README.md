# Dense-Optical-flow
Ce dépôt contient l'implémentation de l'algorithme de Farnebäck pour l'estimation du mouvement optique dense. Cet algorithme, qui repose sur une généralisation de l'approche de Lucas et Kanade, utilise l'expansion polynomiale pour modéliser le voisinage des pixels et ainsi estimer le mouvement de manière plus dense et plus précise.
Présentation

L'estimation du mouvement optique est une tâche importante dans de nombreux domaines, tels que la vision par ordinateur, la robotique et la vidéosurveillance. Elle permet de déterminer la position des objets dans une scène au fil du temps.

L'algorithme de Farnebäck est un algorithme d'estimation du mouvement optique dense, c'est-à-dire qu'il fournit un vecteur de déplacement pour chaque pixel de l'image. Il est particulièrement adapté aux scénarios où une haute résolution de mouvement est requise.
### Structure du projet

.
```
├── images                    # les images générées
├── videos                    # les vidéos
├── utils                     # les fonctions et scripts utilitaires
│  ├── extract.py            # classe qui calcule la PSNR, la DFD et dessine les flux de deux images données une taille de fenêtre
│  ├── myinfo_on_video.py    # infos sur la vidéo : hauteur, largeur, longueur de la séquence, fps
│  └── myreadseq.py            # Visualisation de la séquence video
├── .gitignore
├── mydense_optical_flow.py  # ce fichier permet de générer les images HSV et les flux avec flèches sur les différents frames de la vidéo
├── README.md
├── main.py                   # ce fichier permet de générer le graphique de la variation de la PSNR en fonction de la taille de la fenêtre
└── requirements.txt         # liste des dépendances

```
### Données

Le dataset utilisé pour ce projet est le dataset derf: https://media.xiph.org/video/derf/. Il s'agit d'une collection de vidéos de personnes en mouvement.
### Références

    Gunnar Farnebäck, « Two-frame motion estimation based on polynomial expansion », Proceedings of the 13th Scandinavian conference on Image analysis (SCIA'03), Josef Bigun and Tomas Gustavsson (Eds.). Springer-Verlag, Berlin, Heidelberg, 2003, p. 363-370.

### Installation

Clonez ce dépôt :
```
git clone https://github.com//Dense-Optical-flow.git](https://github.com/fouedayedi/Dense-Optical-flow.git
```
Installez les dépendances requises :
```
pip install -r requirements.txt
```
Exécutez le script:
```
python main.py
```
