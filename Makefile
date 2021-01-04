all: data/gadm36_RUS_1_fixed.json data/covid19_data_ru_government.csv data/covid19ru_rolling_weeks.csv

clean:
	rm -rf data

data/covid19_data_ru_government.csv: get_governmental.py
	python3 $<

data/gadm36_RUS_1_fixed.json: merge_shapes.py data/gadm36_RUS_shp.zip data/gadm36_UKR_shp.zip
	python3 $<

data/gadm36_RUS_shp.zip:
	wget -P data/ https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_RUS_shp.zip

data/gadm36_UKR_shp.zip:
	wget -P data/ https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_UKR_shp.zip

data/covid19_data_ru_government_with_additional_variables.csv: calculate_additional_variables.py data/covid19_data_ru_government.csv
	python3 $<

data/covid19ru_rolling_weeks.csv: calculate_rolling_weeks.py data/covid19_data_ru_government_with_additional_variables.csv
	python3 $<
