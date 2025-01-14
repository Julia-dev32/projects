def main():
    mass = float(input("Enter the objects mass in kilograms: "))
    velocity = float(input("Enter th objects velocity in meters per second: "))
    kinetic_energy = formula(mass, velocity)
    print(f"The kinetic energy is: {kinetic_energy:.2f}joules")
def formula(mass, velocity):
    return 0.5 * mass * (velocity ** 2)
main()