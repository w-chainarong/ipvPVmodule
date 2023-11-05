from ipvCurCalModule import ipvCurCul
from ipvCurves import ipvPlots

PV = ipvCurCul(Isc=8.21, Voc=32.9, Impp=7.61, Vmpp=26.3, Ns = 54, Kv =-1.23e-1, Ki = 3.18e-3)
Rs0, Rsh0, a, Itr = 0.1, 200, 1.5, 10
PV.parameter_extractionCall(Rs0, Rsh0, a)
print('Series resistance Rs=', PV.Rs)
print('Shunt resistance Rsh=', PV.Rsh)
print('Diode quality_factor a=', PV.a)
print('Residuals=', PV.Residuals)

PV.generateIPVcurves()

operating_temperature = 25 + 273
actual_irradiance = 1000
PV.SMD.calculate(operating_temperature, actual_irradiance)
print('Saturation current Io=', PV.SMD.Io)
V, I, P = PV.SMD.voltages, PV.SMD.currents, PV.SMD.powers
PV1curves = ipvPlots('Sim.Kyocera KC200GT')
PV1curves.pviPlot(V, I, P)





 
