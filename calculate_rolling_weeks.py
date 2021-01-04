# coding: utf-8
# This script will calculate last available 7 days sum and 7 days sum before last available 7 days

import pandas as pd

df = pd.read_csv("data/covid19_data_ru_government_with_additional_variables.csv", parse_dates=["date"])
df.head()

last_week = df.date.sort_values().unique()[-7:]
previous_week = df.date.sort_values().unique()[-14:-7]

df_last_week = (
    df.loc[df["date"].isin(last_week)]
    .groupby(["region_name"], as_index=False)[
        ["sick_new", "healed_new", "died_new"]
    ]
    .sum()
)

df_previous_week = (
    df.loc[df["date"].isin(previous_week)]
    .groupby(["region_name"], as_index=False)[
        ["sick_new", "healed_new", "died_new"]
    ]
    .sum()
)


df_last_week["week"] = "last"
df_previous_week["week"] = "previous"
df_calculated = df_last_week.append(df_previous_week)

df_calculated.to_csv("data/covid19ru_rolling_weeks.csv", index=False)
