import matplotlib.pyplot as plt
import numpy as np


def plota_tabuleiro(ax, dados, gruposx, gruposy, titulo):
	ax.matshow(dados, cmap=plt.cm.bwr, aspect=0.4, alpha=0.5)
	for i in range(0,len(dados)):
		for j in range(0, len(dados[i])):
			ax.text(j, i, dados[i][j], va='center', ha='center', fontsize=24)
	ax.set_xticklabels(['']+gruposx, fontsize=22)
	ax.set_yticklabels(['']+gruposy, fontsize=22)
	#ax.set_title(titulo, fontsize=24, bbox={'facecolor':'gray', 'alpha':0.2, 'pad':20})
