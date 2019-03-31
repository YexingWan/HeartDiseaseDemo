
import pandas as pd
import folium
import utm
import os
from folium import FeatureGroup, LayerControl, Map, Marker


def gen_map():
    m = folium.Map(location=[-33.865143, 151.209900],
                   tiles='Stamen Terrain',
                   zoom_start=10)

    df_fail = pd.read_csv('bla')
    df_segment_point = pd.read_csv('bla')
    df_pipe = pd.read_csv('bla')

    # TODO: merge data of seg and pipe
    df_poly = []



    feature_group_1 = FeatureGroup(name='Pailure')
    feature_group_2 = FeatureGroup(name='Pipe Infomation')


    def gen_circleMarker_list(df, tip, color):
        marker_list = []
        for index, row in df[(df['X'] != 0) & (df['Y'] != 0)].iterrows():
            loc = utm.to_latlon(row['X'], row['Y'], 56, 'H')
            marker_list.append(
                folium.CircleMarker(
                    location=loc,
                    radius=3,
                    popup=row['failure type'],
                    color=color,
                    fill=True,
                    fill_color=color,
                    tooltip=tip)
            )
        return marker_list

    # TODO: gen ployline objects list
    def gen_ployline_list(df, tip, color):
        pass


    for marker in gen_circleMarker_list(df_fail, 'click', 'crimson'):
        marker.add_to(feature_group_1)

    for line in gen_ployline_list(df_poly, 'click', 'blue'):
        line.add_to(feature_group_2)

    feature_group_1.add_to(m)
    feature_group_2.add_to(m)
    LayerControl().add_to(m)
    return m







