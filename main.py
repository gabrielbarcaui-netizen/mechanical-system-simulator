import matplotlib.pyplot as plt
from modules import vibration, vehicle_dynamics, heat_transfer, mechanisms, control

print("1 - Vibração")
print("2 - Veículo")
print("3 - Calor")
print("4 - Mecanismo")
print("5 - Controle")

choice = input("Escolha: ")

if choice == "1":
    t, x = vibration.simulate()
    plt.plot(t, x)

elif choice == "2":
    t, v = vehicle_dynamics.simulate()
    plt.plot(t, v)

elif choice == "3":
    T = heat_transfer.simulate()
    plt.plot(T)

elif choice == "4":
    theta, x = mechanisms.simulate()
    plt.plot(theta, x)

elif choice == "5":
    t, x = control.simulate()
    plt.plot(t, x)

plt.grid()
plt.show()
