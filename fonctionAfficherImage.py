#Hugo de Sousa, Matricule: 20220364
#Louis-Philippe Roy-Lemaire, Matricule:20074007


import tuiles

#Viens de tuiles.py qui sert a obtenir les donnees pour les couleurs et les chiffres/nombres
colormap = tuiles.colormap
image = tuiles.images

#largeur prend l'index de n'importe quelle image et le considere comme le nombre de pixel necessaire pour le dessiner
largeur = len(image[0]) 
screenWidth = getScreenWidth()
#N calcule le screenWidth en considerant les dimensions du carre et la largeur de chaque image, donc un 3x3 sera 48px par 48px car 16(largeur) fois 3 equale 48.
N = int(screenWidth/largeur)

#La procedure afficherImage prend en parametres une coordonne x et y pour determiner a partir de quelles pixels les couleurs commenceront a s'afficher. Les deux autres parametres colormap et image sont utiliser pour determiner la couleur de chaque pixels pour une certaine image.
def afficherImage(x, y, colormap, image):
    tab = image
    #Extraction des valeurs colormap
    numberString = ''
    for i in tab.copy():
        for j in i:
            numberString += str(j)

    #Accumulateur        
    pos = 0

    #En prenant compte des parametres x et y comme position initiale, l'accumulateur passe a travers les valeurs colormap extraitent et les affichent avec setPixel
    for i in range(x,largeur+x):
        for j in range(y,largeur+y):
            color = int(numberString[pos])
            setPixel(j, i, colormap[color])
            pos+=1

#La procedure afficherTuile prend en parametre x et y defini la position de l'image similairement a des coordonnees dans une grille. Le parametre tuile affiche le chiffre/nombre inserer.            
def afficherTuile(x, y, tuile):
    tuile=image[tuile]
    #Multiplier par la largeur dune case pour espacer chaque image
    x=x*largeur
    y=y*largeur
    afficherImage(x, y, colormap, tuile)

#La fonction attendreClic retourne les coordonnees d'ou la personne a lacher le bouton de sa souris. Lorsque le bouton est lacher, x.button == 1 et la boucle se termine.    
def attendreClic():
    attendre = True
    while attendre == True:
        x = getMouse()
        sleep(0.01)
        if x.button == 1:
            attendre = False
    return x.x, x.y

sol = []
#La fonction permutationAleatoire retourne des compositions de table aleatoire selon la longueur du tableau.
def permutationAleatoire(n):
    tableau=[]
    for k in range(n):
        tableau.append(k)

    #Definie la solution gagnante  
    global sol
    sol = tableau.copy()
    sol.pop(0)
    sol.append(0)


    #Cette methode de brassage se differencie a la methode naive grace au deplacement progressif dans le tableau apres avoir swap les chiffres. (Src = Notes #8 Marc Feeley, p.57)
    (n)==len(tableau)
    arrayAleatoire=[]
    for i in range(len(tableau)-1, -1, -1):
        j = math.floor(random() * (i+1))
        temp = tableau[i]
        tableau[i] = tableau[j]
        tableau[j] = temp
        arrayAleatoire.append(tableau[i])

    return arrayAleatoire

#Une fonction utiliser localement dans la fct inversions(tab, x) servant a trouver la position "x" dans l'index de la tab evaluer
def position(tab, x):
        for i in range(len(tab)):
            if tab[i] == x:
                return i
        return -1
    
#La fonction inversions prend en parametre un tableau et un "x" et retourne un tableau (et sa longueur) avec les valeurs plus petites que "x" dans le reste de l'index.    
def inversions(tab, x):

    tab2 = tab.copy()
    tab2 = tab[position(tab,x)+1:len(tab):1]
    tab3 = []
    
    for j in tab2:
        if j < x and j != 0:
            tab3.append(j)
                    
    return len(tab3)

def soluble(tab):
    somme = 0
    r = math.ceil((position(tab, 0)+1)/N)
    for i in range(len(tab)):
        k = inversions(tab, i)
        somme += k
        
    if N % 2 == 0:
        somme += r
    
    if somme % 2 ==0:
        return True
    else:
        return False
    
