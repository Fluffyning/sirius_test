from PIL import Image
import matplotlib.pyplot as plt

if __name__=='__main__':
    img = Image.open('memes/meme_2.png')

    plt.imshow(img)
    plt.axis('off')
    plt.show()