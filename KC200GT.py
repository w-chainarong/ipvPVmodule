import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
def initalizeIPV():
        k, q, T = 1.38065e-23, 1.602e-19, 25 + 273
        Vt = k * T / q
        Iph, Io = 8.193, 0.3e-09
        a, Rs, Rsh = 1.0, 0.271, 171.2
        norVoc, Isc, Ns = 32.9, 8.21, 54
        PVmoduleName = 'Sim.KYOCERA PV module KC200GT'
        step = 0.1
        return norVoc, step, Isc, Vt, a, Ns, Rsh, Rs, Io, Iph, PVmoduleName
        
def AppendVI(I, V, P):
        In.append(I)
        Vn.append(V)
        Pn.append(P)
def diode_equationVoc(V):
    return Iph - Io * (np.exp((V) / (Ns * a * Vt)) - 1) - (V) / Rsh
def diode_equation(I, V):
        return Iph - Io * (np.exp((V + I* Rs) / (Ns * a * Vt)) - 1) - (V + I* Rs) / Rsh - I
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
_3Tuple = [(V, I, P) for V, I, P in zip(Vn,In, Pn)]
MPPoint = max(_3Tuple, key=lambda item: item[2])
Str1 = "Voc = %.2f, Isc = %.2f" % (Vn[len(Vn)-1], In[0])
Str2 = "Vmpp = %.2f, Impp = %.2f, Pmax = %.2f" % (MPPoint[0], MPPoint[1], MPPoint[2])
plotIPVcurves(In, Pn, Vn, Str1, Str2, PVname)

