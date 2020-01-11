
# to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
def calc_fuel_req(mass: int) -> int:
    return (mass // 3) - 2

# Unit tests
#For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
#For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
#For a mass of 1969, the fuel required is 654.
#For a mass of 100756, the fuel required is 33583.
assert calc_fuel_req(12) == 2
assert calc_fuel_req(14) == 2
assert calc_fuel_req(1969) == 654
assert calc_fuel_req(100756) == 33583


with open("input.txt") as f:
    masses = [int(line.strip()) for line in f.readlines()]

# Part 1:
total_fuel_req = sum(calc_fuel_req(mass) for mass in masses)
print("(pt.1 ans) Fuel needed:", total_fuel_req)


# Part 2: Need also fuel for fuel, and so on

def calc_fuel_req_considering_fuel(mass: int) -> int:
    total_fuel = 0
    additional_fuel_needed = calc_fuel_req(mass)
    
    while additional_fuel_needed > 0:
        total_fuel += additional_fuel_needed
        additional_fuel_needed = calc_fuel_req(additional_fuel_needed)  # fuel need for the added fuel

    return total_fuel

# Unit tests
assert calc_fuel_req_considering_fuel(14) == 2
assert calc_fuel_req_considering_fuel(100756) == 50346

# What is the sum of the fuel requirements for all of the modules on your spacecraft 
# when also taking into account the mass of the added fuel?
total_fuel_req_pt2 = sum(calc_fuel_req_considering_fuel(mass) for mass in masses)
print("(pt.1 ans) Fuel needed:", total_fuel_req_pt2)