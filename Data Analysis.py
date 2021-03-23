import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
corona_dataset = pd.read_csv('covid19_Confirmed_dataset.csv')
print(corona_dataset.head(5))

print(corona_dataset.shape)

corona_dataset.drop(["Lat","Long"],axis=1,inplace=True)

print(corona_dataset.head(5))
agr=corona_dataset.groupby("Country/Region").sum()
print(agr.head(5))


print(agr.loc['Italy'].diff().max())

countries = list(agr.index)
print(countries)
max_infection_rates = [] 
for c in countries :
    max_infection_rates.append(agr.loc[c].diff().max())
agr['max_infection_rates']=max_infection_rates
print(agr.head(5))
corona_data = pd.DataFrame(agr['max_infection_rates'])
print(corona_data.head(5))

happiness_report_csv = pd.read_csv("worldwide_happiness_report.csv")

print(happiness_report_csv.head(5))
useless_cols=["Overall rank","Score","Generosity","Perceptions of corruption"]
happiness_report_csv.drop(useless_cols,axis=1,inplace=True)
print(happiness_report_csv.head(5))

happiness_report_csv.set_index("Country or region",inplace=True)

print(happiness_report_csv.head(5))
print(corona_data.head(5))
print(corona_data.shape)
data = happiness_report_csv.join(corona_data,how="inner")
print(data.head(5))

print(data.corr())