globTab = []
    
def initial(largeur):
    tuilePixels = len(image[0]) # dependamment de la source
    setScreenMode(largeur*tuilePixels, largeur*tuilePixels)
    
    #global sol
    solution = False
    
    while solution == False:
        c = permutationAleatoire(largeur*largeur)
        if (soluble(c) == True) and (soluble(c) != sol):
            tableau = c
            solution = True
            
    global globTab 
    globTab = tableau
    
    pos = 0
    for x in range(largeur):
        for y in range(largeur):
            afficherTuile(x, y, tableau[pos])
            pos += 1
    

def taquin(largeur):
    initial(largeur)
    # on veut trouver les coordonnes de la case noire
    N = largeur
    def trouverIndex(x, y):
       
        #breakpoint()
        tabY = []
            # range de coordonnes possible pour N
        for i in range(1,N+1):
            tabY.append(i)
            # reverse dat pour calculer index
        tabRev = tabY[::-1]            
        indexCase = (x*N) - tabRev[y-1]
        return indexCase
    
    
    def contenuIndice(i, tab):
        for j in range(len(tab)):
            #breakpoint()
            if tab[i] == tab[j]:
                return tab[i] 
   
    solution = False
    
    while solution == False:       
        caseNoire = position(globTab, 0)
        
        posX = 0
        posY = 0
        pos = -1
        
        for i in range(largeur):
                
            posX += 1
            posY = 0
            for j in range(largeur):
                
                posY += 1
                pos += 1
                
                if pos == caseNoire:
                    # coordonnes x, y de la case noire
                    caseNoireX = posX
                    caseNoireY = posY
        #print('i:', caseNoire,'Case Noire x:', caseNoireX, 'y:', caseNoireY)            
        coord = attendreClic()
        coordX = math.ceil(coord[1] / 16)
        coordY = math.ceil(coord[0] / 16)
        # si on clique sur une case valide, on continue
        if (caseNoireX == coordX) ^ (caseNoireY == coordY):   # xor 
            print('x:', coordX, 'y:', coordY)
            # on veut trouver l'index de notre clic sur globTab          
            index = trouverIndex(coordX, coordY)
            print('index', index, 'contenu :', contenuIndice(index,globTab))
            print('i:', caseNoire,'Case Noire x:', caseNoireX, 'y:', caseNoireY)
 
            if coordY == caseNoireY:

                indexArray = []
                
                # TO DO
                
                for i in range((index%largeur), largeur*largeur, largeur):
                    # incorporer largeur ici
                    indexArray.append(i)

                # il faut cliquer sur un des index qui sont dans indexArray

                contenu = []                
                
                # findIndex retourne none la premiere fois!!!
                
                def findIndex(n, tab):    
                    for i in range(len(tab)):
                        if tab[i] == n:
                            return i 
                         
                
                subIndex = findIndex(index,indexArray)
                
                print('indexArray:',indexArray)
                
                for i in indexArray:
                    contenu1 = contenuIndice(i, globTab)
                    contenu.append(contenu1)

                newContenuArray = contenu.copy()
                print(caseNoire, indexArray)
                #breakpoint()
                newContenuArray.pop(findIndex(caseNoire, indexArray))
                newContenuArray.insert(subIndex ,0)
                
                for i in range(len(indexArray)):
                    # 0,1,2,3
                    globTab[indexArray[i]] = newContenuArray[i]
                print(globTab, indexArray)      
               # easy
            elif coordX == caseNoireX:
                globTab.pop(caseNoire)
                globTab.insert(index, 0)
                
            
                
                
            # re affiche globTab qui est updated a chaque clic
        pos = 0
        for x in range(largeur):
            for y in range(largeur):
                afficherTuile(x, y, globTab[pos])
                pos += 1
        
        
        
        print(globTab, sol)
        
        if globTab == sol:
            solution == True
            break
        #breakpoint()    
        sleep(0.25)
        
       
    alert('VOUS AVEZ GAGNE')
    
    taquin(largeur)
    
taquin(4)