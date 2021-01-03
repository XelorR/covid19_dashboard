all: data/gadm36_RUS_1_fixed.json data/covid19_data_ru_government.csv

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
