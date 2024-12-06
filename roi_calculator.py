import streamlit as st

# ROI Calculator App
st.title("Customer ROI Calculator")

# Input: Downtime
st.header("Downtime Costs")
downtime_hours = st.number_input("Downtime Hours (per month)", min_value=0.0, value=10.0)
hourly_revenue_loss = st.number_input("Revenue Lost per Hour ($)", min_value=0.0, value=100.0)
downtime_cost = downtime_hours * hourly_revenue_loss

# Input: Labor Costs
st.header("Labor Cost Savings")
num_employees = st.number_input("Number of Employees", min_value=1, value=5)
hourly_wage = st.number_input("Average Hourly Wage ($)", min_value=0.0, value=20.0)
hours_saved = st.number_input("Labor Hours Saved per Month", min_value=0.0, value=50.0)
labor_savings = hours_saved * hourly_wage * num_employees

# Input: Volume Efficiency
st.header("Volume Efficiency Savings")
current_volume = st.number_input("Current Units Processed per Hour", min_value=1, value=100)
current_cost_per_unit = st.number_input("Current Cost per Unit ($)", min_value=0.0, value=0.50)
efficiency_gain_percent = st.number_input("Efficiency Gain (%)", min_value=0.0, max_value=100.0, value=20.0)
new_cost_per_unit = current_cost_per_unit * (1 - efficiency_gain_percent / 100)
volume_savings = current_volume * (current_cost_per_unit - new_cost_per_unit) * 8 * 30  # Assuming 8-hour shifts, 30 days

# Total ROI
st.header("Total ROI")
total_savings = downtime_cost + labor_savings + volume_savings
st.write(f"**Downtime Savings:** ${downtime_cost:,.2f}")
st.write(f"**Labor Cost Savings:** ${labor_savings:,.2f}")
st.write(f"**Volume Efficiency Savings:** ${volume_savings:,.2f}")
st.write(f"### Total Monthly ROI: ${total_savings:,.2f}")

# Optional: Payback Period
machine_cost = st.number_input("Machine Cost ($)", min_value=0.0, value=55000.0)
if machine_cost > 0 and total_savings > 0:
    payback_period = machine_cost / total_savings
    st.write(f"### Estimated Payback Period: {payback_period:.2f} months")
else:
    st.write("### Provide machine cost and ensure ROI is positive for payback calculation.")
