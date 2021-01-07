import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

shapes = gpd.read_file("data/gadm36_RUS_1_fixed.json")
rolling_weeks = pd.read_csv("data/covid19ru_rolling_weeks.csv")
annotations = pd.read_csv("data/data_for_annotations.csv")

rolling_weeks_sick_new = (
    rolling_weeks.set_index(["region_name", "week"])[["sick_new"]]
    .unstack()
    .reset_index()
)

rolling_weeks_sick_new.columns = [
    "region_name",
    "sick_new_last_week",
    "sick_new_previous_week",
]
rolling_weeks_sick_new["sick_temp_increase"] = (
    rolling_weeks_sick_new.sick_new_last_week
    / rolling_weeks_sick_new.sick_new_previous_week
    - 1
)

gdf = shapes.merge(rolling_weeks_sick_new)
gdf_with_employees = gdf.merge(annotations)
gdf_mercator = gdf_with_employees.to_crs(epsg=3857)

ax = gdf_mercator.plot(
    figsize=(17, 10),
    column="sick_temp_increase",
    cmap="OrRd",
    alpha=0.7,
    edgecolor="r",
    legend=True,
    legend_kwds={"label": "COVID19 sick rate change"},
)

gdf_mercator.apply(
    lambda x: ax.annotate(
        s=x.annotation_col, xy=x.geometry.representative_point().coords[0], ha="center"
    ),
    axis=1,
)

ax.set_xlim(0.21 * 1e7, 2.0 * 1e7)
ax.set_axis_off()

ctx.add_basemap(ax)

plt.savefig("data/covid19_map.png")
