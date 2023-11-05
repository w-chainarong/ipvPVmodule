from single_diode_model import SingleDiodeModel
from parameter_extraction import ParameterExtraction
#Two modules, single_diode_model and parameter_extraction
# are downloaded from "https://github.com/tadatoshi/photovoltaic_modeling_python."
from math import exp, sqrt
class ipvCurCul(object):    
    def __init__(self, Isc, Voc, Impp, Vmpp, Ns, Kv, Ki):
        self.K, self.q = 1.38065e-23, 1.602e-19 #Joule/C, C(Coulomb)
        self.norG, self.norT = 1000, 25 + 273 #W/m^2, K(Kelvin)
        self.norIsc, self.norVoc, self.norImpp,  self.norVmpp = Isc, Voc, Impp, Vmpp
        self.Ns, self.Kv, self.Ki = Ns, Kv, Ki
        self.Rs, self.Rsh, self.a = 0.0, 0.0, 0.0
        self.SMD = None
    def parameter_extractionCall(self,Rs0, Rsh0, a0, **optionalArguments):    
        Rs_estimate, Rsh_estimate, a_estimate = Rs0, Rsh0, a0
        if 'iteration_arg' in optionalArguments :
            iteration =  optionalArguments['iteration_arg']
            parameter_extraction = ParameterExtraction(self.norIsc, self.Voc, 
                self.Impp, self.Vmpp,self.Ns, number_of_iterations = iteration)
        else:
            parameter_extraction = ParameterExtraction(self.norIsc, 
                self.norVoc, self.norImpp, self.norVmpp,self.Ns)        
        parameter_estimates = [Rs_estimate, Rsh_estimate, a_estimate] 
        parameter_extraction.calculate(parameter_estimates)
        self.Rs = parameter_extraction.series_resistance
        self.Rsh= parameter_extraction.shunt_resistance
        self.Vt = parameter_extraction.thermal_voltage
        self.a =  parameter_extraction.diode_quality_factor
        Solution = [self.Rs, self.Rsh, self.Vt]
        self.Residuals = self.minimize_of_three_equations(Solution)
    def generateIPVcurves(self):
        dgtsOfVltgDec, Params = 1, [self.Rs, self.Rsh, self.a]
        if sqrt(sum([x**2 for x in Params])) != 0.0:
            self.SMD = SingleDiodeModel(self.norIsc, self.norVoc, self.Ns, dgtsOfVltgDec,
                    temperature_current_coefficient = self.Ki, series_resistance =self.Rs, 
                    shunt_resistance = self.Rsh, diode_quality_factor = self.a) 
    def minimize_of_three_equations(self, ComptdParam):
        Rs, Rsh, Vt = ComptdParam[0], ComptdParam[1], ComptdParam[2]
        Isc, Vmpp, Impp, ns, Voc =self.norIsc,self.norVmpp, self.norImpp, self.Ns, self.norVoc 
        X, Y = Isc*Rsh-Voc+Isc*Rs, exp((Vmpp+Impp*Rs-Voc)/(ns*Vt))
        Z = exp((Isc*Rs-Voc)/(ns*Vt))
        return [Isc -(Vmpp+Impp*Rs-Isc*Rs)/Rsh-(Isc-(Voc-Isc*Rs)/Rsh)*Y -Impp, 
                Impp + Vmpp*(-X*Y/(ns*Vt*Rsh)-1/Rsh)/(1 + X*Y/(ns*Vt*Rsh) + Rs/Rsh),
                (-X*Z/(ns*Vt*Rsh) -1/Rsh)/(1 + X*Z/(ns*Vt*Rsh) + Rs/Rsh) + 1/Rsh]
