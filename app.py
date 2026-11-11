import streamlit as st

st.set_page_config(
    page_title="FarmaCalc Educacional",
    page_icon="⚗️",
    layout="centered"
)

st.title(" FarmaCalc Educacional ")
st.caption("Simulador didático de cálculos de princípios ativos")

st.info(
    "Atividade educacional com fórmulas fictícias. "
    "O simulador calcula apenas a massa teórica dos princípios ativos."
)

st.header("1. Dados da fórmula")
capsulas = st.number_input(
    "Quantidade de cápsulas",
    min_value=1,
    max_value=10000,
    value=30,
    step=1
)

st.header("2. Princípios ativos")

nome_a = st.text_input("Nome do princípio ativo 1", "Princípio ativo A")
dose_a = st.number_input(
    "Dosagem do ativo 1 por cápsula (mg)",
    min_value=0.01,
    max_value=1000000.0,
    value=100.0,
    step=1.0
)

incluir_b = st.checkbox("Adicionar segundo princípio ativo", value=True)

if incluir_b:
    nome_b = st.text_input("Nome do princípio ativo 2", "Princípio ativo B")
    dose_b = st.number_input(
        "Dosagem do ativo 2 por cápsula (mg)",
        min_value=0.01,
        max_value=1000000.0,
        value=50.0,
        step=1.0
    )
else:
    nome_b = ""
    dose_b = 0.0

if st.button("Calcular fórmula", type="primary", use_container_width=True):
    total_a_mg = dose_a * capsulas
    total_b_mg = dose_b * capsulas if incluir_b else 0.0
    total_mg = total_a_mg + total_b_mg

    st.header("3. Resultado do cálculo")
    st.subheader("Memória de cálculo")

    st.write(f"**{nome_a or 'Princípio ativo 1'}**")
    st.latex(
        rf"{dose_a:g}\ mg \times {capsulas} = {total_a_mg:,.2f}\ mg"
        .replace(",", r"{,}")
    )
    st.success(f"Quantidade total: {total_a_mg / 1000:.4f} g")

    if incluir_b:
        st.write(f"**{nome_b or 'Princípio ativo 2'}**")
        st.latex(
            rf"{dose_b:g}\ mg \times {capsulas} = {total_b_mg:,.2f}\ mg"
            .replace(",", r"{,}")
        )
        st.success(f"Quantidade total: {total_b_mg / 1000:.4f} g")

    st.divider()
    st.metric("Massa total dos princípios ativos", f"{total_mg / 1000:.4f} g")
    st.caption(f"Equivalente a {total_mg:,.2f} mg no total.")

    resumo = (
        f"Para {capsulas} cápsulas, são necessários "
        f"{total_a_mg / 1000:.4f} g de {nome_a or 'ativo 1'}"
    )
    if incluir_b:
        resumo += (
            f" e {total_b_mg / 1000:.4f} g de "
            f"{nome_b or 'ativo 2'}"
        )
    st.write(resumo + ".")

st.divider()
st.header("4. Fórmulas utilizadas")
st.latex(r"Q_{total}(mg) = D(mg) \\times N")
st.latex(r"Q_{total}(g) = \\frac{Q_{total}(mg)}{1000}")

with st.expander("Entenda as variáveis"):
    st.write("- **Q total:** quantidade total do princípio ativo.")
    st.write("- **D:** dosagem por cápsula, em miligramas.")
    st.write("- **N:** número de cápsulas.")

st.warning(
    "Este protótipo não calcula excipientes, fator de correção, "
    "fator de equivalência, teor, umidade ou perdas de processo. "
    "Não deve ser utilizado como prescrição, ordem de produção ou "
    "substituto da avaliação e conferência do farmacêutico."
)

st.caption("FarmaCalc Educacional • Versão didática- 1.0-Curso Técnico em Farmácia Etec Edson Galvão")
