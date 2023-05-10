from PIL import Image, ImageDraw, ImageFont
import cv2
import urllib.request


def formato(url):
    print(url)
    urllib.request.urlretrieve(url, "imageModifyCSS/local.jpg")
    im_v = Image.open("imageModifyCSS/local.jpg")
    width, height = im_v.size
    # print(width,height)

    if width != height:
        if width > height:
            difference = width - height
            oip_to_resize = Image.open('imageModifyCSS/OIP.jpeg')
            oip_resized = oip_to_resize.resize((width, int(difference / 2)))
            oip_resized.save('imageModifyCSS/OIP.jpeg')

            # Vertical images concatenation pt1
            product = cv2.imread('imageModifyCSS/local.jpg')
            oip = cv2.imread('imageModifyCSS/OIP.jpeg')
            im_v = cv2.vconcat([oip, product, oip])

        elif width < height:
            difference = height - width
            oip_to_resize = Image.open('imageModifyCSS/OIP.jpeg')
            oip_resized = oip_to_resize.resize((int(difference / 2), height))
            oip_resized.save('imageModifyCSS/OIP.jpeg')

            # Horizontal images concatenation pt1
            product = cv2.imread('imageModifyCSS/local.jpg')
            oip = cv2.imread('imageModifyCSS/OIP.jpeg')
            im_v = cv2.hconcat([oip, product, oip])
        cv2.imwrite('imageModifyCSS/local.jpg', im_v)

    # Image concatenation pt2
    r2_product = Image.open("imageModifyCSS/local.jpg")
    r2_product = r2_product.resize((1000, 1000))
    r2_product.save('imageModifyCSS/local.jpg')
    width, height = r2_product.size
    # print(width, height)

    # left oip (space for pudding)
    left_to_resize = Image.open('imageModifyCSS/OIP.jpeg')
    left_resized = left_to_resize.resize((20, height))
    left_resized.save('imageModifyCSS/left_pudding.jpeg')

    # right oip (space for price)
    right_to_resize = Image.open('imageModifyCSS/OIP.jpeg')
    right_resized = right_to_resize.resize((700, height))
    right_resized.save('imageModifyCSS/right_pudding.jpeg')

    product = cv2.imread('imageModifyCSS/local.jpg')
    left = cv2.imread('imageModifyCSS/left_pudding.jpeg')
    right = cv2.imread('imageModifyCSS/right_pudding.jpeg')
    im_h = cv2.hconcat([left, product, right])

    cv2.imwrite('imageModifyCSS/local.jpg', im_h)

def draw(sconto, prezzoscontato, prezzoiniziale):
    img_not_drawed = Image.open("imageModifyCSS/local.jpg")
    I1 = ImageDraw.Draw(img_not_drawed)

    myFont = ImageFont.truetype('imageModifyCSS/Metropolis-ExtraBold.otf', 120)  # +30 per prezzi senza centesimi
    sconto = '-{}'.format(str(sconto))
    size = myFont.getsize(sconto)
    I1.text((1720 - size[0] - 50, 280), sconto, font=myFont, fill=(255, 0, 0))  # 1350

    myFont = ImageFont.truetype('imageModifyCSS/Metropolis-ExtraBold.otf', 180)  # +30 per prezzi senza centesimi
    prezzoscontato = f'{prezzoscontato}'
    # print(prezzoscontato)
    size = myFont.getsize(prezzoscontato)
    I1.text((1720 - size[0] - 50, 420), prezzoscontato, font=myFont, fill=(0, 0, 0))  # 1150

    myFont = ImageFont.truetype('imageModifyCSS/Metropolis-ExtraBold.otf', 90)  # +30 per prezzi senza centesimi
    prezzoiniziale = f'{prezzoiniziale}'
    # print(prezzoiniziale)
    size = myFont.getsize(prezzoiniziale)
    I1.text((1720 - size[0] - 50, 620), prezzoiniziale, font=myFont, fill=(0, 0, 0))  # 1400

    img_not_drawed.save("imageModifyCSS/local.jpg")

def border():
    size_verticals = (1720 + 21 * 2, 21)
    size_laterals = (21, 1000)

    # resize borders
    top = Image.open('imageModifyCSS/top.png')
    top = top.resize(size_verticals)
    top.save('imageModifyCSS/top.png')

    bottom = Image.open('imageModifyCSS/bottom.png')
    bottom = bottom.resize(size_verticals)
    bottom.save('imageModifyCSS/bottom.png')

    left = Image.open('imageModifyCSS/left.png')
    left = left.resize(size_laterals)
    left.save('imageModifyCSS/left.png')

    right = Image.open('imageModifyCSS/right.png')
    right = right.resize(size_laterals)
    right.save('imageModifyCSS/right.png')

    # Merge images
    product = cv2.imread('imageModifyCSS/local.jpg')
    left = cv2.imread('imageModifyCSS/left.png')
    right = cv2.imread('imageModifyCSS/right.png')
    border_h = cv2.hconcat([left, product, right])
    cv2.imwrite('imageModifyCSS/local.jpg', border_h)
    product = cv2.imread('imageModifyCSS/local.jpg')
    top = cv2.imread('imageModifyCSS/top.png')
    bottom = cv2.imread('imageModifyCSS/bottom.png')
    border_v = cv2.vconcat([top, product, bottom])
    cv2.imwrite('imageModifyCSS/local.jpg', border_v)

def imageStyle(imageUrl, strikePrice, oldPrice, discount):
    formato(imageUrl)
    draw(discount, strikePrice, oldPrice)
    border()