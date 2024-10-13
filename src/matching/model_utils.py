import numpy as np
import pandas as pd


def featurize(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df
        .assign(
            name_product_normalized = lambda df: df["name_offer"].str.lower(),
            name_offer_normalized = lambda df: df["name_product"].str.lower(),
        )
    )

def predict(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df
        .assign(
            similarity = lambda df: np.random.rand(len(df))
        )
    )

def postprocess(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df
        .assign(
            is_match = lambda df: df["similarity"] > 0.5
        )
    )