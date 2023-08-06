import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("../../dataset/demo.xlsx")
df = df.drop(df.tail(20).index)
df = df.iloc[:, 6:10]

selected_0 = df[df['婴儿行为特征'] == '中等型']
selected_1 = df[df['婴儿行为特征'] == '安静型']
selected_2 = df[df['婴儿行为特征'] == '矛盾型']

CBTS_中等型_max = selected_0['CBTS'].max()
CBTS_中等型_min = selected_0['CBTS'].min()
CBTS_中等型_mean = selected_0['CBTS'].mean()

EPDS_中等型_max = selected_0['EPDS'].max()
EPDS_中等型_min = selected_0['EPDS'].min()
EPDS_中等型_mean = selected_0['EPDS'].mean()

HADS_中等型_max = selected_0['HADS'].max()
HADS_中等型_min = selected_0['HADS'].min()
HADS_中等型_mean = selected_0['HADS'].mean()

print("CBTS_中等型_max", CBTS_中等型_max)
print("CBTS_中等型_min", CBTS_中等型_min)
print("CBTS_中等型_mean", CBTS_中等型_mean)
print("EPDS_中等型_max", EPDS_中等型_max)
print("EPDS_中等型_min", EPDS_中等型_min)
print("EPDS_中等型_mean", EPDS_中等型_mean)
print("HADS_中等型_max", HADS_中等型_max)
print("HADS_中等型_min", HADS_中等型_min)
print("HADS_中等型_mean", HADS_中等型_mean)

print("===============================")

CBTS_安静型_max = selected_1['CBTS'].max()
CBTS_安静型_min = selected_1['CBTS'].min()
CBTS_安静型_mean = selected_1['CBTS'].mean()

EPDS_安静型_max = selected_1['EPDS'].max()
EPDS_安静型_min = selected_1['EPDS'].min()
EPDS_安静型_mean = selected_1['EPDS'].mean()

HADS_安静型_max = selected_1['HADS'].max()
HADS_安静型_min = selected_1['HADS'].min()
HADS_安静型_mean = selected_1['HADS'].mean()

print("CBTS_安静型_max", CBTS_安静型_max)
print("CBTS_安静型_min", CBTS_安静型_min)
print("CBTS_安静型_mean", CBTS_安静型_mean)
print("EPDS_安静型_max", EPDS_安静型_max)
print("EPDS_安静型_min", EPDS_安静型_min)
print("EPDS_安静型_mean", EPDS_安静型_mean)
print("HADS_安静型_max", HADS_安静型_max)
print("HADS_安静型_min", HADS_安静型_min)
print("HADS_安静型_mean", HADS_安静型_mean)
print("===============================")

CBTS_矛盾型_max = selected_2['CBTS'].max()
CBTS_矛盾型_min = selected_2['CBTS'].min()
CBTS_矛盾型_mean = selected_2['CBTS'].mean()

EPDS_矛盾型_max = selected_2['EPDS'].max()
EPDS_矛盾型_min = selected_2['EPDS'].min()
EPDS_矛盾型_mean = selected_2['EPDS'].mean()

HADS_矛盾型_max = selected_2['HADS'].max()
HADS_矛盾型_min = selected_2['HADS'].min()
HADS_矛盾型_mean = selected_2['HADS'].mean()

print("CBTS_矛盾型_max", CBTS_矛盾型_max)
print("CBTS_矛盾型_min", CBTS_矛盾型_min)
print("CBTS_矛盾型_mean", CBTS_矛盾型_mean)
print("EPDS_矛盾型_max", EPDS_矛盾型_max)
print("EPDS_矛盾型_min", EPDS_矛盾型_min)
print("EPDS_矛盾型_mean", EPDS_矛盾型_mean)
print("HADS_矛盾型_max", HADS_矛盾型_max)
print("HADS_矛盾型_min", HADS_矛盾型_min)
print("HADS_矛盾型_mean", HADS_矛盾型_mean)

print("===============================")
print("CBTS_中等型_mean", CBTS_中等型_mean)
print("CBTS_安静型_mean", CBTS_安静型_mean)
print("CBTS_矛盾型_mean", CBTS_矛盾型_mean)
print("===============================")
print("EPDS_中等型_mean", EPDS_中等型_mean)
print("EPDS_安静型_mean", EPDS_安静型_mean)
print("EPDS_矛盾型_mean", EPDS_矛盾型_mean)

print("===============================")
print("HADS_中等型_mean", HADS_中等型_mean)
print("HADS_安静型_mean", HADS_安静型_mean)
print("HADS_矛盾型_mean", HADS_矛盾型_mean)
