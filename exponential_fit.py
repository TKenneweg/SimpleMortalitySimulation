import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import sys

from util import *



def exponential_func(age, m_0, r):
    return m_0 * r**age 

def main():
    ages, mortality_data = read_average_death_rates("deathrates.txt")

    start_age = 30
    end_age = 100
    ages = ages[start_age:end_age]
    mortality_data = mortality_data[start_age:end_age]
    
    popt, _ = curve_fit(exponential_func, ages, mortality_data, p0=[0.001, 1.01])
    best_m_0, best_r = popt
    print(f"Best-fit parameters:\nm_0 = {best_m_0}  r = {best_r}")
    y_fit = exponential_func(ages, best_m_0, best_r)

    print("Life Expectancy of Original Data: ", getLifeExpectancy(mortality_data)+start_age)
    print("Life Expectancy of Sim Data: ", getLifeExpectancy(y_fit)+start_age)

    plt.figure(figsize=(8, 5))
    plt.scatter(ages, mortality_data, label="Data", color="blue")
    plt.plot(ages, y_fit, label="Exponential Fit", color="red")
    plt.xlabel("Age")
    plt.ylabel("Average Mortality Rate")
    plt.title("Mortality Rate")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
