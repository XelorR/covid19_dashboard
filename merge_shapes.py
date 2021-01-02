# coding: utf-8

import geopandas as gpd


SUBJECT_NAMES = {
    "Adygey": "Республика Адыгея",
    "Altay": "Алтайский край",
    "Amur": "Амурская область",
    "Arkhangel'sk": "Архангельская область",
    "Astrakhan'": "Астраханская область",
    "Bashkortostan": "Республика Башкортостан",
    "Belgorod": "Белгородская область",
    "Bryansk": "Брянская область",
    "Buryat": "Республика Бурятия",
    "Chechnya": "Чеченская Республика",
    "Chelyabinsk": "Челябинская область",
    "Chukot": "Чукотский автономный округ",
    "Chuvash": "Чувашская Республика",
    "City of St. Petersburg": "Санкт-Петербург",
    "Dagestan": "Республика Дагестан",
    "Gorno-Altay": "Республика Алтай",
    "Ingush": "Республика Ингушетия",
    "Irkutsk": "Иркутская область",
    "Ivanovo": "Ивановская область",
    "Kabardin-Balkar": "Кабардино-Балкарская Республика",
    "Kaliningrad": "Калининградская область",
    "Kalmyk": "Республика Калмыкия",
    "Kaluga": "Калужская область",
    "Kamchatka": "Камчатский край",
    "Karachay-Cherkess": "Карачаево-Черкесская Республика",
    "Karelia": "Республика Карелия",
    "Kemerovo": "Кемеровская область",
    "Khabarovsk": "Хабаровский край",
    "Khakass": "Республика Хакасия",
    "Khanty-Mansiy": "Ханты-Мансийский АО",
    "Kirov": "Кировская область",
    "Komi": "Республика Коми",
    "Kostroma": "Костромская область",
    "Krasnodar": "Краснодарский край",
    "Krasnoyarsk": "Красноярский край",
    "Kurgan": "Курганская область",
    "Kursk": "Курская область",
    "Leningrad": "Ленинградская область",
    "Lipetsk": "Липецкая область",
    "Maga Buryatdan": "Магаданская область",
    "Mariy-El": "Республика Марий Эл",
    "Mordovia": "Республика Мордовия",
    "Moscow City": "Москва",
    "Moskva": "Московская область",
    "Murmansk": "Мурманская область",
    "Nenets": "Ненецкий автономный округ",
    "Nizhegorod": "Нижегородская область",
    "North Ossetia": "Республика Северная Осетия — Алания",
    "Novgorod": "Новгородская область",
    "Novosibirsk": "Новосибирская область",
    "Omsk": "Омская область",
    "Orel": "Орловская область",
    "Orenburg": "Оренбургская область",
    "Penza": "Пензенская область",
    "Perm'": "Пермский край",
    "Primor'ye": "Приморский край",
    "Pskov": "Псковская область",
    "Rostov": "Ростовская область",
    "Ryazan'": "Рязанская область",
    "Sakha": "Республика Саха (Якутия)",
    "Sakhalin": "Сахалинская область",
    "Samara": "Самарская область",
    "Saratov": "Саратовская область",
    "Smolensk": "Смоленская область",
    "Stavropol'": "Ставропольский край",
    "Sverdlovsk": "Свердловская область",
    "Tambov": "Тамбовская область",
    "Tatarstan": "Республика Татарстан",
    "Tomsk": "Томская область",
    "Tula": "Тульская область",
    "Tuva": "Республика Тыва",
    "Tver'": "Тверская область",
    "Tyumen'": "Тюменская область",
    "Udmurt": "Удмуртская Республика",
    "Ul'yanovsk": "Ульяновская область",
    "Vladimir": "Владимирская область",
    "Volgograd": "Волгоградская область",
    "Vologda": "Вологодская область",
    "Voronezh": "Воронежская область",
    "Yamal-Nenets": "Ямало-Ненецкий автономный округ",
    "Yaroslavl'": "Ярославская область",
    "Yevrey": "Еврейская автономная область",
    "Zabaykal'ye": "Забайкальский край",
    "Crimea": "Республика Крым",
    "Sevastopol'": "Севастополь",
}

russia = gpd.read_file("zip://data/gadm36_RUS_shp.zip!gadm36_RUS_1.shp")
ukrain = gpd.read_file("zip://data/gadm36_UKR_shp.zip!gadm36_UKR_1.shp")

russia_fixed = russia.append(
    ukrain.loc[ukrain.NAME_1.isin(["Crimea", "Sevastopol'"])])
russia_fixed["region_name"] = russia_fixed.NAME_1.map(SUBJECT_NAMES)
russia_fixed.reset_index(inplace=True, drop=True)

russia_fixed.to_file("data/gadm36_RUS_1_fixed.json", driver="GeoJSON")
