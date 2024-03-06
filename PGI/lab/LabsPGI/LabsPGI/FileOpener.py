import random
import math
import numpy as np
import matplotlib.pyplot as plt
from FileOpener import *
BMP_HEADER_BSIZE = 14
BMP_INFO_HEADER_BSIZE = 40

class Converter:
    def __init__(self, name):



        self.name = name
        self.fileObj = None
        self.header = None
        self.infoHeader = None
        self.palette = None  
        self.paletteSize = None
        self.colorCount = None
        self.bpp = None
        self.padding = None
        self.type = None
        self.size = None
        self.reserved = None
        self.offset = None
        self.infoHeaderSize = None
        self.width = None
        self.height = None 
        self.planes = None
        self.depthColor = None
        self.compression = None
        self.compressedSize = None
        self.xPixPM = None
        self.yPixPM = None
        self.usedColors = None
        self.importantColors = None


    def Print(self):
        print("header information:\n\n")
        print(f"type file: {self.type}")
        print(f"size file: {self.size}")
        print(f"res: {self.reserved}")
        print(f"data offset: {self.offset}")
        print(f"size head: {self.infoHeaderSize}")
        print(f"width: {self.width}")
        print(f"height: {self.height}")
        print(f"planes: {self.planes}")
        print(f"depth color: {self.depthColor}")
        print(f"compression: {self.compression}")
        print(f"size compressed: {self.compressedSize}")
        print(f"X res: {self.xPixPM}")
        print(f"Y res: {self.yPixPM}")
        print(f"colors: {self.usedColors}")
        print(f"all colors: {self.importantColors}")
        print() 
    
    #lab 3                
    def RotateImg(self):
        with open(self.name, 'rb') as originalFile:
            header = originalFile.read(BMP_HEADER_BSIZE + BMP_INFO_HEADER_BSIZE)

            if self.depthColor <= 8:
                palette = originalFile.read(self.paletteSize)
        
            originalPixels = originalFile.read()
            width = self.height
            height = self.width

            with open('new_' + self.name, 'wb') as fileObj:



                header_new = bytearray(header)
                header_new[18:22] = width.to_bytes(4, 'little')
                header_new[22:26] = height.to_bytes(4, 'little')
            
                fileObj.write(header_new)  
                if self.depthColor <= 8:
                    fileObj.write(palette)

                padding = b'\x00' * ((4 - (width * self.bpp) % 4) % 4)

                pixels = bytearray()
                for x in range(self.width):
                    for y in range(self.height):
                        pixelPos = y * self.width * self.bpp + x * self.bpp
                        pixels.extend(originalPixels[pixelPos : (pixelPos + self.bpp)])

                    pixels.extend(padding)
                    
                fileObj.write(pixels)                
    #lab 4
    def PutPixelImg(self):
        with open(self.name, 'rb') as fileObj:



            fileObj.seek(self.offset)
            image = None
        
            if (self.depthColor == 24):
                image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
                
                for y in range(self.height - 1, -1, -1):
                    for x in range(self.width):
                        blue = int.from_bytes(fileObj.read(1), 'little')
                        green = int.from_bytes(fileObj.read(1), 'little')
                        red = int.from_bytes(fileObj.read(1), 'little')
                        image[y, x] = [red, green, blue]
                
                    fileObj.read(self.padding)
                    
            elif (self.depthColor == 8):
                image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
                palette = np.frombuffer(self.palette, dtype=np.uint8).reshape((self.colorCount, 4))
            
                for y in range(self.height - 1, -1, -1):
                    for x in range(self.width):
                        pixel = int.from_bytes(fileObj.read(self.bpp), 'little')
                        image[y, x] = np.flip(palette[pixel, :3])
                    
                    fileObj.read(self.padding)
                    
            elif (self.depthColor == 4):
                padding = (4 - (self.width // 2) % 4) % 4
                image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
                palette = np.frombuffer(self.palette, dtype=np.uint8).reshape((self.colorCount, 4))
            
                for y in range(self.height - 1, -1, -1):
                    for x in range(0, self.width, 2):
                        byteVal = int.from_bytes(fileObj.read(1), 'little')
                        pixel1 = (byteVal >> 4) & 0x0F
                        pixel2 = byteVal & 0x0F
                        image[y, x] = np.flip(palette[pixel1, :3])
                        if x+1 < self.width:
                            image[y, x + 1] = np.flip(palette[pixel2, :3])
                    
                    fileObj.read(padding)
        
        plt.figure()
        plt.imshow(image)
        plt.axis('off')
        return image    
    #lab 5
    def Scale(self, scaleVar):
        with open(self.name, 'rb') as originalFile:
            originalFile.seek(self.offset)
            
            image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            palette = np.frombuffer(self.palette, dtype=np.uint8).reshape((self.colorCount, 4))
            
            for y in range(self.height - 1, -1, -1):
                for x in range(self.width):
                    pixel = int.from_bytes(originalFile.read(self.bpp), 'little')
                    image[y, x] = np.flip(palette[pixel, :3])
                    
                originalFile.read(self.padding)

        newWidth = int(self.width * scaleVar)
        newHeight = int(self.height * scaleVar)
    
        scaledImage = np.zeros((newHeight, newWidth, 3), dtype=np.uint8)
    
        for y in range(newHeight):
            for x in range(newWidth):
                originalX = int(x / scaleVar)
                originalY = int(y / scaleVar)
                scaledImage[y, x] = image[originalY, originalX]
    
        plt.imshow(scaledImage)
        plt.axis('off')
        plt.show()
        return scaledImage    
    #lab 6
    def AddLogo(self, markName, opacity):
        with open(self.name, 'rb') as objFile:
            objFile.seek(self.offset)
            graphImg = np.zeros((self.height, self.width, 3), dtype=np.uint8)
                
            for y in range(self.height - 1, -1, -1):
                for x in range(self.width):
                    blue = int.from_bytes(objFile.read(1), 'little')
                    green = int.from_bytes(objFile.read(1), 'little')
                    red = int.from_bytes(objFile.read(1), 'little')
                    graphImg[y, x] = [red, green, blue]
                
                objFile.read(self.padding)
                
        markFILE = FileOpener(markName)
        markFILE.Read()
        markFILE.obj.Print()
        mark = markFILE.obj
        
        with open(markName, 'rb') as newFile:
            newFile.seek(mark.offset)
                
            for y in range(mark.height - 1, -1, -1):
                for x in range(mark.width):
                    markBlue = int.from_bytes(newFile.read(1), 'little')
                    markGreen = int.from_bytes(newFile.read(1), 'little')
                    markRed = int.from_bytes(newFile.read(1), 'little')
                    if markBlue == 0 and markGreen == 0 and markRed == 0:
                        newFile.read(1)
                        continue
                    
                    blue = markBlue * (1 - opacity) + graphImg[y, x][2] * opacity
                    green = markGreen * (1 - opacity) + graphImg[y, x][1] * opacity
                    red = markRed * (1 - opacity) + graphImg[y, x][0] * opacity
                    newFile.read(1)
                    graphImg[y, x] = [red, green, blue]
                
                newFile.read(mark.padding)
        
        plt.figure()
        plt.imshow(graphImg)
        plt.axis('off')
        return graphImg    
    #lab 7
    def EncodeText(self, sizePercent):
        self.encodeOffset = math.ceil(8 * sizePercent)
        with open('text.txt', 'r') as textFile:
            textBits = ""
            readBitsCount = int(self.compressedSize * sizePercent)
            readBitsCount = (readBitsCount - readBitsCount % 24) * 8
            text = textFile.read()
            for i in text:
                textBits = textBits + bin(ord(i))[2:].zfill(8)
                if len(textBits) >= readBitsCount:
                    break

        with open(self.name, 'rb') as originalFile:
            header = originalFile.read(self.offset)
            graphImg = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            
            for y in range(self.height - 1, -1, -1):
                for x in range(self.width):
                    blue = int.from_bytes(originalFile.read(1), 'little')
                    green = int.from_bytes(originalFile.read(1), 'little')
                    red = int.from_bytes(originalFile.read(1), 'little')
                    graphImg[y, x] = [red, green, blue]
                        
                originalFile.read(self.padding)
            
            bitCounter = 0
            textBitsCount = len(textBits)
            self.textBitsCount = textBitsCount
            
            for y in range(self.height - 1, -1, -1):
                for x in range(self.width):
                    if bitCounter < textBitsCount:
                        for i in range(3):
                            botRowOffset = bitCounter + (self.encodeOffset * i)
                            graphImg[y, x][i] = ((graphImg[y, x][i] >> self.encodeOffset) << self.encodeOffset) | int(textBits[botRowOffset:botRowOffset+self.encodeOffset], 2)
                            
                        bitCounter += self.encodeOffset * 3
                     
            with open('encode_' + str(self.encodeOffset) + self.name, 'wb') as newFile:
                newHeader = bytearray(header)
                newFile.write(newHeader)
                
                newPixels = bytearray()
                for y in range(self.height - 1, -1, -1):
                    for x in range(self.width):
                        blue = int(graphImg[y, x][2]).to_bytes(1, 'little')
                        green = int(graphImg[y, x][1]).to_bytes(1, 'little')
                        red = int(graphImg[y, x][0]).to_bytes(1, 'little')
                        newPixels.extend(blue)
                        newPixels.extend(green)
                        newPixels.extend(red)

                    newPixels.extend(b'\x00' * self.padding)
                    
                newFile.write(newPixels)
            
            plt.figure()
            plt.imshow(graphImg)
            plt.axis('off')
            return graphImg
    
    def DecodeText(self):
        bits = ""
        decodedText = ""
        bitsStr = ""
        bitCounter = 0

        with open('encode_' + str(self.encodeOffset) + self.name, 'rb') as originalFile:
            header = originalFile.read(self.offset)
            
            graphImg = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            
            for y in range(self.height - 1, -1, -1):
                for x in range(self.width):
                    blue = int.from_bytes(originalFile.read(1), 'little')
                    green = int.from_bytes(originalFile.read(1), 'little')
                    red = int.from_bytes(originalFile.read(1), 'little')
                    graphImg[y, x] = [red, green, blue]
                        
                originalFile.read(self.padding)
            
            textBitsCount = self.textBitsCount
            
            for y in range(self.height - 1, -1, -1):
                for x in range(self.width):
                    if bitCounter < textBitsCount:
                        binPowOffset = (pow(2, self.encodeOffset) - 1)
                        bits = bits + bin(graphImg[y, x][0] & binPowOffset)[2:].zfill(self.encodeOffset)
                        bits = bits + bin(graphImg[y, x][1] & binPowOffset)[2:].zfill(self.encodeOffset)
                        bits = bits + bin(graphImg[y, x][2] & binPowOffset)[2:].zfill(self.encodeOffset)
                            
                        bitCounter += self.encodeOffset * 3
                     
            with open('newtext.txt', 'w') as decodedTxt:
                for i in range(0, len(bits), 8):
                    decodedText += chr(int(bits[i:i+8], 2))
                    a = 0
                decodedTxt.write(decodedText)

class FileOpener:
    def __init__(self, fileName):
        self.obj = Converter(fileName)
    def Read(self):
        self.obj.fileObj = open(self.obj.name, 'rb')
        self.obj.header = self.obj.fileObj.read(BMP_HEADER_BSIZE)
        self.obj.type = self.obj.header[:2].decode('utf-8')
        self.obj.size = int.from_bytes(self.obj.header[2:6], 'little')
        self.obj.reserved = int.from_bytes(self.obj.header[6:10], 'little')
        self.obj.offset = int.from_bytes(self.obj.header[10:14], 'little')
        self.obj.infoHeader = self.obj.fileObj.read(BMP_INFO_HEADER_BSIZE)
        self.obj.infoHeaderSize = int.from_bytes(self.obj.infoHeader[:4], 'little')
        self.obj.width = int.from_bytes(self.obj.infoHeader[4:8], 'little')
        self.obj.height = int.from_bytes(self.obj.infoHeader[8:12], 'little')
        self.obj.planes = int.from_bytes(self.obj.infoHeader[12:14], 'little')
        self.obj.depthColor = int.from_bytes(self.obj.infoHeader[14:16], 'little')
        self.obj.compression = int.from_bytes(self.obj.infoHeader[16:20], 'little')
        self.obj.compressedSize = int.from_bytes(self.obj.infoHeader[20:24], 'little')
        self.obj.xPixPM = int.from_bytes(self.obj.infoHeader[24:28], 'little')
        self.obj.yPixPM = int.from_bytes(self.obj.infoHeader[28:32], 'little')
        self.obj.usedColors = int.from_bytes(self.obj.infoHeader[32:36], 'little')
        self.obj.importantColors = int.from_bytes(self.obj.infoHeader[36:40], 'little')
        self.obj.colorCount = pow(2, self.obj.depthColor)
        self.obj.paletteSize = self.obj.colorCount * 4
        self.obj.palette = self.obj.fileObj.read(self.obj.paletteSize)
        self.obj.bpp = self.obj.depthColor // 8
        self.obj.padding = (4 - (self.obj.width * self.obj.bpp) % 4) % 4

        return self.obj.fileObj
    def Rewrite(self, newName):
        with open(newName, 'wb') as newFileObj:           
            newFileObj.write(self.obj.header)
            newFileObj.write(self.obj.infoHeader)
            newFileObj.write(self.obj.palette)
            newFileObj.write(self.obj.fileObj.read())
            newFileObj.close()