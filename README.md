# Dense-Optical-flow
Ce repo contient l'utlisation de l’algorithme de Farnebäck. Cette méthode, qui repose sur une généralisation de l’approche
de Lucas et Kanade, utilise l’expansion polynomiale pour modéliser le voisinage des pixels et ainsi
estimer le mouvement de manière plus dense et plus précise. La capacité de l’algorithme de Farnebäck
à fournir un vecteur de déplacement pour chaque pixel de l’image le rend particulièrement adapté aux
scénarios où une haute résolution de mouvement est requise. Dans ce TP, en mettant en application la
méthode de Farnebäck, nous ne nous contentons pas seulement de quantifier le mouvement, mais nous
plongeons également dans la complexité de son estimation, ce qui nous permet de saisir les nuances et
les défis techniques inhérents à l’analyse du mouvement dans les séquences vidéo.

## Project Structure

```plaintext
.
├── data                 # Directory containing the dataset
├── model                
│   └── classHOG.p       # Pre-trained model
├── pickle              
├── utile                # Utility functions and scripts
│   ├── __init__.py     
│   ├── functions.py     # Utility functions
│   └── visuHOG.py       # Visualization for HOG
├── .gitignore
├── HOG_ATELIER1.py      # SVM training and results
├── README.md
├── main.py              # Main script to run the project
└── requirements.txt     # List of dependencies
```
## Dataset

The dataset used for this project is the les séquences vidéo à étudier de  https://media.xiph.org/video/derf/

## Key Reference

For those interested in diving deeper into the topic,
Gunnar Farnebäck, « Two-frame motion estimation based on polynomial
expansion », Proceedings of the 13th Scandinavian conference on Image analysis (SCIA'03),
Josef Bigun and Tomas Gustavsson (Eds.). Springer-Verlag, Berlin, Heidelberg, 2003, p. 363-
370

## Setup and Installation

1. Clone this repository:

2. Install the required dependencies:

4. Run the main script:
python main.py
