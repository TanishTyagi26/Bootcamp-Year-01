import pandas as pd
import numpy as np

rows = 100000

data = {
    "Timestamp": pd.date_range(
        start="2020-01-01",
        periods=rows,
        freq="h"
    ),

    "Country": np.random.choice(
        ["India","USA","UK"],
        rows
    ),

    "State": np.random.choice(
        ["Haryana","Texas","London"],
        rows
    ),

    "Temperature": np.random.normal(
        25,
        5,
        rows
    ),

    "Latitude": np.random.uniform(
        -90,
        90,
        rows
    ),

    "Longitude": np.random.uniform(
        -180,
        180,
        rows
    ),

    "QualityFlag": np.random.choice(
        ["Good","Bad"],
        rows,
        p=[0.95,0.05]
    )
}


df = pd.DataFrame(data)


# Add artificial bad values
df.loc[
    np.random.choice(df.index,100),
    "Temperature"
] = 999


df.to_csv(
    "climate_data.csv",
    index=False
)