import matplotlib.pyplot as plt

def gas_and_liquid_amortizator(m, legs, g, V, y, h, S, T_0, T_critical_walls, T_critical_gas, P_0, P_critical, M_gas, i, p_body, volume_body, c, p_liquid, dt, max_oscillation):
    R = 8.31 #Унверсальная газовая постоянная.
    t = 0
    the_oscillation = 1
    m /= legs
    P_gas = []
    T_gas = []
    y_coordinate = []
    speed = []
    time_of_oscillation = []
    while the_oscillation <= max_oscillation:
        while y > h:
            P_gas.append(P_0)
            T_gas.append(T_0)
            y_coordinate.append(y)
            speed.append(V)
            time_of_oscillation.append(t)
            #Изменение координаты поршня относительно дна газовой камеры.
            y += V * dt
            #Изменение скорости аппарата.
            V -= g * dt
            #Изменение времени, прошедшего с начала процесса.
            t += dt
        while y <= h and V <= 0:
            #Изменение давления газа.
            P_gas.append(P_0 * (h / y)**((2 + i) / i))
            #Изменение температуры газа.
            T_gas.append(T_0 * (h / y)**(2 / i))
            y_coordinate.append(y)
            speed.append(V)
            time_of_oscillation.append(t)
            y += V * dt
            #Изменение скорости аппарата.
            V += (P_0 * S * (h / y)**((2 + i) / i) + c * V**2 - g * (m + volume_body * (p_body - p_liquid))) / m * dt
            t += dt
        while y <= h and V > 0:
            P_gas.append(P_0 * (h / y)**((2 + i) / i))
            T_gas.append(T_0 * (h / y)**(2 / i))
            y_coordinate.append(y)
            speed.append(V)
            time_of_oscillation.append(t)
            y += V * dt
            V += (P_0 * S * (h / y)**((2 + i) / i) - c * V**2 - g * (m + volume_body * (p_body - p_liquid))) / m * dt
            t += dt
        the_oscillation += 1
    if max(P_gas) < P_critical:
        if max(T_gas) < T_critical_walls:
            if max(T_gas) < T_critical_gas:
                print(f"The gas will have {round(M_gas * h * S * P_0 / (R * T_0), 4)} kilogram.")
                print(f"Time of oscillations is {round(t / (max_oscillation + 0.5) * max_oscillation, 4)} seconds.")
                plt.subplot(2,2,1)
                plt.plot(time_of_oscillation, y_coordinate, "black")
                plt.grid()
                plt.title("Зависимость координаты крепления от времени.")
                plt.subplot(2,2,2)
                plt.plot(time_of_oscillation, speed, "gray")
                plt.grid()
                plt.title("Зависимость скорости точки крепления от времени.")
                plt.subplot(2,2,3)
                plt.plot(time_of_oscillation, P_gas, "red")
                plt.grid()
                plt.title("Зависимость давления газа от времени.")
                plt.subplot(2,2,4)
                plt.plot(time_of_oscillation, T_gas, "green")
                plt.grid()
                plt.title("Зависимость температуры газа от времени.")
                plt.show()
            elif max(T_gas) >= T_critical_gas:
                print("The gas will ionize.")
        elif max(T_gas) >= T_critical_walls:
            print("The walls will melt.")
    elif max(P_gas) >= P_critical:
        print("The walls will berak.")
gas_and_liquid_amortizator(
    m = float(input("Choose mass of the spacecraft.")),
    legs = int(input("Choose a number of legs on the machine.")),
    g = float(input("Choose acceleration on the space object.")),
    V = float(input("Choose speed of starting.")),
    y = float(input("Choose height upon the liquid.")),
    h = float(input("Choose height of the gas camera.")),
    S = float(input("Choose the piston area.")),
    T_0 = float(input("Choose temperature of the as.")),
    T_critical_walls = float(input("Choose max temperature of the walls.")),
    T_critical_gas = float(input("Choose max temperature of the gas.")),
    P_0 = float(input("Choose pressure of the gas.")),
    P_critical = float(input("Choose max pressure of the walls.")),
    M_gas = float(input("Choose molar mass of the gas.")),
    i = int(input("Choose degree of freedom of the gas.")),
    p_body = float(input("Choose density of the bar.")),
    volume_body = float(input("Choose volume of the bar.")),
    c = float(input("Choose the viscosity coefficient of the liquid.")),
    p_liquid = float(input("Choose density of the liquid.")),
    dt = float(input("Choose time interval.")),
    max_oscillation = int(input("Choose number of oscillation."))
)