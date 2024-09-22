from PIL import Image
import matplotlib.pyplot as plt

if __name__=='__main__':
    img = Image.open('memes/meme_2sdfgfd.png')

    plt.imshow(img)
    plt.axis('off')
    plt.show()