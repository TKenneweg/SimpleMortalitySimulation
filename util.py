
import numpy as np

def to_fraction(y, pos):
    return f'{y:.2%}'



def read_average_death_rates(file_path):
    """
    Reads a mortality text file and returns two lists:
      - ages: A sorted list of unique ages (integer, with '110+' treated as 110).
      - avg_rates: The corresponding average 'Total' death rates, across all years, for each age.
    """
    from collections import defaultdict
    import statistics
    
    # Dictionary to accumulate total death rates by age
    # Key: age (int), Value: list of "Total" death rates
    age_to_rates = defaultdict(list)
    
    with open(file_path, 'r') as f:
        # Skip the header line
        header = next(f)
        
        for line in f:
            line = line.strip()
            # Skip empty or malformed lines
            if not line:
                continue

            columns = line.split()
            # We expect 5 columns: Year, Age, Female, Male, Total
            if len(columns) != 5:
                continue
            
            year_str, age_str, female_str, male_str, total_str = columns
            
            # Convert age_str to an integer (including '110+')
            try:
                if age_str.endswith('+'):
                    age_val = 110
                else:
                    age_val = int(age_str)
            except ValueError:
                # If we can't parse the age, skip
                continue
            
            # Convert the total death rate to float
            try:
                total_val = float(total_str)
            except ValueError:
                # If we can't parse the total, skip
                continue
            
            # Accumulate this rate under the given age
            age_to_rates[age_val].append(total_val)
    
    # Now compute the average for each age
    ages_sorted = sorted(age_to_rates.keys())
    avg_rates = []
    for age in ages_sorted:
        avg_rates.append(statistics.mean(age_to_rates[age]))
    

    ages_sorted = np.array(ages_sorted, dtype=float)        # ages
    avg_rates = np.array(avg_rates, dtype=float)   # average mortality rates

    return ages_sorted, avg_rates





def getLifeExpectancy(mortalityByAge):
    le = 0 
    for age in range(len(mortalityByAge)):
        chanceofDyingAtAge = 1
        for j in range(age):
            chanceofDyingAtAge *= (1-mortalityByAge[j])
        chanceofDyingAtAge *= mortalityByAge[age]
        le += chanceofDyingAtAge * age
    chanceofSurvivingToMaxAge = 1


    #add all the survivors to the max age
    for j in range(len(mortalityByAge)):
        chanceofSurvivingToMaxAge *= (1-mortalityByAge[j])
    le += chanceofSurvivingToMaxAge * len(mortalityByAge)
    return le 
