def number_to_words_inr(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    denominations = ["", "Thousand", "Lakh", "Crore", "Arab"]

    def convert_chunk(num):
        words = ""
        if num >= 100:
            words += ones[num // 100] + " Hundred "
            num %= 100
        if num >= 20:
            words += tens[num // 10] + " "
            num %= 10
        elif num >= 10:
            words += teens[num - 10] + " "
            num = 0
        if num > 0:
            words += ones[num] + " "
        return words.strip()

    if n == 0:
        return "Zero"

    words = ""
    parts = []
    parts.append(n % 1000)  # Hundreds
    n //= 1000
    parts.append(n % 100)  # Thousands
    n //= 100
    parts.append(n % 100)  # Lakhs
    n //= 100
    parts.append(n)  # Crores

    for i in range(len(parts)):
        if parts[i]:
            words = convert_chunk(parts[i]) + " " + denominations[i] + " " + words

    return words.strip()

def calculate_wealth(n, s, si, i, r):
    wealth = 0
    monthly_savings = s  # Initial monthly savings
    max_savings = 4000000  # Maximum allowed yearly savings
    start_year = 2025  # Start from 2025

    
    
    
    print("\nYear | Yearly Savings | Total Wealth | Inflation Adjusted Wealth")
    print("-" * 60)

    yearly_savings = monthly_savings * 12  # Convert monthly to yearly savings

    for year in range(1, n + 1):
        wealth += yearly_savings
        wealth *= (1 + r / 100)  # Apply returns

        # Adjust wealth for inflation
        inflation_adjusted_wealth = wealth / ((1 + i / 100) ** year)

        print(f"{year:4} | {yearly_savings:14.2f} | {wealth:12.2f} | {inflation_adjusted_wealth:22.2f}")

        # Increase savings for the next year but cap at max_savings
        yearly_savings = min(yearly_savings * (1 + si / 100), max_savings)

    print("\nInput Parameters:")
    print(f"Total Years: {n},\nInitial Monthly Savings: {s}\nYearly Increase: {si}%\nInflation Rate: {i}%\nReturn Rate: {r}%")
    print("\nFinal Wealth Summary:")
    print(f"Total Wealth after {n} years: {wealth:.2f}")
    print(f"In words: {number_to_words_inr(int(wealth))} Rupees\n")
    print(f"Inflation Adjusted Wealth: {inflation_adjusted_wealth:.2f}")
    print(f"In words: {number_to_words_inr(int(inflation_adjusted_wealth))} Rupees")

# Input Parameters
n = 20  # Total Years
s = 15000  # Initial Monthly Savings
si = 50  # Yearly Increase in savings (%) upto max: 40L
i = 5  # Yearly Inflation Rate (%)
r = 14  # Yearly Returns (%)

calculate_wealth(n, s, si, i, r)

'''

Year | Yearly Savings | Total Wealth | Inflation Adjusted Wealth
------------------------------------------------------------
   1 |      180000.00 |    205200.00 |              195428.57
   2 |      270000.00 |    541728.00 |              491363.27
   3 |      405000.00 |   1079269.92 |              932313.94
   4 |      607500.00 |   1922917.71 |             1581989.16
   5 |      911250.00 |   3230951.19 |             2531534.80
   6 |     1366875.00 |   5241521.85 |             3911304.31
   7 |     2050312.50 |   8312691.16 |             5907674.41
   8 |     3075468.75 |  12982502.30 |             8787068.58
   9 |     4000000.00 |  19360052.62 |            12479662.54
  10 |     4000000.00 |  26630459.99 |            16348792.34
  11 |     4000000.00 |  34918724.39 |            20416254.95
  12 |     4000000.00 |  44367345.81 |            24705398.29
  13 |     4000000.00 |  55138774.22 |            29241269.22
  14 |     4000000.00 |  67418202.61 |            34050773.59
  15 |     4000000.00 |  81416750.97 |            39162849.29
  16 |     4000000.00 |  97375096.11 |            44608653.48
  17 |     4000000.00 | 115567609.57 |            50421765.25
  18 |     4000000.00 | 136307074.90 |            56638405.03
  19 |     4000000.00 | 159950065.39 |            63297672.30
  20 |     4000000.00 | 186903074.55 |            70441803.11

Input Parameters:
Total Years: 20,
Initial Monthly Savings: 15000
Yearly Increase: 50%
Inflation Rate: 5%
Return Rate: 14%

Final Wealth Summary:
Total Wealth after 20 years: 186903074.55
In words: Eighteen Crore Sixty Nine Lakh Three Thousand Seventy Four Rupees

Inflation Adjusted Wealth: 70441803.11
In words: Seven Crore Four Lakh Forty One Thousand Eight Hundred Three Rupees
'''
