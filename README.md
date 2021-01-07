# Covid 19 map generator

## Goals

My personal progect with following goals:

- get data from [official russian source](https://стопкоронавирус.рф/information/)
- undertand how to create choropleth maps with annotations using python
- merge complete Rusian shape (with Crimea and Sevastopol) from shapes found on [gadm.org](https://gadm.org/)
- keep examples somewhere for further references

## Setup

First, install all requirements from [requirements.txt](./requirements.txt).

It is better to use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) since it installs all geopandas dependencies automatickly.

If you want to use [pip](https://pip.pypa.io/en/latest/user_guide/), please refer [geopandas documentation](https://geopandas.org/install.html) to install it's dependencies.

Please note that full generation process is automated via [GNU Make](https://www.gnu.org/software/make/), so plese install it too.

## Run and usage

#### To just run and generate with defaults:

```
git clone https://github.com/XelorR/covid19_map_ru
cd covid19_map_ru
make
```

#### To refresh:

```
make refresh
```

#### To customize annotations:

just edit data/data_for_annotations.csv like this:

```
vim ./data/data_for_annotations.csv
```

or using your favorite spreadsheets editor.

#### If you just need geojson with all 85 federal subjects:

```
make data/gadm36_RUS_1_fixed.json
```

## Map examples:

- [geopandas version](geopandas_map_example.ipynb)
- [plotly version](plotly_map_example.ipynb)

---

**For further references please read [Makefile](./Makefile)**

