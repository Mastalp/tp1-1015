import tuiles

colormap = tuiles.colormap
image = tuiles.images

largeur = len(image[0]) # dependamment de la source
screenWidth = getScreenWidth()
N = int(screenWidth/largeur)


def afficherImage(x, y, colormap, image):
    tab = image
# extraction de valeurs colormap pour une tuile dans une string
    numberString = ''
    for i in tab.copy():
        for j in i:
            numberString += str(j)
    pos = 0

    for i in range(x,largeur+x):
        for j in range(y,largeur+y):
            color = int(numberString[pos])
            setPixel(j, i, colormap[color])
            pos+=1

            
def afficherTuile(x, y, tuile):
    tuile=image[tuile]
    x=x*largeur
    y=y*largeur
    afficherImage(x, y, colormap, tuile)

    
def attendreClic():
    attendre = True
    while attendre == True:
        x = getMouse()
        sleep(0.01)
        if x.button == 1:
            attendre = False
    return x.x, x.y

sol = []

def permutationAleatoire(n):

    # on cree un tableau de valeurs de 0 a N*N-1
    tableau=[]
    for k in range(n):
        tableau.append(k)

    # dans la solution finale, le 0 est a la fin
    # on sauve la solution dans une variable globale
    global sol
    sol = tableau.copy()
    sol.pop(0)
    sol.append(0)

    # On utilise l'alorithme qui se trouve les powerpoints
    (n)==len(tableau)
    arrayAleatoire=[]
    for i in range(len(tableau)-1, -1, -1): # brasser les cartes Marc Feeley#8 & p.57
        j = math.floor(random() * (i+1))
        temp = tableau[i]
        tableau[i] = tableau[j]
        tableau[j] = temp
        arrayAleatoire.append(tableau[i])
    # on retourne le tableau aleatoire
    return arrayAleatoire


def position(tab, x):
    # retourne l'index de x dans tab
        for i in range(len(tab)):
            if tab[i] == x:
                return i
        return -1
    
    
def inversions(tab, x):
    # on cree un tableau des elements suivant x
    tab2 = tab.copy()
    tab2 = tab[position(tab,x)+1:len(tab):1]
    tab3 = []
    # on cree un autre tableau ou on ajoute seulement les elements
    # plus petits que x et qui ne sont pas 0 
    for j in tab2:
        if j < x and j != 0:
            tab3.append(j)
                    
    return len(tab3)


def soluble(tab):
    # r represente la range de la case noire ( 1 a 4)
    # on l'additionne a la somme ssi largeur est paire
    somme = 0
    r = math.ceil((position(tab, 0)+1)/N)
    for i in range(len(tab)):
        k = inversions(tab, i)
        somme += k
        
    if N % 2 == 0:
        somme += r
    # si la somme est paire, le tableau est soluble
    if somme % 2 == 0:
        return True
    else:
        return False
    
globTab = []
    
def initial(largeur):
    # on initialise le jeu avec une grille de largeur*16 pixels
    tuilePixels = len(image[0]) # dependamment de la source
    setScreenMode(largeur*tuilePixels, largeur*tuilePixels)
    
    solution = False
    # La boucle s'effectue tant qu'un tableau soluble n'est pas cree
    while solution == False:
        c = permutationAleatoire(largeur*largeur)
        if (soluble(c) == True) and (soluble(c) != sol):
            tableau = c
            solution = True
    # on assigne le tableau soluble a la variable globale globTab        
    global globTab 
    globTab = tableau
    # on affiche les tuiles dans globTab
    pos = 0
    for x in range(largeur):
        for y in range(largeur):
            afficherTuile(x, y, tableau[pos])
            pos += 1
    

