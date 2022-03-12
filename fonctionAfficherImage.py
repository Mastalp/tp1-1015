import tuiles
colormap = tuiles.colormap
image = tuiles.images
setScreenMode(16,16)

largeur = len(image[0]) # dependamment de la source
screenWidth = getScreenWidth()
N = int(screenWidth/16)


def afficherImage(x, y, colormap, image):
    tab = image
    # extraction de valeurs colormap pour une tuile dans une string
    numberString = ''
    for i in tab.copy():
        for j in i:
            numberString += str(j)
    pos = 0
    for i in range(x):
        for j in range(y):
            color = int(numberString[pos])
            setPixel(j, i, colormap[color])
            pos += 1
            