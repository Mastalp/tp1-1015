import tuiles

colormap = tuiles.colormap
image = tuiles.images
setScreenMode(32,32)

largeur = 16 # dependamment de la source
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
    positionInitial = 0
    for i in range(x,largeur):
        for j in range(y,largeur):
            color = int(numberString[pos])
            setPixel(j, i, colormap[color])
            pos+=1                                     
        
def afficherTuile(x, y, tuile):
    tuile=image[tuile]
    x=int(x*4)
    positionInitial=0
    for i in range((0 + x), (x+16)):
        for j in range((0 + x), (x+16)):
            afficherImage(x, y, colormap, tuile)
            
                
afficherTuile(3,4,4)
            