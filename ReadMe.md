# Enibot
Enibot est un outil en ligne de commande permettant de télécharger automatiquement l'ebook de notre choix provenant du catalogue de la bibliothèque numérique Eni (site: https://www.editions-eni.fr). On peut aussi voir des informations concernant un livre en particulier si besoin.
## /!\ /!\ /!\ Attention
### Je précise que cette outil est uniquement disponible pour les personnes ayant payé leur accès au catalogue de la bibliothèque Eni et benificiant donc d'un accès à celle-ci.

## Installation
NB: Utiliser l'utilisateur root lors de ces manipulations
```bash
chmod +x ./build/install.sh
./install.sh
```
## Désintallation
NB: Utiliser aussi l'utilisateur root lors de ces manipulations
```bash
chmod +x ./build/uninstall.sh
./uninstall.sh
```
## Utilisation/Exemples
### Configuration des coordonnées de l'utilisateur
```bash
python ./repos/project_script/run_python_script.py config "email" "mot de passe" "portail d'accès"
```
### Télécharger un livre
NB: A la place de l'ISBN (série de 13 chiffres), on peut mettre le numéro de Ref.Eni 
```bash
python ./repos/project_script/run_python_script.py download "nom du livre" "mot de passe" ISBN [ou Ref.Eni]
```
### Regarder les informations sur un livre 
```bash
python ./repos/project_script/run_python_script.py info "nom du livre" "mot de passe" ISBN [ou Ref.Eni]
```
###  Aide (terminal)
```bash
python ./repos/project_script/run_python_script.py help
```

# Support

Dans le cas où vous souhaiteriez me contacter, utilisez cette email: gogolplhex@duck.com.
J'ai aussi developé une interface graphique pour ceux et celles qui ont du mal avec cette outil en ligne de commande et donc dans le cas où vous voudriez y avoir accès faites-le moi savoir, via ce même mail.