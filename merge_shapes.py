# coding: utf-8

import geopandas as gpd

russia = gpd.read_file("zip://data/gadm36_RUS_shp.zip!gadm36_RUS_1.shp")
ukrain = gpd.read_file("zip://data/gadm36_UKR_shp.zip!gadm36_UKR_1.shp")

russia_fixed = russia.append(
    ukrain.loc[ukrain.NAME_1.isin(["Crimea", "Sevastopol'"])])

russia_fixed.to_file("data/gadm36_RUS_1_fixed.json", driver="GeoJSON")
