import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データ読み込み
sales_df = pd.read_csv("data/processed/sales.csv")

# 成約率計算
sales_df["success_rate"] = sales_df["num_successes"] / sales_df["num_negotiations"]

# サイドバーで営業選択
selected_sales = st.sidebar.selectbox("営業を選択", sales_df["name"].unique())

# フィルタ処理
filtered = sales_df[sales_df["name"] == selected_sales]

# タイトル
st.title("営業別KPIサマリー")

# 数値表示
st.metric(label="アポ数", value=int(filtered["num_appointments"]))
st.metric(label="商談数", value=int(filtered["num_negotiations"]))
st.metric(label="成約数", value=int(filtered["num_successes"]))
st.metric(label="成約率", value=f'{filtered["success_rate"].values[0]*100:.1f}%')

# グラフ：全営業の成約率比較
st.subheader("全営業の成約率比較")
fig, ax = plt.subplots()
ax.bar(sales_df["name"], sales_df["success_rate"])
ax.set_ylabel("成約率")
ax.set_ylim(0, 1)
st.pyplot(fig)
