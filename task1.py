import pandas as pd
import matplotlib.pyplot as plt


ds = pd.read_csv('C:/Users/thris/OneDrive/Desktop/datascience/dataset1/population/API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv', skiprows=3)


ds_clean = ds.drop(columns=['Unnamed: 68'])

ds_clean = ds[['Country Name', 'Country Code', 'Indicator Name', '2020']]

ds_clean = ds_clean.dropna(subset=['2020'])

ds_first10 = ds_clean.head(10)

plt.figure(figsize=(10,8))
plt.barh(ds_first10['Country Name'], ds_first10['2020'], color='lightblue')
plt.title('Population Distribution by Country in 2020')
plt.xlabel('Population')
plt.ylabel('Country')
plt.tight_layout()
plt.show()