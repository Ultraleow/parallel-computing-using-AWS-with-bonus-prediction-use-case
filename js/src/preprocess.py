#!/usr/bin/env python3
import pandas as pd
import numpy as np
import sys
import time
import sys
import os



mapping_path = "/home/ubuntu/src/mapping.xlsx"
def convert_company_to_numeric(dspay_labelled):
    dic = pd.read_excel(mapping_path, sheet_name="company", index_col=0).to_dict()[0]
    dic[pd.read_excel(mapping_path, sheet_name="company").columns[0]] = 0
    dspay_labelled['company'] = dspay_labelled['company'].map(dic).fillna(89)
    return dspay_labelled


def convert_title_to_numeric(dspay_labelled):
    dic = pd.read_excel(mapping_path, sheet_name="title", index_col=0).to_dict()[0]
    dic[pd.read_excel(mapping_path, sheet_name="title").columns[0]] = 0
    dspay_labelled['title'] = dspay_labelled['title'].map(dic)
    return dspay_labelled


def convert_gender_to_numeric(dspay_labelled):
    dic = pd.read_excel(mapping_path, sheet_name="gender", index_col=0).to_dict()[0]
    dic[pd.read_excel(mapping_path, sheet_name="gender").columns[0]] = 0
    dspay_labelled['gender'] = dspay_labelled['gender'].map(dic)
    return dspay_labelled


def convert_race_to_numeric(dspay_labelled):
    dic = pd.read_excel(mapping_path, sheet_name="Race", index_col=0).to_dict()[0]
    dic[pd.read_excel(mapping_path, sheet_name="Race").columns[0]] = 0
    dspay_labelled['Race'] = dspay_labelled['Race'].map(dic)
    return dspay_labelled


def convert_education_to_numeric(dspay_labelled):
    dic = pd.read_excel(mapping_path, sheet_name="Education", index_col=0).to_dict()[0]
    dic[pd.read_excel(mapping_path, sheet_name="Education").columns[0]] = 0
    dspay_labelled['Education'] = dspay_labelled['Education'].map(dic)
    return dspay_labelled


def convert_state_to_numeric(dspay_labelled):
    dic = pd.read_excel(mapping_path, sheet_name="state", index_col=0).to_dict()[0]
    dic[pd.read_excel(mapping_path, sheet_name="state").columns[0]] = 0
    dspay_labelled['state'] = dspay_labelled['state'].map(dic)
    return dspay_labelled


def convert_country_to_numeric(dspay_labelled):
    dic = pd.read_excel(mapping_path, sheet_name="country", index_col=0).to_dict()[0]
    dic[pd.read_excel(mapping_path, sheet_name="country").columns[0]] = 0
    dspay_labelled['country'] = dspay_labelled['country'].map(dic)
    return dspay_labelled


def convert_all_value(dataframe):
    df = dataframe
    df = convert_company_to_numeric(df)
    df = convert_title_to_numeric(df)
    df = convert_gender_to_numeric(df)
    df = convert_race_to_numeric(df)
    df = convert_education_to_numeric(df)
    df = convert_state_to_numeric(df)
    df = convert_country_to_numeric(df)
    return df