import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
def initalizeIPV():
        k, q, T = 1.38065e-23, 1.602e-19, 25 + 273
        Vt = k * T / q
        Iph, Io = 3.321, 1.177e-9
        a, Rs, Rsh = 1.056, 0.026, 1102
        norVoc, Isc, Ns = 22.1, 2.9, 36
        PVmoduleName = 'Sim.AMERESCO PV module 50J'
        step = 0.1
        return norVoc, step, Isc, Vt, a, Ns, Rsh, Rs, Io, Iph, PVmoduleName
        
def AppendVI(I, V, P):
        In.append(I)
        Vn.append(V)
        Pn.append(P)
def diode_equation(I, V):
        return Iph - Io * (np.exp((V + I* Rs) / (Ns * a * Vt)) - 1) - (V + I* Rs) / Rsh - I
def diode_equationVoc(V):
    return Iph - Io * (np.exp((V) / (Ns * a * Vt)) - 1) - (V) / Rsh
def plotIPVcurves(I, P, V, legend1, legend2, PVmoduleName):
        fig, IVcurve = plt.subplots()
        IVcurve.plot(Vn, In, 'b', label=legend1)
        IVcurve.set_xlabel('Voltage [V]')
        IVcurve.set_ylabel('Current [A]', color='b')
        PVcurve = IVcurve.twinx()
        PVcurve.plot(Vn, Pn, 'r', label=legend2)
        PVcurve.set_ylabel('Powe [W]', color='r')
        IVcurve.legend(loc='center left')
        PVcurve.legend(loc='lower left')
        plt.title(PVmoduleName)
        plt.grid()
        plt.show()
        
norVoc, step, I, Vt, a, Ns, Rsh, Rs, Io, Iph, PVname = initalizeIPV()
Vn, In, Pn = [], [], []
end = newton(diode_equationVoc, norVoc)
for Value in np.arange(0,  end, step):
        V = Value
        I_update = newton(diode_equation, I, args=(V,))
        AppendVI(I_update, V, I_update*V )
        I = I_update
AppendVI(0, end, 0 )
ordered_pairs = [(V, I, P) for V, I, P in zip(Vn,In, Pn)]
MPPoint = max(ordered_pairs, key=lambda item: item[2])
Str1 = "Voc = %.2f, Isc = %.2f" % (Vn[len(Vn)-1], In[0])
Str2 = "Vmpp = %.2f, Impp = %.2f, Pmax = %.2f" % (MPPoint[0], MPPoint[1], MPPoint[2])
plotIPVcurves(In, Pn, Vn, Str1, Str2, PVname)

