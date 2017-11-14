import random
import tabuleiro
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

volume = []
subpops = ['Grupoa','Grupoab','Grupoac','Grupoad','Grupoae','Grupoaf','Grupoag']
ghs = ['3','4','5','6','7']
cores = []

for subpop in subpops:
	volume_atual = []
	for gh in range(len(ghs)):
		volume_atual.append(random.randint(0,100)+0.89)
	volume.append(volume_atual)


fig = plt.figure(figsize=(22, 12))
gs = gridspec.GridSpec(20, 40)
ax = [
      plt.subplot(gs[0:2, 0:40]),
      plt.subplot(gs[2:3, 0:20]),
      plt.subplot(gs[2:3, 20:40]),
      plt.subplot(gs[11:12, 0:20]),
      plt.subplot(gs[11:12, 20:40]),

      plt.subplot(gs[3:11, 0:20]),
      plt.subplot(gs[3:11, 20:40]),
      plt.subplot(gs[12:20, 0:20]),
      plt.subplot(gs[12:20, 20:40])]

ax[0].text(0.5, 0.5, s='PARCERIA', 
		horizontalalignment='center', 
		verticalalignment='center', 
		fontsize=48, 
		bbox={'facecolor':'green', 'alpha':0, 'pad':20})
for i in range(1,5):
	ax[i].text(0.5, 0.5, s='Volume', 
		horizontalalignment='center', 
		verticalalignment='center', 
		fontsize=24, 
		bbox={'facecolor':'gray', 'alpha':0.2, 'pad':20})
for i in range(5):
	ax[i].axis('off')


tabuleiro.plota_tabuleiro(ax[5], volume, ghs, subpops, 'Volume')
tabuleiro.plota_tabuleiro(ax[6], volume, ghs, subpops, 'BR')
tabuleiro.plota_tabuleiro(ax[7], volume, ghs, subpops, 'Volume')
tabuleiro.plota_tabuleiro(ax[8], volume, ghs, subpops, 'BR')

plt.tight_layout()
plt.savefig('teste.png', dpi=300)
