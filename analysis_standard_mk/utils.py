from typing import List
import pandas as pd
from dython.nominal import identify_nominal_columns


def identify_limited_categorical(df: pd.DataFrame, category_limit: int = 30) -> List[str]:
    nominal_columns = identify_nominal_columns(df)
    limited_columns = [column for column in nominal_columns if len(df[column].unique()) <= category_limit]
    return limited_columns


def identify_overlimited_categorical(df: pd.DataFrame, category_limit: int = 30) -> List[str]:
    nominal_columns = identify_nominal_columns(df)
    overlimited_columns = [column for column in nominal_columns if len(df[column].unique()) > category_limit]
    return overlimited_columns


def transform_categorical_from_numerical(df, category_limit=10, numerical_types=['int64']):
    numerical_cols = df.select_dtypes(include=numerical_types).columns.tolist()
    numerical_cols = [col for col in numerical_cols if len(df[col].unique()) < category_limit]
    df[numerical_cols] = df[numerical_cols].astype('category')
    return df
