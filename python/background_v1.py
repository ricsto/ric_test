#background acquisition before the movie:
#sys.path.append('C:\Users\mqbphrs3\Desktop\PYTHON_CODE')
#import background_v1 as bg
from psychopy import visual
from psychopy import core
import serial
import scipy as sc


def run():
    
    im = sc.loadtxt("C:\\Users\\mqbphrs3\\Desktop\\PYTHON_CODE\\image_stimuli\\static_images\\image_white_bg.txt")
    im[:,:] = -0.6
    ser = serial.Serial(2,9600,timeout=1)
    core.wait(2)
    #myWin = visual.Window((1920,1080),  pos = (0,0), allowGUI=False, fullscr=True,monitor='testMonitor', units='pix', screen = 1, color = -0.7)
    myWin = visual.Window((1920,1080),  pos = (0,0), allowGUI=False, fullscr=True,monitor='testMonitor', units='pix', screen = 1, color = -0.6)
    #start acquisition 
    for n in range(100):
        myWin.flip()
        ser.write('4')
        core.wait(0.05)
    #close serial & window
    myWin.close()
    ser.close()