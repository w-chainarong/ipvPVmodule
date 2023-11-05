import matplotlib.pyplot as plt
class ipvPlots(object):
    def __init__(self, moduleName):
        self.PVmoduleName = moduleName
        self.Vn, self.In, self.Vn1, self.In1, self.Vn2, self.In2,\
        self.Pn = [], [], [], [], [], [], []

    def plotIPVcurves(self,legend1, legend2, PVmoduleName):
        fig, IVcurve = plt.subplots()
        IVcurve.plot(self.Vn, self.In, 'b', label=legend1)
        IVcurve.set_xlabel('Voltage [V]')
        IVcurve.set_ylabel('Current [A]', color='b')
        PVcurve = IVcurve.twinx()
        PVcurve.plot(self.Vn, self.Pn, 'r', label=legend2)
        PVcurve.set_ylabel('Powe [W]', color='r')
        IVcurve.legend(loc='center left')
        PVcurve.legend(loc='lower left')
        plt.title(PVmoduleName)
        plt.grid()
        plt.show()

    def plotIVcurves(self,legend1, legend2, legend3,  PVmoduleName, title1):
        fig, IVcurve  = plt.subplots(figsize=(10, 6))
        fig.suptitle(title1)
        IVcurve.plot(self.Vn, self.In, 'r', label=legend1)
        IVcurve.plot(self.Vn1, self.In1,'g', label=legend2)
        IVcurve.plot(self.Vn2, self.In2,'b', label=legend3)
        IVcurve.set_xlabel('Voltage [V]')
        IVcurve.set_ylabel('Current [A]', color='b')
        IVcurve.legend()
        plt.title(PVmoduleName)
        IVcurve.legend()
        plt.grid()
        plt.show()

    def pviPlot(self, Vn, In,  Pn): 
        self.Vn, self.In, self.Pn = Vn, In, Pn
        _3Tuple = [(V, I, P) for V, I, P in zip(Vn, In, Pn)]
        MPPoint = max(_3Tuple, key=lambda item: item[2])
        Str1 = "Voc = %.2f, Isc = %.2f" % (self.Vn[len(self.Vn)-1], self.In[0])
        Str2 = "Vmpp = %.2f, Impp = %.2f, Pmax = %.2f" % (MPPoint[0], MPPoint[1], MPPoint[2])
        self.plotIPVcurves(Str1, Str2, self.PVmoduleName)
        return


    def ivTempDependencePlot(self, IV, IV1, IV2, T, T1, T2):
        self.Vn, self.In, = [pair[0] for pair in IV], [pair[1] for pair in IV]
        self.Vn1, self.In1, = [pair[0] for pair in IV1], [pair[1] for pair in IV1]
        self.Vn2, self.In2, = [pair[0] for pair in IV2], [pair[1] for pair in IV2]
        Str = "Voc = %.2f, Isc = %.2f, T = %d \u00b0C"  % (self.Vn[len(self.Vn)-1], self.In[0], T)
        Str1 = "Voc = %.2f, Isc = %.2f, T = %d \u00b0C" % (self.Vn1[len(self.Vn1)-1], self.In1[0], T1)
        Str2 = "Voc = %.2f, Isc = %.2f, T = %d \u00b0C" % (self.Vn2[len(self.Vn2)-1], self.In2[0], T2)
        figTitle = "Temperature dependence of I-V curves at 1000 W/m\u00b2"
        self.plotIVcurves(Str, Str1, Str2, self.PVmoduleName, figTitle) 

    def ivIrraDependencePlot(self, IV, IV1, IV2, G, G1, G2):
        self.Vn, self.In, = [pair[0] for pair in IV], [pair[1] for pair in IV]
        self.Vn1, self.In1, = [pair[0] for pair in IV1], [pair[1] for pair in IV1]
        self.Vn2, self.In2, = [pair[0] for pair in IV2], [pair[1] for pair in IV2]
        Str = "Voc = %.2f, Isc = %.2f, G = %d W/m\u00b2"  % (self.Vn[len(self.Vn)-1], self.In[0], G)
        Str1 = "Voc = %.2f, Isc = %.2f, G = %d W/m\u00b2" % (self.Vn1[len(self.Vn1)-1], self.In1[0], G1)
        Str2 = "Voc = %.2f, Isc = %.2f, G= %d W/m\u00b2" % (self.Vn2[len(self.Vn2)-1], self.In2[0], G2)
        figTitle = "Irradiances dependence of I-V curves at 25\u00b0C"
        self.plotIVcurves(Str, Str1, Str2, self.PVmoduleName, figTitle) 


