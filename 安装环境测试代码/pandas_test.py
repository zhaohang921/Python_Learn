# encoding=utf-8
import numpy as np
import pandas as pd


def main():
    # Data Structure
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(type(s))
    dates = pd.date_range("20180208", periods=8)
    df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
    print(df)
    # df = pd.DataFrame({"A": 1, "B": pd.Timestamp("20180208"), "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    #                    "D": np.array([3] * 4, dtype="float32"),
    #                    "E": pd.Categorical(["police", "student", "teacher", "doctor"])})
    # print(df)

    # 基本操作
    print(df.head(3))
    print(df.tail(3))
    print(df.index)
    print(df.values)
    print(df.T)
    # print(df.sort(columns="C"))
    print(df.sort_index(axis=1, ascending=False))
    print(df.describe())
    # 选择，切片
    print(type(df["A"]))
    print(df[:3])
    print(df["20180208":"20180211"])
    print(df.loc[dates[0]])
    print(df.loc["20180208":"20180211", ["B", "D"]])
    print(df.at[dates[0], "C"])

    print(df.iloc[1:3, 2:4])
    print(df.iloc[1, 4])
    print(df.iat[1, 4])

    print(df[df.B > 0][df.A < 0])
    print(df[df > 0])
    print(df[df["E"].isin([1, 2])])



if __name__ == "__main__":
        main()
