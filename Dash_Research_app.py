from dash import Dash, html, dcc
import pandas as pd


## data sources to be used for this project

bacteria = pd.read_excel("data/Bacteria_Firebird_ALL_2_6_2022.xlsx")
cold_finger = pd.read_excel("data/Cold_Finger_Firebird_ALL_2_6_2022.xlsx")
coupon = pd.read_excel("data/Coupon_Firebird_ALL_2_6_2022.xlsx")
cwa = pd.read_excel("data/CWA_Firebird_ALL_2_6_2022.xlsx")
deposit = pd.read_excel("data/Deposit_Firebird_ALL_2_6_2022.xlsx")
feMnP = pd.read_excel("data/FeMnP_Firebird_ALL_2_6_2022.xlsx")
millipore = pd.read_excel("data/millipore_Firebird_ALL_2_6_2022.xlsx")
oil_grease = pd.read_excel("data/OG_Firebird_ALL_2_6_2022.xlsx")
oil_finger = pd.read_excel("data/Oil_FingerPrint_Firebird_ALL_2_6_2022.xlsx")

app = dash.Dash(__name__)

bacteria.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician","Sample Type"])
cold_finger.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician"])
coupon.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician"])
cwa.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician"])
deposit.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician"])
feMnP.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician"])
millipore.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician"])
oil_grease.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician"])
oil_finger.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician",])