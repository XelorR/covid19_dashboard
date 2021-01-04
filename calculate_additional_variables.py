# -*- coding: utf-8 -*-

# This sctipt will calculate the following fields for "covid19_data_ru_government.csv":
#
# - sick_new
# - healed_new
# - died_new
# - active ( = sick - healed - died )

import pandas as pd


def uncummulate(arr: list) -> list:
    """
    Convert cummulative sum to individual values
    """
    individual_values = list()
    for element_index, element_value in enumerate(sorted(arr, reverse=True)):
        try:
            individual_values.append(element_value - arr[element_index + 1])
        except IndexError:
            individual_values.append(None)
    return individual_values


df = pd.read_csv("data/covid19_data_ru_government.csv")
df.head()

df_calculated = pd.DataFrame()
for region in df["region_name"].unique():

    df_temp = df.loc[df["region_name"] == region]

    for col in ["sick", "healed", "died"]:
        df_temp[col + "_new"] = uncummulate(df_temp[col].values)
    df_temp["active"] = df_temp["sick"] - df_temp["healed"] - df_temp["died"]

    df_calculated = df_calculated.append(df_temp)

df_calculated.to_csv(
    "data/covid19_data_ru_government_with_additional_variables.csv", index=False
)
