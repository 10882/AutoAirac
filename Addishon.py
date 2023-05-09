
def addNDB():
    content = ''' 
 2  54.005056000   48.231130000        0     1230    50      0.000   MS ENRT UW SOLD-TASHLA NDB
 2  54.017588000   48.309788000        0     1630    50      0.000   SL ENRT UW SOLD-TASHLA-FIELD NDB'''
    fle = open('earth_nav.dat', 'a')
    fle.write(content)
    fle.close