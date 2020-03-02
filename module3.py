from sklearn.datasets import load_sample_image
from sklearn.feature_extraction import image
# Use the array data from the first image in this dataset:
one_image = load_sample_image("china.jpg")
print('Image shape: {}'.format(one_image.shape))
patches = image.extract_patches_2d(one_image, (2, 2))
print('Patches shape: {}'.format(patches.shape))
# Here are just two of these patches:
print(patches[1]) 

print(patches[800])
