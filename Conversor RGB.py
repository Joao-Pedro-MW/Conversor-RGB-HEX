def rgb(r, g, b):
    
    if r>255 : r=255
    if g>255 : g=255
    if b>255 : b=255
    if r<0 : r= 0
    if g<0 : g= 0
    if b<0 : b= 0
    
    r = '{:02X}'.format(r)
    g = '{:02X}'.format(g)
    b = '{:02X}'.format(b)
    a = '{0}{1}{2}'.format(r,g,b)
    a = a.upper() 
    return a