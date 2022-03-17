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
    tableau=[]
    for k in range(n):
        tableau.append(k)
        
    global sol
    sol = tableau.copy()
    sol.pop(0)
    sol.append(0)

    (n)==len(tableau)
    arrayAleatoire=[]
    for i in range(len(tableau)-1, -1, -1): # brasser les cartes Marc Feeley#8 & p.57
        j = math.floor(random() * (i+1))
        temp = tableau[i]
        tableau[i] = tableau[j]
        tableau[j] = temp
        arrayAleatoire.append(tableau[i])

    return arrayAleatoire


def position(tab, x):
        for i in range(len(tab)):
            if tab[i] == x:
                return i
        return -1
    
    
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