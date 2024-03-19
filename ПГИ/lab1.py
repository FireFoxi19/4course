
def GetMonochromePalatte(palette):
    monohrome_palette = bytearray()
    for i in range(0, len(palette), 4):
        color = sum(palette[i:i+3]) // 3
        monohrome_palette.extend([color, color, color, 0])
    return monohrome_palette

def SaveFile(head,palette,File):
    with open('newCat.BMP', 'wb') as newFile:
        newFile.write(head)
        newFile.write(palette)
        newFile.write(File.read())

def Convert(fileName):
    myFile = open(fileName, 'rb')
  
    head = myFile.read(54)
    palette = myFile.read(1024)


    typeFile = head[:2].decode('utf-8') #узнаем что файл BM
    size = int.from_bytes(head[2:6], byteorder='little')
    arr = int.from_bytes(head[10:14], byteorder='little')
    width = int.from_bytes(head[18:22], byteorder='little')
    height = int.from_bytes(head[22:26], byteorder='little')
    depth = int.from_bytes(head[28:30], byteorder='little')


    rez1 = int.from_bytes(head[6:8], byteorder='little')
    rez2 = int.from_bytes(head[8:10], byteorder='little')

    #print(f"head: {head_int}")
    print(f"width: {width}")
    print(f"height: {height}")
    print(f'type file: {typeFile}')
    print(f'size: {size} bytes')
    print(f'depth: {depth}')
    print(f'arr pixels: {arr}')

    print(f'rez1: {rez1}')
    print(f'rez2: {rez2}')

    palette = GetMonochromePalatte(palette)
    SaveFile(head,palette,myFile)

if __name__ == '__main__':

     fileName = 'CAT256.BMP'
     Convert(fileName)