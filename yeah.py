import math

RadiusG = float(input("What is the radius of the garden?: "))

Area          = math.pi * math.pow(RadiusG,2)
Circumference = math.pi * 2 * RadiusG

SqrtArea      = math.sqrt(Area)

RoundDownArea = math.floor(Area)
RoundUpArea   = math.ceil(Area)

print(f"Area of the garden is {Area:.2f}")
print(f"Circumference of the garden is {Circumference:.2f}")
print(f"Square root of the area is {SqrtArea:.2f}")
print(f"Rounded down area is {RoundDownArea}")
print(f"Rounded up area is {RoundUpArea}")