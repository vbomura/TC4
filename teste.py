import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title = "Painel de Ações da B3",
    layout="wide"
)

st.header("**Painel de preço de fechamento e dividendos de ações B3**")

ticker= st.text_input("Digite o ticker/sigla da ação:", "PETR4")
empresa=yf.Ticker(f"{ticker}.SA")

tickerDF = empresa.history(
                             start ="2019-01-01", 
                             end = "2025-09-30")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write(f"**Empresa:** {empresa.info['longName']}")
with col2:
    st.write(f"**Mercado:** {empresa.info['industry']}")
with col3:
    st.write(f"**Preço Atual:** {empresa.info['currentPrice']}")

st.line_chart(tickerDF.Close)
st.bar_chart(tickerDF.Dividends)