import numpy as np 
import matplotlib.pyplot as plt

### Propulsion Core Model ###

def compute_thrust(Pc,eps,Pa,mdot,gamma=1.22,R=287,Tc=3000):
    ### Simplified rocket thrust model (first-order approximation) ###
    """
    Pc: Combustion chamber pressure; Unit - Pa
    eps: Expansion ratio (exhaust area/throat area; how much exhaust expands before leaving the nozzle); Unitless
    Pa: Ambient pressure aka nozzle exit pressure (altitute/operating condition: Sea level = 101,325Pa; Vacuum = 0 Pa); Units - Pa
    mdot: Mass flow rate (how much propellant is flowing out per second); Units - kg/s
    gamma: Specific heat ratio (constant pressure/constant volume; therodynamic behavior of exhaust gases); Unitless
    R: Gas constant (universal gas constant / exhaust gas molecular weight); Units - J/(kg*K)
    Tc: Chamber temperature (temperature of combust gases inside chamber); Units - K
    """

    ## placeholder structure (will be refined step by step)

    # Calculate exhaust velcoity
    Ve = np.sqrt((((2 * gamma) / (gamma - 1)) * (R * Tc) * (1-(Pa/Pc)**((gamma - 1)/ gamma))))

    momentum_thrust = mdot * Ve
    pressure_thrust = (Pc - Pa) * (eps * 1e-4) #simplified scaling placeholder

    F = momentum_thrust + pressure_thrust

    return F

def compute_isp(F,mdot,g0=9.81):
    ### Specific Impluse Calculation ###
    return F / (mdot * g0)

def compute_delta_v(Isp, m0, mf, g0=9.81):
    ### Delta-V Calculation using Tsiolkovsky rocket equation ###
    """
    Isp: Specific impulse of the engine; Units - s
    m0: Initial mass (including propellant); Units - kg
    mf: Final mass (after propellant is expended); Units - kg
    g0: Standard gravity; Units - m/s^2
    """
    return Isp * g0 * np.log(m0 / mf)

if __name__ == "__main__":
    ### Input Variables
    Pc = 10e6
    mdot = 20
    eps = 20
    Pa = 101325

    ### Calculate values then output
    for gamma in np.arange(1.0, 1.45, 0.05):
        F = compute_thrust(Pc,eps,Pa,mdot,gamma=gamma)
        Isp = compute_isp(F,mdot) 
        
        print("Thrust: ", f"{F:,.2f}")
        print("Isp: ", f"{Isp:,.2f}")
        print("Gamma: ", f"{gamma:,.2f}")