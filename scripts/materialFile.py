class material:
    def __init__(self, name, density, dynViscosity, kinViscosity, specificHeatCapacity, turbPr, thermalConductivity, pressure, temperature, thermalExpansionCoeff, lamPr):
        self.name = name                                    #
        self.density = density                              # [Kg/m3]
        self.dynViscosity = dynViscosity                    # [Pa*s]
        self.kinViscosity = kinViscosity                    # [m2/s]
        self.specificHeatCapacity = specificHeatCapacity    # [J/Kg*K]
        self.turbPr = turbPr                                #
        self.thermalConductivity = thermalConductivity      # [W/m*K]
        self.pressure = pressure                            # [Pa]
        self.temperature = temperature                      # [K]
        self.thermalExpansionCoeff = thermalExpansionCoeff  # [1/K]
        self.lamPr = lamPr                                  #

    def displayVars(self):
        print(vars(self))



if __name__ == '__main__':
    H2O = material(
        name='H2O',
        density=998.2,
        dynViscosity=0.001002,
        kinViscosity=0.0000010038,
        specificHeatCapacity=4187,
        turbPr=0.9,
        thermalConductivity=0.5985,
        pressure=101325,
        temperature=293,
        thermalExpansionCoeff=0.00207,
        lamPr=0.9
    )

    H2O.displayVars()