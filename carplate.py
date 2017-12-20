import numpy as np
import cv2
import imageio

PLATE_WIDTH     = 1024
PLATE_HEIGHT    = 256
Lambda = 205    # Color base (minimum)
Kappa = 50      # Color "+" deviation (added to the base)

def getPlates(batch_size = 32):
    plates = np.ndarray(shape = (batch_size,PLATE_HEIGHT,PLATE_WIDTH,3) )
    for i in range (0, batch_size):
        NUMBER_LETTERS = 5+np.random.randint(5)
        LETTER_SIZE     = 180
        LETTER_WIDTH    = round((0.63)*LETTER_SIZE)
        text_width = LETTER_WIDTH*NUMBER_LETTERS
        loc_x = PLATE_WIDTH/6#round((PLATE_WIDTH - text_width) / 2))
        loc_y = round((PLATE_HEIGHT- LETTER_SIZE)/ 2) + np.random.randint(10) 
        img = 255*np.ones([PLATE_HEIGHT,PLATE_WIDTH,3], dtype = np.uint8)
        
        if (np.random.rand()>0.7):
            s1 = np.random.randint(Kappa)+Lambda
            s2 = np.random.randint(Kappa)+Lambda
            s3 = np.random.randint(Kappa)+Lambda 
            img[:,:,0] = s1
            img[:,:,1] = s2
            img[:,:,2] = s3
        
        s1 = np.random.randint(255)
        s2 = np.random.randint(255)
        s3 = np.random.randint(255)
        img[:,0:round(PLATE_WIDTH/8),0] = s1  
        img[:,0:round(PLATE_WIDTH/8),1] = s2  
        img[:,0:round(PLATE_WIDTH/8),2] = s3  
        img = Image.fromarray(img, 'RGB')
        draw = ImageDraw.Draw(img)
        
        # REGION
        font = ImageFont.truetype("EuroPlate.ttf", 90)
        text = ''    
        for j in range (0, 2):
            text += (random.choice(string.ascii_letters)).lower()
        draw.text((15, PLATE_HEIGHT*2/4),text,(0,0,0),font=font)
        fstring=text
        # FLAG if region generated existed country
        c=0
        try:
            flag = Image.open('flags/'+text+'.png'); flag = flag.convert('RGB'); 
            img.paste( flag, (round(PLATE_WIDTH/34), np.random.randint(80) ))
        except:
            c=c+1
          
        #NUMBER
        font = ImageFont.truetype("EuroPlate.ttf", LETTER_SIZE)
        text = ''
        for j in range (0, NUMBER_LETTERS):
            text += random.choice(string.ascii_letters+'     '+'1234567890')
        draw.text((loc_x, loc_y),text,(0,0,0),font=font)

        plates[i,...] = img
    return np.array(plates, dtype=np.uint8)