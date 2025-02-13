import matplotlib.pyplot as plt
from util import *

h = 1e-4 #step size in years

def main():

    r = 1.1030432364475082
    m_0 = 2.387993633642519e-05
    senescentCell_mortality = [m_0/2]
    inflammation_mortality = [m_0/2]
    age_steps = [0] 
    mortality_steps = [m_0] 
    intervened = False
    for i in range(int(110/h)):
        age_steps.append(age_steps[-1] + h)
        currentSenescentCellM = senescentCell_mortality[-1]
        currentInflammationM = inflammation_mortality[-1]

    ################ interventions ###############
        # #single intervention
        # if not intervened and age_steps[-1] > 70:
        #     currentSenescentCellM *= 0.1
        #     print(f"Intervened at {age_steps[-1]}")
            # intervened = True

        # #multiple interventions
        # if i % int(5/h) == 0 and age_steps[-1] > 50:
        #     currentSenescentCellM *= 0.1
        #     print(f"Intervened at {age_steps[-1]}")

        factor = 1 if age_steps[-1] > 30 else 1
        senescentCell_mortality.append(currentSenescentCellM + factor * h * np.log(r) * currentInflammationM)
        inflammation_mortality.append(currentInflammationM + h * np.log(r) * currentSenescentCellM) 
        mortality_steps.append(senescentCell_mortality[-1] + inflammation_mortality[-1])
    
######### limit range to 30 to 100 years ##########
    start_age = 30
    end_age = 100
    age_steps = age_steps[int(start_age/h):int(end_age/h)]
    mortality_steps = mortality_steps[int(start_age/h):int(end_age/h)]
    senescentCell_mortality = senescentCell_mortality[int(start_age/h):int(end_age/h)]
    inflammation_mortality = inflammation_mortality[int(start_age/h):int(end_age/h)]
    mortality_sim = mortality_steps[::int(1/h)]

    #read in data from file
    ages, mortality_data = read_average_death_rates("deathrates.txt")
    ages = ages[start_age:end_age]
    mortality_data = mortality_data[start_age:end_age]


    print("Life Expectancy of Original Data: ", getLifeExpectancy(mortality_data)+start_age)
    print("Life Expectancy of Sim Data: ", getLifeExpectancy(mortality_sim)+start_age)

    # plt.plot(ages,mortality_sim, label = "Total Mortality")
    plt.plot(age_steps,mortality_steps, label = "Total Mortality")
    plt.plot(age_steps,senescentCell_mortality, label="Senescent Cell Mortality")
    plt.plot(age_steps,inflammation_mortality, label = "Inflammation Mortality")
    plt.scatter(ages, mortality_data, label="Mortality Data", color="blue")
    # plt.yscale('log')
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.title("Evolution of x(t) using RK4")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
