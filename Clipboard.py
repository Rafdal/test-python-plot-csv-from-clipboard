# % Graficos perdida de paquetes, RSSI, SNR, pFE

import pyperclip, csv, pandas
import matplotlib.pyplot as plt
from io import StringIO

cmap = plt.get_cmap('jet_r')

papelera = pyperclip.paste()
f = StringIO(papelera)

data = pandas.read_csv(f, delimiter=",")

fig, ax = plt.subplots(ncols=3, nrows=2)

x_axis = 'X_AXIS'

def ParamPlot(axe, name):
    lim = []
    mx = max(data[str(name)+'_max'])
    mn = min(data[str(name)+'_min'])


    if mn < 0:
        lim.append( mx )
        lim.append( mn )

        data.plot(ylim=lim, kind='bar', x = x_axis, y=str(name)+'_min', color=cmap(0.0), ax = axe)
        data.plot(ylim=lim, kind='bar', x = x_axis, y=str(name)+'_avg', color=cmap(0.13),ax = axe)
        data.plot(ylim=lim, kind='bar', x = x_axis, y=str(name)+'_max', color=cmap(0.26), ax = axe)
        pass
    else:
        lim.append( mn )
        lim.append( mx )

        data.plot(ylim=lim, kind='bar', x = x_axis, y=str(name)+'_max', color=cmap(0.0), ax = axe)
        data.plot(ylim=lim, kind='bar', x = x_axis, y=str(name)+'_avg', color=cmap(0.13),ax = axe)
        data.plot(ylim=lim, kind='bar', x = x_axis, y=str(name)+'_min', color=cmap(0.26), ax = axe)
        pass

ParamPlot(ax[0,0], 'rssi')
ParamPlot(ax[1,0], 'snr')
ParamPlot(ax[1,1], 'pfe')

data.plot(grid='true',kind='line',x = x_axis, y='t_tot', ax = ax[0,1])
data.plot(grid='true',kind='line', x = x_axis, y='t_avg', ax = ax[0,2])
data.plot(kind='bar', x = x_axis, y='perdida', color='xkcd:periwinkle',ax = ax[1,2])

# mng = plt.get_current_fig_manager()
# mng.frame.Maximize(True)


mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()

