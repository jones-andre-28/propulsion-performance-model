# Experiment: Effect of Mass Flow Rate
### 7/7/26

## Current Assumptions
Specific Heat Ratio = 1.22 \n
Gas Constant = 287 \n
Chamber Temperature = 3000 \n

## Input changed:
mdot increased from 10 to 20

## Prediction before running:
Thrust should double \n
Isp should decrease 

## Observed:
Thrust increased by 78.3% \n
Isp decreased by 10.8%

## Rough Explanation:
Thrust increased as it is dependent on the mass flow rate proportionally however it is not a 100% increase as it is equivalent to the momentum + pressure so the value provided by a constant pressure will dilute the increase. This means pressure should increase to reach 100% increase.
\n 
ISP decreasd since the denominator increases faster than the numerator and as there was not a totally efficient increase in Thrust, the Isp is decreased even more

### Edit: 7/20/26
Numbers are not doubled as the Ve equation (which is in the momentum_thrust equation of m-dot * Ve) contains a square root, meaning 2x inputs only produces 1.4x output

# Experiment: Limits of ISP
## Chamber pressure
### 7/20/26

## Constants
gamma = 1.22 \n
R = 287 \n
Tc = 3000 \n
g0 = 9.81 \n
eps = 20 \n
Pa = 101325 \n
mdot = 20 \n

## Variable
Pc: 2e6 < x < 5e6 \n
inc = 0.25e6 \n

## Results
### Pc           Thrust                    ISP
2.0     43659.21023378106       222.52400730775256 \n
2.25    44742.97089625777       228.04776195850033 \n
2.5     45747.914069986444      233.16979648311133 \n
2.75
3.0
3.25
3.5
3.75
4.0
4.25
4.5
4.75
5