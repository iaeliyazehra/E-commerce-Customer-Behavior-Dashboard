import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Behavior Dashboard", layout="wide")
st.title("E-commerce Customer Behavior Dashboard")
st.write("This dashboard analyzes customer behavior and purchasing patterns.")
BLUE = "#2a6fdb"


@st.cache_data
def load_data():
    return pd.read_csv("ecommerce_customers.csv")

df = load_data()



# ---------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------

st.sidebar.header("Filters")

membership = st.sidebar.slider("Membership Length", 0.0, 7.0, (0.0, 7.0))
filtered_df = df[
    (df["Length of Membership"] >= membership[0]) &
    (df["Length of Membership"] <= membership[1])
]

spending = st.sidebar.slider("Yearly Spending", 0.0, 1000.0, (0.0, 1000.0))
filtered_df = filtered_df[
    (filtered_df["Yearly Amount Spent"] >= spending[0]) &
    (filtered_df["Yearly Amount Spent"] <= spending[1])
]

# ---------------------------------------------------------------
# Matrics
# ---------------------------------------------------------------

st.divider()
total_customers = len(filtered_df)
average_spending = round(filtered_df["Yearly Amount Spent"].mean(), 2)
average_membership = round(filtered_df["Length of Membership"].mean(), 2)
highest_spending = round(filtered_df["Yearly Amount Spent"].max(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", total_customers)

with col2:
    st.metric("Average Spending", average_spending)

with col3:
    st.metric("Average Membership", average_membership)

with col4:
    st.metric("Highest Spending", highest_spending)

# ---------------------------------------------------------------
# 5 graphs
# ---------------------------------------------------------------


# Row 1
st.write("")
st.write("")
st.write("")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("**Yearly Spending Distribution**")
    plt.figure(figsize=(4, 2))
    plt.hist(filtered_df["Yearly Amount Spent"], bins=20, edgecolor="black")
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    st.pyplot(plt)
    plt.close()

with col2:
    st.markdown("**Membership vs Yearly Spending**")
    plt.figure(figsize=(4, 2))
    plt.scatter(filtered_df["Length of Membership"], filtered_df["Yearly Amount Spent"])
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    st.pyplot(plt)
    plt.close()

st.write("")
st.write("")


# Row 2
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("**Time on App vs Yearly Spending**")
    plt.figure(figsize=(4, 2))
    plt.scatter(filtered_df["Time on App"], filtered_df["Yearly Amount Spent"])
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    st.pyplot(plt)
    plt.close()

with col2:
    st.markdown("**Time on Website vs Yearly Spending**")
    plt.figure(figsize=(4, 2))
    plt.scatter(filtered_df["Time on Website"], filtered_df["Yearly Amount Spent"])
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    st.pyplot(plt)
    plt.close()


st.write("")
st.write("")


# Row 3
st.markdown("**Correlation Heatmap**")

plt.figure(figsize=(3, 2))
sns.heatmap(filtered_df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm", annot_kws={"size": 5})
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.tight_layout()
st.pyplot(plt)
plt.close()


st.divider()

show_data = st.checkbox("Show Raw Data")

if show_data:
    st.dataframe(filtered_df)

st.divider()

st.subheader("Main Findings")

st.write("Customers with longer memberships generally spend more.")

st.write("Time spent on the app has a positive relationship with yearly spending.")

st.write("Time spent on the website has almost no relationship with yearly spending.")

st.write("Length of Membership has the strongest relationship with yearly spending.")