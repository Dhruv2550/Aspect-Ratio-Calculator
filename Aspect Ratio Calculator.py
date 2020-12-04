def aspect_ratio(w, h, nw, nh,nratio):

    if nratio == 'width':
        nw = int(input("Enter the New Width\n"))
        if w - h < 0:
            nh = nw * (h / w)
        else:
            nh = nw / (w / h)

    elif nratio == 'height':
        nh = int(input("Enter the New Height\n"))
        if w - h > 0:
            nw = nh / (h / w)
        else:
            nw = nh * (w / h)

    return nw,nh


print("Aspect Ratio Calculator")
print('-'*30)
quit=''
while quit=='':
    w = int(input("What is the existing width"))
    h = int(input("What is the existing height"))

    nratio = input('Do you want to provide a new width or height')
    nh = 0
    nw = 0

    dimensions = aspect_ratio(w, h, nw, nh,nratio)

    print(f'The New Dimensions are {dimensions}')
    print('-'*30)
    quit=input('Press Enter to Calculate Another Ratio or Press any other Key to Quit')
