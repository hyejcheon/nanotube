import numpy as np               # http://www.numpy.org/
import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu

##fixing numbers, opposite charge : neg/pos

strtype = ['m30m10']#, 'm10m20m10', 'm10m10m10m10']

pathstring  = []

ph = []
linecolor = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['powderblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

for i in range(len(strtype)):
    pathstring.append('alsi/polymer/quenchedpoly/{:s}/'.format(str(strtype[i])))


for j in range(len(pathstring)):
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.list')):
        print(p)  
        d = mu.monAnalysis(p, 'iotube', 'tt')   #choose itube/otube/iotube 
        e = mu.monAnalysis(p, 'itube', 'tt') 
        f = mu.monAnalysis(p, 'otube', 'tt')

        titlestring = '{:s}'.format(p.parts[-4]) 
        labelstring = 'ph = {:d}'.format(int(p.parts[-2][2]))
        
        print(p.parts)
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])
        #reetemp = d

        
        plt.figure(1)
        #plt.subplot(311)        
        plt.plot(d[:,0], d[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of inner/outer tube surface')
        
        
        plt.figure(2)
        #plt.subplot(312)        
        plt.plot(e[:,0], e[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of inner tube surface')
        
        
        plt.figure(3)
        #plt.subplot(313)        
        plt.plot(d[:,0], f[:,1], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        plt.title('{:s}'.format(titlestring)+'\nProbability of outer tube surface')
       
        
    plt.figure(1)
    plt.ylim(0.000, 1.000)
    plt.ylabel('Prob(d<7.1Å)')
    plt.xlabel('Monomer index')
    plt.legend()
    
    plt.figure(2)             
    plt.ylim(0.000, 1.000)
    plt.ylabel('Prob(d<7.1Å)')
    plt.xlabel('Monomer index')
    plt.legend()
    
    plt.figure(3)
    plt.ylim(0.000, 1.000)
    plt.ylabel('Prob(d<7.1Å)')
    plt.xlabel('Monomer index')
    plt.legend()
    #    plt.title('{:s}'.format(titlestring)+'\nProbability of inner/outer tube surface')
    plt.show()
    
    
    
    

