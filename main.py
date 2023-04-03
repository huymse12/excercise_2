import pandas as pd
import mysql.connector
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


def convert_string_to_datetime(value):
    value_arr = value.split("/")
    datetime_object = datetime(int(value_arr[2]), int(value_arr[1]), int(value_arr[0]))
    return datetime_object


def get_data_csv(link):
    df = pd.read_csv(link)
    return df


def convert_money_to_float(value):
    value = value.lstrip("$")
    value = value.replace(",", "")
    value = float(value)
    return float(value)


def connect_my_sql():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database="Films"
    )
    return mydb


def get_top_data(db, top):
    pass


def insert_data():
    db = connect_my_sql()
    cursor = db.cursor()
    data_frame = get_data_csv('cost_revenue_dirty.csv')
    for index, data in data_frame.iterrows():
        sql = "insert into FilmsRevenue(RankFilm, MovieTitle, ProductionBudget, WorldwideGross, DomesticGross) " \
              "VALUES (%s,%s,%s,%s,%s)"
        val = (data['Rank'], data['Movie Title'],
               convert_money_to_float(data['Production Budget ($)']),
               convert_money_to_float(data['Worldwide Gross ($)']),
               convert_money_to_float(data['Domestic Gross ($)']))
        cursor.execute(sql, val)
        db.commit()


def visualize_data_bar(x, y):
    fig, ax = plt.subplots()

    hbars = ax.barh(x, y, align='center')
    ax.set_yticks(x, labels=x)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('World wide gross')
    ax.set_title('Revenue')

    # Label with specially formatted floats
    ax.bar_label(hbars, fmt='%.2f')
    plt.show()


def run_app():
    db = connect_my_sql()
    cursor = db.cursor()
    cursor.execute("select MovieTitle , WorldwideGross  from FilmsRevenue limit 5")
    data = cursor.fetchall()
    arr_movie_title = []
    arr_ww_gross = []
    for value in data:
        arr_movie_title.append(value[0])
        arr_ww_gross.append(value[1])

    x = np.array(arr_movie_title)
    y = np.array(arr_ww_gross)

    visualize_data_bar(x, y)


run_app()
