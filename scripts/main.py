import numpy as np
import matplotlib.pyplot as plt
from materialFile import material
from salts import Salt


def chloride_density_interpolation(x: float, tempK: float) -> float:
    '''Interpolation based on Table 572, page 1135 of https://aip.scitation.org/doi/pdf/10.1063/1.555527
    Molten salts: Volume 4, part 2, chlorides and mixtures—electrical conductance, density,
    viscosity, and surface tension data
    return [g/cc]
    '''
    x = x * 100.0  # fraction -> %
    if x < 1.59 or x > 53.81:
        raise ValueError("UCl3 fraction has to be 1.6 to 53.8% :", x)
    # rho = a + b/1e3  T
    xmol = [1.6, 8.7, 24.7, 53.8]  # mol% of UCl3 in NaCl+UCl3
    a = [2.2075, 2.7796, 4.2900, 6.6390]
    b = [-0.5655, -0.6828, -1.5903, -3.0582]
    ia = np.interp(x, xmol, a)
    ib = np.interp(x, xmol, b)
    # print(ia,ib)
    return ia + ib * 1e-3 * tempK

def main():
    '''
% Fuel salt: 58%NaCl + 42%UCl3, U enrichment 0.1083
mat fuelsalt  -3.46981237 rgb 240 30 30 burn 1 tmp  900.000
 11023.09c  -0.073590076230    %  Na-23
 17035.09c  -0.000003551042    %  Cl-35
 17037.09c  -0.375380269116    %  Cl-37
 92234.09c  -0.000522897128    %  U-234
 92235.09c  -0.059004268911    %  U-235
 92236.09c  -0.000272576282    %  U-236
 92238.09c  -0.491226361291    %  U-238

% Iron reflector [density 7.874/((1+680*12e-6)^3)]
mat refl   -7.68435 tmp 900.0 rgb 128 128 178
 26054.09c  -0.058450   %  Fe
 26056.09c  -0.917540   %  Fe
 26057.09c  -0.021190   %  Fe
 26058.09c  -0.002820   %  Fe
    '''

    saltObj = Salt(f='66.67%NaCl + 33.33%UCl3', e=0.01975)

    fuelSalt = material(
        name='66.67%NaCl + 33.33%UCl3, U enrichment 19.75%',
        density=saltObj.densityC(626.85)*1e3,  # [Kg/m3]
        temperature=900,                # [K](626.85 C)
        dynViscosity=None,              # [Pa*s]
        kinViscosity=None,              # [m2/s]
        specificHeatCapacity=None,      # [J/Kg*K]
        turbPr=0.9,                     # maybe dont change? OIL
        thermalConductivity=None,       # [W/m*K]
        pressure=0,                     # [Pa] maybe dont change? OIL
        thermalExpansionCoeff=None,     # [1/K]
        lamPr=0                         # maybe dont change? OIL
    )

    print(fuelSalt.density)

    oil = material(
        name='oil',
        density=500,  # [Kg/m3]
        temperature=300,            # [K](626.85 C)
        dynViscosity=0.05,          # [Pa*s]
        kinViscosity=0.0001,        # [m2/s]
        specificHeatCapacity=1006,  # [J/Kg*K]
        turbPr=0.9,                 #
        thermalConductivity=0.007,  # [W/m*K]
        pressure=0,                 # [Pa]
        thermalExpansionCoeff=0,    # [1/K]
        lamPr=0                     #
    )

    pass


if __name__ == '__main__':
    main()
