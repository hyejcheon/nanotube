import matplotlib.pyplot as plt    # https://matplotlib.org/
from pathlib import Path         # https://docs.python.org/3.5/library/pathlib.html#module-pathlib
import molsim_utilities as mu
import pylab as py

##fixing numbers, opposite charge : neg/pos

strtype = ['m40ncenxyz', 'm40pcenxyz'] 
chargeratio = ['0', '0']

pathstring  = []
ph = []
axs = []

linecolor = [['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown'],
              ['lightsteelblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']]
linecolor1 = ['wheat', 'gold', 'orange', 'darkorange', 'chocolate', 'sienna', 'saddlebrown']
linecolor2 = ['lightsteelblue', 'lightblue', 'lightskyblue', 'royalblue', 'blue', 'mediumblue', 'darkblue']

#fig, axs = plt.subplots(2, 1, sharex=True)
#fig.subplots_adjust(hspace=0)



for i in range(len(strtype)):
    pathstring.append('../alsi/polymer/quenchedpoly/{:s}'.format(str(chargeratio[i])) + '/{:s}/'.format(str(strtype[i])))
plotlines=[]
fig = []
for j in range(len(pathstring)):
    fig.append([])
    for p in sorted(Path(str(pathstring[j])).glob('zero/ph*/cylinder_shell.list')):
        print(p)  
        e = mu.getDistribution(p, 'opt_d gr:3') 
        f = mu.getDistribution(p, 'zden gr:3') 
        if '40n' in p.parts[-4]:
            labelstring = 'neg, pH = {:d}'.format(int(p.parts[-2][2]))
        else:
            labelstring = 'pos, pH = {:d}'.format(int(p.parts[-2][2]))
        
        print(p.parts)
        print(p.parts[-2])
        print(p.parts[-2][2])
        ph.append(p.parts[-2][2])  
           
        e_errdown = e[:,1] - 0.5*e[:,2]
        e_errup = e[:,1] + 0.5*e[:,2]       
        f_errdown = f[:,1] - 0.5*f[:,2]
        f_errup = f[:,1] + 0.5*f[:,2]            
        
        plt.figure(1)  # in out 
        if '40n' in p.parts[-4]: 
            fig[j] = plt.plot(e[:,0], e[:,1], label=labelstring, color = linecolor[j][int(p.parts[-2][2])-2] ,linestyle='-')      
        else: 
            fig[j] = plt.plot(e[:,0], e[:,1], label=labelstring, color = linecolor[j][int(p.parts[-2][2])-2] ,linestyle=':')      
        fig[j] = plt.fill_between(e[:,0], e_errdown, e_errup, color = linecolor[j][int(p.parts[-2][2])-2] , alpha=0.2)
        fig[j] = plt.legend(fontsize=8)  
        fig[j]  = plt.ylabel(r'$P(r_{z=0})$', size=10)
        fig[j] = plt.xlabel(r'$r_{z=0} \ [\AA]$', size=10)
        fig[j]  = plt.xlim(0, 60)
        #fig1 = plt.legend(fontsize=8)
        area = 0
        for m in range(len(e)-1):
            area += e[m][1]*(e[m+1][0]-e[m][0])
        print('integral result =', area)
       # axs[0].legend(fontsize=8)
        #axs[0].grid(True)
        
        #if j == 0:
        #    axs[0].legend(fontsize=8)
        plt.figure(2)
        if '40n' in p.parts[-4]:
            fig[j] = plt.plot(f[:,0], f[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle='-'  )      
        else:
            fig[j] = plt.plot(f[:,0], f[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) ,linestyle=':'  )                  
        fig[j] = plt.fill_between(f[:,0], f_errdown, f_errup, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , alpha=0.2)
        #fig[j] = plt.ylim(0.00, 0.5)    
        fig[j] = plt.ylabel(r'$P(r_z)$', size=10)
        fig[j] = plt.xlabel(r'$r_z\ [\AA]$', size=10)
        fig[j] = plt.xlim(-350, 350)
        fig[j] = plt.legend(fontsize=8)
        area2 = 0
        for n in range(len(f)-1):
            area2 += f[n][1]*abs(f[n+1][0]-f[n][0])
        print('integral result, prob-z =', area2)
        #axs[1].grid(True)
        '''
        axs[2].plot(f[:,0], f[:,1], label=labelstring, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , linestyle=':')      
        
        axs[2].fill_between(f[:,0], f_errdown, f_errup, color = '{:s}'.format(linecolor[j][int(p.parts[-2][2])-2]) , alpha=0.2)
        axs[2].set_ylim(0.0, 0.5)        
        axs[2].set_ylabel(r'$P(d<7.1\AA)$', size=8)
        axs[2].set_xlim(0, 40.5)
        axs[2].set_xlabel(r'$Monomer\ index$')
        #axs[2].grid(True)
        #if j == 1:   
        #axs[2].legend(fontsize=8)
        '''

#plt.hold(True)
#plotlines.append([axs[0], axs[1], axs[2]])
#legend1 = plt.legend(plotlines[0], ['in+out', 'in', 'out'], loc = 'center left')
#pyplot.legend([axs[0]])
#plt.plot(f[:,0], d[:,0], e[:,0], f[:,0], label=['in+out', 'in', 'out'])
plt.figure(1)
plt.savefig("fig/coordxy_neg_pos_40_r1.pdf")    
plt.figure(2)
plt.savefig("fig/coordz_neg_pos_40_r1.pdf")  
'''
    plt.figure(2)      
    axs[0].plot(d[:,0], d[:,1], label=labelstring, color = '{:s}'.format(linecolor1[j]))      
    axs[0].fill_between(d[:,0], d_errdown, d_errup, color = '{:s}'.format(linecolor1[j]) , alpha=0.2)
    axs[0].set_ylim(0.00, 0.5)        
    axs[0].set_xlim(0, 40)
    axs[0].legend(fontsize=8)
    
    axs[1].plot(e[:,0], e[:,1],  color = '{:s}'.format(linecolor1[j]))      
    axs[1].fill_between(e[:,0], e_errdown, e_errup, color = '{:s}'.format(linecolor1[j]) , alpha=0.2)
    axs[1].set_ylim(0.00, 0.5)        
    axs[1].set_xlim(0, 40)
   # axs[1].legend(off)
    
    axs[2].plot(f[:,0], f[:,1],  color = '{:s}'.format(linecolor1[j]))      
    axs[2].fill_between(f[:,0], f_errdown, f_errup, color = '{:s}'.format(linecolor1[j]) , alpha=0.2)
    axs[2].set_ylim(0.0, 0.5)        
    axs[2].set_xlim(0, 40)
    fig.show()
'''
'''
        plt.figure(2)
        #plt.subplot(312)        
        plt.errorbar(e[:,0], e[:,1], e[:,2], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        #plt.title('{:s}'.format(titlestring)+'\nProbability of inner tube surface')
        plt.ylim(0.00, 1.00)
        plt.xlim(0, 40)
        
        plt.figure(3)
        #plt.subplot(312)        
        plt.errorbar(f[:,0], f[:,1], f[:,2], label = labelstring, color = '{:s}'.format(linecolor[int(p.parts[-2][2])-2]))     
        #plt.title('{:s}'.format(titlestring)+'\nProbability of outer tube surface')
        plt.ylim(0.00, 1.00) 
        plt.xlim(0, 40)
        
    plt.figure(1)
    plt.ylim(0.00, 1.00)
    plt.xlim(0, 40)
    plt.ylabel(r'$Prob(d<7.1\AA)$')
    plt.xlabel(r'$Monomer\ index$')
    plt.legend()
    #py.savefig('{:s}'.format(titlestring) + '-prob' + '-io.pdf')        
     
    plt.figure(2)
    plt.ylim(0.00, 1.00)
    plt.xlim(0, 40)
    plt.ylabel(r'$Prob(d<7.1\AA)$')
    plt.xlabel(r'$Monomer\ index$')
    plt.legend()
    #py.savefig('{:s}'.format(titlestring) + '-prob' + '-i.pdf')
    
    plt.figure(3)
    plt.ylim(0.00, 1.00)
    plt.xlim(0, 40)
    plt.ylabel(r'$Prob(d<7.1\AA)$')
    plt.xlabel(r'$Monomer\ index$')
    plt.legend()
    #py.savefig('{:s}'.format(titlestring) + '-prob' + '-o.pdf')    

    plt.show()
'''
'''
    #    plt.title('{:s}'.format(titlestring)+'\nProbability of inner/outer tube surface')
plt.figure(4) 
#y = [0.25546, 0.26873, 0.27580, 0.25980, 0.25955, 0.25982, 0.27091, 0.26251, 0.26117, 0.25232, 0.24820, 0.25587, 
#         0.26452, 0.26695, 0.25728, 0.24996, 0.24036, 0.25415, 0.26207, 0.26480, 0.25217, 0.25935]
#z = [0.17228, 0.15982, 0.15508, 0.15216, 0.15751, 0.15706, 0.16135, 0.15694, 0.15940, 0.16288, 0.15837, 0.15563, 
#          0.15897, 0.15760, 0.16046, 0.15971, 0.15874, 0.15525, 0.15716, 0.15945, 0.15767, 0.15806]

y = [0.26873, 0.27580, 0.25980, 0.25955, 0.25982, 0.27091, 0.26251, 0.26117, 0.25232, 0.24820, 0.25587, 
         0.26452, 0.26695, 0.25728, 0.24996, 0.24036, 0.25415, 0.26207, 0.26480, 0.25217]
yy = 0.25935 * np.ones(20)
z = [0.15982, 0.15508, 0.15216, 0.15751, 0.15706, 0.16135, 0.15694, 0.15940, 0.16288, 0.15837, 0.15563, 
          0.15897, 0.15760, 0.16046, 0.15971, 0.15874, 0.15525, 0.15716, 0.15945, 0.15767]
zz = 0.15806 * np.ones(20)

plt.plot(np.linspace(1, 20, 20), y, 'b.:', label = 'from outside') 
plt.plot(np.linspace(1, 20, 20), yy , 'b_-', label = 'from outside(final)')
plt.plot(np.linspace(1, 20, 20), z, 'g.:', label = 'from inside(center)')
plt.plot(np.linspace(1, 20, 20), zz, 'g_-', label = 'from inside(final)')
  
plt.ylabel(r'$U_{total}$')
plt.xlabel(r'$Macrostep \ number$')
plt.legend()
py.savefig('m40n-m40ncen-u.pdf')   
plt.show()  
'''

