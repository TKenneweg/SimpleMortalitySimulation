import matplotlib.pyplot as plt
from util import *
import sys

h = 1e-4 #step size

#change_of_mortality = constant * mortality!

def main():
    mortality_0 = 2.387993633642519e-05
    r = 1.1030432364475082
    age_steps = [0]  # initial age
    mortality_steps = [mortality_0]  # initial mortality value
    for i in range(int(110/h)):
        age_steps.append(age_steps[-1] + h)
        current_mortality = mortality_steps[-1]
        mortality_steps.append(current_mortality +h * np.log(r) * current_mortality)
    

    start_age = 30
    end_age = 100
    mortality_steps = mortality_steps[int(start_age/h):int(end_age/h)]
    mortality_sim = mortality_steps[::int(1/h)]
    
    ages, mortality_data = read_average_death_rates("deathrates.txt")
    ages = ages[start_age:end_age]
    mortality_data = mortality_data[start_age:end_age]

    print("Life Expectancy of Original Data: ", getLifeExpectancy(mortality_data)+start_age)
    print("Life Expectancy of Sim Data: ", getLifeExpectancy(mortality_sim)+start_age)


    plt.plot(ages,mortality_sim)
    plt.scatter(ages, mortality_data, label="Data", color="blue")
    plt.xlabel("Age")
    plt.ylabel("Mortality")
    plt.title("Evolution of M(t)")
    plt.show()

if __name__ == '__main__':
    main()
