***Tracking: incorrect assumptions, confusing outputs, bugs in equations, misunderstood physics***


# Effect of mass flow rate on thrust and specific impulse 
### 7/7/26
## Initial Assumption
Increasing mass flow rate would double thrust because thrust is proportional to mdot

Increasing mass flow rate would decrease Isp because 
mdot is in the denominator.

## Issue identified
Total thrust is not solely depednent on momentum thrust:
    F = momentum_thrust = pressure_thrust
Only the momentum component scales with mdot while pressure remained constant under fixed Pc, Pa, and nozzle conditions
Therefore, total thrust increased less than proportionally

## Validation experiemnt
Increased mdot from 10 -> 20 kg/s
Thrust increased 78.3%
Isp decreased 10.8%

## Key takeaway
A variable appearing in an equation does not necesarily control the entire system response
Coupled systems require examining all contributing terms
Isp depends on the relationship between thrust growth and mass flow growth, not simple the presence of mdot in the denominator 

## Assumptions to Investigate
Changing mass flow rate independently while holding chamber pressure and nozzle geometry constant may not represent a realistic engine design change