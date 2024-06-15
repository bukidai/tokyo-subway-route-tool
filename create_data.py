import pandas as pd

station = pd.read_csv("station20240426free.csv")
line = pd.read_csv("line20240426free.csv")

metro_station = station.loc[
    (station["line_cd"] >= 28001) & (station["line_cd"] <= 28010)
]

cols = ["station_g_cd", "station_name", "lon", "lat"]
metro_station = metro_station[cols]
metro_station.to_csv("metro_station.csv", index=False, encoding="utf-8")

toei_station = station.loc[
    (station["line_cd"] >= 99301) & (station["line_cd"] <= 99304)
]
toei_station = toei_station[cols]
toei_station.to_csv("toei_station.csv", index=False, encoding="utf-8")

metro_line = line.loc[(line["company_cd"] == 18)]
cols = ["line_cd", "line_name", "line_color_c"]
metro_line = metro_line[cols]
metro_line.to_csv("metro_line.csv", index=False, encoding="utf-8")

toei_line = line.loc[(line["company_cd"] == 119)]
toei_line = toei_line[cols]
toei_line.to_csv("toei_line.csv", index=False, encoding="utf-8")
