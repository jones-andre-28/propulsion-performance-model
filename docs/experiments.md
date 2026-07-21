# Experiment: Effect of Mass Flow Rate | 7/7/26

## Current Assumptions
Specific Heat Ratio = 1.22  
Gas Constant = 287  
Chamber Temperature = 3000

## Input changed:
mdot increased from 10 to 20

## Prediction before running:
Thrust should double  
Isp should decrease 

## Observed:
Thrust increased by 78.3%  
Isp decreased by 10.8%

## Rough Explanation:
Thrust increased as it is dependent on the mass flow rate proportionally however it is not a 100% increase as it is equivalent to the momentum + pressure so the value provided by a constant pressure will dilute the increase. This means pressure should increase to reach 100% increase.  

Isp decreasd since the denominator increases faster than the numerator and as there was not a totally efficient increase in Thrust, the Isp is decreased even more

### Edit: 7/20/26
Numbers are not doubled as the Ve equation (which is in the momentum_thrust equation of m-dot * Ve) contains a square root, meaning 2x inputs only produces 1.4x output

# Experiment: Limits of ISP | 7/20/26
## Chamber pressure
## Code
for Pc in np.arange(10.0e6, 20.5e6, 0.5e6):
        F = compute_thrust(Pc,eps,Pa,mdot)
        Isp = compute_isp(F,mdot) 
        
        print("Pc: ", f"{Pc:,.2f}")
        print("Thrust: ", f"{F:,.2f}")
        print("Isp: ", f"{Isp:,.2f}") 

## Current Assumptions
gamma = 1.22  
R = 287  J/(kg*K)
Tc = 3000 K  
g0 = 9.81 m/s^2
eps = 20  
Pa = 101325 Pa
mdot = 20 kg*m / s 

## Input changed
Chamber pressure (Pc): 10.0e6 < x < 20.0e6  
inc = 0.5e6  

## Results
| Chamber Pressure (MPa) | Thrust (N) | Specific Impulse (s) |
|------------------------|-----------:|---------------------:|
| 10.0 | 66,175.20 | 337.28 |
| 10.5 | 67,332.53 | 343.18 |
| 11.0 | 68,480.77 | 349.04 |
| 11.5 | 69,620.83 | 354.85 |
| 12.0 | 70,753.49 | 360.62 | 
| 12.5 | 71,879.43 | 366.36 |
| 13.0 | 72,999.26 | 372.07 |
| 13.5 | 74,113.47 | 377.74 |
| 14.0 | 75,222.55 | 383.40 |
| 14.5 | 76,326.88 | 389.03 |
| 15.0 | 77,426.84 | 394.63 | 
| 15.5 | 78,522.74 | 400.22 |
| 16.0 | 79,614.88 | 405.78 |
| 16.5 | 80,703.51 | 411.33 |
| 17.0 | 81,788.87 | 416.86 | 
| 17.5 | 82,871.17 | 422.38 | 
| 18.0 | 83,950.61 | 427.88 |
| 18.5 | 85,027.37 | 433.37 |
| 19.0 | 86,101.59 | 438.85 |
| 19.5 | 87,173.44 | 444.31 |
| 20.0 | 88,243.04 | 449.76 |

## Conclusion
Combustion chamber temperature and ISP have a linearly proportional relationship