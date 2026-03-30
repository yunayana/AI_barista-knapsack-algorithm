import streamlit as st
import pandas as pd
from coffee_knapsack import BaristaKnapsackHS

st.title("AI Barista - Coffee Bean Selection Optimizer")

st.sidebar.header("Parameters")
max_weight = st.sidebar.slider("Max Weight (g)", 100, 500, 250)
max_budget = st.sidebar.slider("Max Budget (zł)", 10, 100, 40)
iterations = st.sidebar.slider("Iterations", 1000, 20000, 10000)
hms = st.sidebar.slider("Harmony Memory Size", 5, 20, 10)
hmcr = st.sidebar.slider("HMCR", 0.5, 0.9, 0.7)
par = st.sidebar.slider("PAR", 0.1, 0.5, 0.3)
mutation_rate = st.sidebar.slider("Mutation Rate", 0.01, 0.1, 0.02)

if st.sidebar.button("Run Optimization"):
    with st.spinner("Optimizing..."):
        problem = BaristaKnapsackHS(
            "coffee_beans.csv",
            max_weight=max_weight,
            max_budget=max_budget,
            hms=hms,
            hmcr=hmcr,
            par=par,
            mutation_rate=mutation_rate
        )

        result = problem.solve(iterations)

    if result:
        st.success("Optimization Complete!")

        # Display results
        st.header("Selected Coffee Beans")
        selected_beans = []
        total_weight = 0
        total_price = 0
        total_sensory = 0

        for i, selected in enumerate(result['sol']):
            if selected:
                bean = problem.beans[i]
                selected_beans.append({
                    'Name': bean.name,
                    'Weight (g)': bean.weight,
                    'Price (zł)': bean.price,
                    'Sensory Score': bean.sensory_score
                })
                total_weight += bean.weight
                total_price += bean.price
                total_sensory += bean.sensory_score

        df_selected = pd.DataFrame(selected_beans)
        st.dataframe(df_selected)

        st.subheader("Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Weight", f"{total_weight:.1f} g")
        with col2:
            st.metric("Total Price", f"{total_price:.1f} zł")
        with col3:
            st.metric("Total Sensory Score", f"{total_sensory:.1f}")

        st.write(f"Best Fitness: {result['fit']:.1f}")
        st.write(f"Total Mutations: {result.get('mutations', 0)}")
    else:
        st.error("No solution found. Check parameters or data.")

# Display available beans
st.header("Available Coffee Beans")
try:
    df_beans = pd.read_csv("coffee_beans.csv")
    st.dataframe(df_beans)
except Exception as e:
    st.error(f"Error loading CSV: {e}")