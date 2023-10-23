import pandas as pd
from geopy.geocoders import Nominatim
import folium


def get_gps_coordinates(df):
    df["Lat"]= 0.0
    df["Lon"]= 0.0
    for i in range(len(df)):
        town = df.iloc[i]["Town"]
        country = df.iloc[i]["Country"]
        location = town+", "+country
        gn = Nominatim(user_agent="myapplication")
        loc = gn.geocode(location)
        if loc is not None:
            lat = loc.raw["lat"]
            lon = loc.raw["lon"]
            df["Lat"][i] = lat
            df["Lon"][i] = lon
    df.to_csv("grimurwithgps.csv")
    return df

if __name__ == "__main__":
    dataframe = pd.read_csv("/home/thorsteinnj/Documents/Grimur/dataframes/grimurtorkelin.csv")
    df = get_gps_coordinates(df=dataframe)
    df.to_csv("dataframes/grimurwithgps.csv")