def taquin(largeur):
    initial(largeur)
    
    N = largeur
    def trouverIndex(x, y):
        # retourne l'index correspondant a la coordonne x,y sur la grille
        # de tuiles
        #breakpoint()
        tabY = []
        # range de coordonnes possible pour N
        for i in range(1,N+1):
            tabY.append(i)
        # reverse dat pour calculer index
        tabRev = tabY[::-1]         
        # la relation entre l'index et les coordonnees est la suivante   
        indexCase = (x*N) - tabRev[y-1]
        return indexCase
    
    
    def contenuIndice(i, tab):
        # retourne la tuile qui est a l'indice i dans tab
        for j in range(len(tab)):
            #breakpoint()
            if tab[i] == tab[j]:
                return tab[i] 

   # La boucle s'effectue tant que la combinaison gagnante n'est pas atteinte
    solution = False
    
    while solution == False:       
        # on veut trouver les coordonnees de la case noire
        # premierement, on trouve l'index de 0 dans globTab
        caseNoire = position(globTab, 0)
        
        # On veut produire toutes les coordonnes possibles dans une grille
        # de largeur*largeur ainsi que leur indice
        # ex.: (1,1) 0, (1,2), 1, (1,3), 2, ..., (4,4), 15
        posX = 0
        posY = 0
        pos = -1
        
        for i in range(largeur):
                
            posX += 1
            posY = 0
            for j in range(largeur):
                
                posY += 1
                pos += 1
                # si l'index de la paire de coords (x,y) est egal a l'index de la case
                # noire, on sait les coordonnees de la case noire 
                if pos == caseNoire:
                    # coordonnes x, y de la case noire
                    caseNoireX = posX
                    caseNoireY = posY
        #print('i:', caseNoire,'Case Noire x:', caseNoireX, 'y:', caseNoireY) 
        # attendreClic retourne des coordonnes x,y en pixels
        # on les transforme en coordonnes de grille de tuiles
        coord = attendreClic()
        coordX = math.ceil(coord[1] / 16)
        coordY = math.ceil(coord[0] / 16)

        # si on clique sur une case valide, dans l'axe de la case noire, on continue
        if (caseNoireX == coordX) ^ (caseNoireY == coordY):   # xor 
            #print('x:', coordX, 'y:', coordY)
            # on veut trouver l'index de notre clic sur globTab          
            index = trouverIndex(coordX, coordY)
            #print('index', index, 'contenu :', contenuIndice(index,globTab))
            #print('i:', caseNoire,'Case Noire x:', caseNoireX, 'y:', caseNoireY)

            # Si notre clic est dans l'axe des Y, donc dans une colonne
            if coordY == caseNoireY:

                # on commence par construire un tableau compose des index de
                # chaques tuiles dans la colonne

                indexArray = []

                for i in range((index%largeur), largeur*largeur, largeur):
                    # incorporer largeur ici
                    indexArray.append(i)

                # il faut necessairement avoir cliquer sur un des index qui sont 
                # dans indexArray

                              

                def findIndex(n, tab): 
                    # retourne l'index de n dans tab   
                    for i in range(len(tab)):
                        if tab[i] == n:
                            return i                         
                
                # on trouve l'index de notre clic dans indexArray
                subIndex = findIndex(index,indexArray)
                #print('indexArray:',indexArray)
                
                # on cree un tableau qui va servir a afficher la valeurs des tuiles
                # aux index de indexArray en utilisant globTab
                contenu = []  
                for i in indexArray:
                    contenu1 = contenuIndice(i, globTab)
                    contenu.append(contenu1)
                # On sait ou on a clic, on veut maintenant y inserer la case noire
                newContenuArray = contenu.copy()
                # print(caseNoire, indexArray)
                #breakpoint()
                # on pop la case noire dans indexArray et on la reinsere ou on
                # a clic
                newContenuArray.pop(findIndex(caseNoire, indexArray))
                newContenuArray.insert(subIndex ,0)
                
                # on insere les nouvelles valeurs de la colonne dans le tableau global
                for i in range(len(indexArray)):
                    # 0,1,2,3
                    globTab[indexArray[i]] = newContenuArray[i]
                print(globTab, indexArray)      

               # si notre clic est dans l'axe des X, donc dans une rangee
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
        # si l'état de globTab est = a la solution, on a gagne
        if globTab == sol:
            solution == True
            break
        #breakpoint()    
        sleep(0.25)
        
       
    alert('VOUS AVEZ GAGNE')
    
    taquin(largeur)
    
taquin(4)