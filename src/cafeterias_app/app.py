import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración visual
st.set_page_config(page_title="Dashboard Cafetería", page_icon="☕", layout="wide")

st.title("☕ Análisis Inteligente de la Cafetería")
st.markdown("---")

# --- SIMULACIÓN DE DATOS (Cámbialos por los tuyos luego) ---
datos = {
    'Producto': ['Espresso', 'Latte', 'Capuccino', 'Muffin', 'Croissant', 'Té Verde'],
    'Ventas_Unidades': [150, 280, 210, 85, 130, 45],
    'Precio_Unitario': [2.5, 3.5, 3.8, 2.0, 2.5, 2.2],
    'Categoria': ['Café', 'Café', 'Café', 'Comida', 'Comida', 'Bebida']
}
df = pd.DataFrame(datos)
df['Ingresos'] = df['Ventas_Unidades'] * df['Precio_Unitario']

# --- MÉTRICAS PRINCIPALES ---
col1, col2, col3 = st.columns(3)
col1.metric("Ingresos Totales", f"${df['Ingresos'].sum():,.2f}")
col2.metric("Producto más vendido", df.loc[df['Ventas_Unidades'].idxmax(), 'Producto'])
col3.metric("Ticket Promedio", f"${df['Ingresos'].mean():,.2f}")

st.markdown("---")

# --- GRÁFICAS ---
c1, c2 = st.columns(2)

with c1:
    st.subheader("Ventas por Producto")
    fig_bar = px.bar(df, x='Producto', y='Ventas_Unidades', color='Categoria', 
                     text_auto=True, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    st.subheader("Distribución de Ingresos")
    fig_pie = px.pie(df, values='Ingresos', names='Producto', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- TABLA DE DATOS ---
with st.expander("Ver detalle de la tabla de datos"):
    st.dataframe(df, use_container_width=True)



