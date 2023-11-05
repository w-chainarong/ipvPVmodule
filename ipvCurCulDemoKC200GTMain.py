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
V, I, P = PV.SMD.voltages, PV.SMD.currents, PV.SMD.powers
print('Saturation current Io=', PV.SMD.Io)
print('photo current Iph=', PV.SMD.Iph)
IV1 = [(v, i) for v, i in zip(PV.SMD.voltages, PV.SMD.currents)]

operating_temperature = 50 + 273
PV.SMD.calculate(operating_temperature, actual_irradiance)
IV2 = [(v, i) for v, i in zip(PV.SMD.voltages, PV.SMD.currents)]

operating_temperature = 75 + 273
PV.SMD.calculate(operating_temperature, actual_irradiance)
IV3 = [(v, i) for v, i in zip(PV.SMD.voltages, PV.SMD.currents)]

operating_temperature = 25 + 273
actual_irradiance = 800
PV.SMD.calculate(operating_temperature, actual_irradiance)
IV4 = [(v, i) for v, i in zip(PV.SMD.voltages, PV.SMD.currents)]

actual_irradiance = 600
PV.SMD.calculate(operating_temperature, actual_irradiance)
IV5 = [(v, i) for v, i in zip(PV.SMD.voltages, PV.SMD.currents)]


PV1curves = ipvPlots('Sim.Kyocera KC200GT')
PV1curves.pviPlot(V, I, P)
PV1curves.ivTempDependencePlot(IV1, IV2, IV3, 25, 50, 75)
PV1curves.ivIrraDependencePlot(IV1, IV4, IV5, 1000, 800, 600)




 
