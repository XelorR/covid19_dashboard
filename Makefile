all: data/covid19_map.png

clean:
	rm -rf data/*.png data/*.zip data/*.json data/covid*

clean_data:
	rm -rf data/covid* data/geopandas_map_example.png

refresh: clean_data all

data/covid19_data_ru_government.csv: src/get_governmental.py
	python3 $<

data/gadm36_RUS_1_fixed.json: src/merge_shapes.py data/gadm36_RUS_shp.zip data/gadm36_UKR_shp.zip
	python3 $<

data/gadm36_RUS_shp.zip:
	wget -P data/ https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_RUS_shp.zip

data/gadm36_UKR_shp.zip:
	wget -P data/ https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_UKR_shp.zip

data/covid19_data_ru_government_with_additional_variables.csv: src/calculate_additional_variables.py data/covid19_data_ru_government.csv
	python3 $<

data/covid19ru_rolling_weeks.csv: src/calculate_rolling_weeks.py data/covid19_data_ru_government_with_additional_variables.csv
	python3 $<

data/covid19_map.png: src/gen_map.py data/gadm36_RUS_1_fixed.json data/covid19ru_rolling_weeks.csv data/data_for_annotations.csv
	python3 $<
