import matplotlib.pyplot as plt
import pandas
import opioids
opioid_deaths = opioids.get_opioid_deaths()

#I want every death per race for the year of 1999 and then graph it

#narrowing year down to 1999
for year in opioid_deaths:
    if year["Year"] == 1999:
        year_1999 = year
        break

#deaths by race
deaths = year_1999["Number"]["Opioid"]

types = list(deaths.keys())
counts = list(deaths.values())

plt.figure(figsize=(10, 6))
plt.bar(types, counts, color="teal")
plt.title("Opioid Deaths by Type (1999)")
plt.xlabel("Opioid Type")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("opioids")