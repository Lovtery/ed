def greenhouse():

    plant_height = int(input("введите рост вашего растения "))

    def measure_growth():
        nonlocal plant_height
        plant_height += 2
    measure_growth()
    measure_growth()
    return plant_height

print(greenhouse())


