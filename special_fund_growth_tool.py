import streamlit as st
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Investment Growth Comparison", layout="centered")

# Title
st.title("📈 MMF vs Special Fund: Investment Growth Over Time")
st.markdown("""
Enter your investment amount and timeline below to compare how a Money Market Fund (MMF) and a Special Fund might grow over time.

- **MMF**: Assumes 7% annual return
- **Special Fund**: Assumes 17% annual return
""")

# Input fields
initial_investment = st.number_input("Initial Investment Amount (KES)", min_value=1000, value=250000, step=1000)
years = st.slider("Investment Duration (Years)", min_value=1, max_value=10, value=5)

# Constants
mmf_rate = 0.07
special_rate = 0.17
years_range = list(range(years + 1))

# Calculate compound returns
mmf_values = [initial_investment * ((1 + mmf_rate) ** yr) for yr in years_range]
special_values = [initial_investment * ((1 + special_rate) ** yr) for yr in years_range]

# Plotting
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(years_range, mmf_values, marker='o', label='MMF (7% p.a)', color='green')
ax.plot(years_range, special_values, marker='o', label='Special Fund (17% p.a)', color='red')

# Annotate values
for i in range(len(years_range)):
    ax.annotate(f"{int(mmf_values[i]):,}", (years_range[i], mmf_values[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='green')
    ax.annotate(f"{int(special_values[i]):,}", (years_range[i], special_values[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

ax.set_title("Projected Investment Growth")
ax.set_xlabel("Years")
ax.set_ylabel("Value (KES)")
ax.grid(True)
ax.legend()

st.pyplot(fig)

# Summary
st.markdown("""
### 💡 Summary
- **MMF Final Value**: KES {:,.0f}  
- **Special Fund Final Value**: KES {:,.0f}

This tool is for educational purposes only and does not constitute financial advice.
""".format(mmf_values[-1], special_values[-1]))
