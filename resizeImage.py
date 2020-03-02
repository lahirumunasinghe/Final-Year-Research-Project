import image_slicer

def imSlice(pathImg):
    path ='/home/lahiru/PycharmProjects/untitled/malignant/1.jpg'
    tiles = image_slicer.slice(pathImg, 9, save=False)
    image_slicer.save_tiles(tiles, directory='/home/lahiru/PycharmProjects/untitled/SliceImage',\
                            prefix='slice', format='png')


#imSlice('/home/lahiru/PycharmProjects/untitled/malignant/1.jpg')
