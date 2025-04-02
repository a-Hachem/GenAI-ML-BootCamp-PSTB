number = 1

def calculate () :
    return 2 + number

# ligne de code necessaire si mon fichier 
# est un module que j'importe dans d'autre fichier
if __name__ == "__main__" :
    print("je suis dans le fichier calculus")
    # si j'execute le ficheir calculus alors affiche moi cette ligne
    # sinon, si je ne fais que importer ce fichier
    # par exemple comme dans le fichier test
    # ne m'affiche pas cette ligne
    