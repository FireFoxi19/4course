
from FileOpener import *



class PCXConverter:
    def __init__(self, outputColorNum, filename):
        self.outputColorNum = outputColorNum
        with open(filename, 'rb') as file:
            self.header = file.read(128)
        
            self.depth = int.from_bytes(self.header[3:4], 'little')
        
            self.width = self.header[8] + (self.header[9] << 8) - self.header[4] - (self.header[5] << 8) + 1
            self.height = self.header[10] + (self.header[11] << 8) - self.header[6] - (self.header[7] << 8) + 1
        
            file.seek(-768, 2)
            self.palette = np.frombuffer(file.read(), dtype=np.uint8).reshape((256, 3))
            self.graphImg = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
            file.seek(128)
            x, y = 0, 0
            while y < self.height:
                x = 0
                while x < self.width:
                    binByte = file.read(1)
                    byte = int.from_bytes(binByte, 'little')
                    if byte < 192:
                        self.graphImg[y, x] = self.palette[byte]
                        x += 1
                    else:
                        count = byte - 192
                        binRepeatedByte = file.read(1)
                        repeatedByte = int.from_bytes(binRepeatedByte, 'little')
                        if count == 1 and repeatedByte == 0: continue
                    
                        for _ in range(count):
                            if x >= self.width: break
                            self.graphImg[y, x] = self.palette[repeatedByte]
                            x += 1
                y += 1
                
            plt.figure()
            plt.imshow(self.graphImg)
            plt.axis('off')

    def Convert(self):
        self.newPalette = self.GenerateNewPalette(self.graphImg, self.width, self.height)
        dictPalette = {self.newPalette[i]: i for i in range(len(self.newPalette))}
        imgBytes = []
        
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                self.graphImg[y, x] = self.GetSimilarColor(self.newPalette, self.graphImg[y, x])
                colorInd = dictPalette.get(tuple(self.graphImg[y, x]))
                if colorInd == None:
                    colorInd = 0
                imgBytes.append(colorInd)
                 
        self.imgZipBytes = []       
        for i in range(0, len(imgBytes), 2):
            colorByte = 0
            pixel1 = (colorByte | imgBytes[i]) << 4
            pixel2 = pixel1 | imgBytes[i + 1]
            self.imgZipBytes.append(pixel2)
        
        self.WriteOutputFile()
        
    def WriteOutputFile(self):
        bmpHeader = bytearray()

        headerSize = 54
        paletteSize = 4 * 16
        
        bmpHeader.extend(b'BM')
        bmpHeader.extend(int(self.width * self.height // 2 + paletteSize + headerSize).to_bytes(4, 'little'))   
        bmpHeader.extend(b'\x00\x00\x00\x00')
        bmpHeader.extend(int(paletteSize + headerSize).to_bytes(4, 'little'))
        
        bmpHeader.extend(int(40).to_bytes(4, 'little'))
        bmpHeader.extend(int(self.width).to_bytes(4, 'little'))
        bmpHeader.extend(int(self.height).to_bytes(4, 'little'))
        # Planes
        bmpHeader.extend(int(1).to_bytes(2, 'little'))
        # bit count
        bmpHeader.extend(int(4).to_bytes(2, 'little'))
        # compression
        bmpHeader.extend(int(0).to_bytes(4, 'little'))
        # compressed size
        bmpHeader.extend(int(0).to_bytes(4, 'little'))
        # pix per m X
        bmpHeader.extend(int(0).to_bytes(4, 'little'))
        # pix per m Y
        bmpHeader.extend(int(0).to_bytes(4, 'little'))
        # used colors
        bmpHeader.extend(int(0).to_bytes(4, 'little'))
        # important colors
        bmpHeader.extend(int(0).to_bytes(4, 'little'))
        
        paletteBytes = []
        for color in self.newPalette:
            r, g, b = color
            paletteBytes.extend([b, g, r, 0])

        with open('converted_pcx.bmp', 'wb') as f:
            f.write(bytes(bmpHeader))
            f.write(bytes(paletteBytes))
            f.write(bytes(self.imgZipBytes))

    def Show(self):
        plt.figure()
        plt.imshow(self.graphImg)
        plt.axis('off')
        plt.show()

    def CountDelta(self, left, right):
        return sum([(x - y) ** 2 for x, y in zip(left, right)])

    def GenerateNewPalette(self, pixels, width, height):
        colors = {}
        for y in range(height):
            for x in range(width):
                flattenColor = (pixels[y, x][0] >> 4 << 4, pixels[y, x][1] >> 4 << 4, pixels[y, x][2] >> 4 << 4)
                colors[flattenColor] = colors[flattenColor] + 1 if flattenColor in colors else 1
            
        colors = list(colors.items())
        colors.sort(key=lambda x: x[1], reverse=False)

        newPalette = []
        newPalette.append(colors.pop()[0])
        newColorCount = 1
    
        while newColorCount < self.outputColorNum:
            newColor = colors.pop()[0]
            for color in newPalette:
                if 128*128*3 < self.CountDelta(color, newColor):
                    newPalette.append(newColor)
                    newColorCount += 1
                    break
            
        return newPalette

    def GetSimilarColor(self, palette, color):
        similarColor = (0, 0, 0)
        for paletteColor in palette:
            if self.CountDelta(similarColor, color) > self.CountDelta(paletteColor, color):
                similarColor = paletteColor
        return similarColor

class LabSystem:

    def lab3(self):
        converter = FileOpener('fish.BMP')
        converter.Read()
        converter.obj.Print()
        converter.obj.RotateImg() 

    def lab4(self):
        converter = FileOpener('CAT16.BMP')
        converter.Read()
        #converter.obj.Print()
        converter.obj.PutPixelImg() 
    
        converter1 = FileOpener('CAT256.BMP')
        converter1.Read()
        #converter1.obj.Print()
        converter1.obj.PutPixelImg() 
    
        converter2 = FileOpener('fish.BMP')
        converter2.Read()
        #converter2.obj.Print()
        converter2.obj.PutPixelImg() 
    
        plt.show()

    def lab5(self):
        converter = FileOpener('CAT256.BMP')
        converter.Read()
        #converter.obj.Print()
        converter.obj.Scale(5) 

    def lab6(self):
        converter = FileOpener('fish.BMP')
        converter.Read()
        #converter.obj.Print()
        converter.obj.AddLogo('logo.BMP', 0.5) 
    
        plt.show()
    
    def lab7(self):
        converter = FileOpener('fish.BMP')
        converter.Read()
        #converter.obj.Print()
        converter.obj.EncodeText(0.5) 
        converter.obj.DecodeText() 
        plt.show()
   
    def lab8(self):
        converter = PCXConverter(16, "200001.pcx")
        converter.Show()

    def one(self):
        pcxFile = PCXConverter(16, "200001.pcx")
        pcxFile.Convert()
        pcxFile.Show()

def main():
    labs = LabSystem()
    #labs.lab3()
    #labs.lab4()
    #labs.lab5()
    labs.lab6()
    #labs.lab7()
    #labs.lab8()

if __name__ == '__main__':
    main()
