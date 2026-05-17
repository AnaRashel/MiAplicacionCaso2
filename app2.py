import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# PRINCIPAL
# Interfaz de Streamlit
# Selección de página
st.sidebar.image("logo.png")
pagina = st.sidebar.selectbox("Selecciona una página:", ["🏠 Home", "📋 Carga del dataset"])

#Selección Home
if pagina == "🏠 Home":
    # HOME - PRESENTACIÓN DEL PROYECTO
    # CONFIGURACIÓN DE PÁGINA
    # ======================================================

    st.set_page_config(
        page_title="Telco Customer Churn",
        page_icon="📊",
        layout="wide"
    )

    # ======================================================
    # ESTILOS
    # ======================================================

    st.markdown("""
    <style>

    .main {
        background-color: #F5F7FA;
    }

    .titulo {
        text-align: center;
        color: #0E1117;
        font-size: 72px !important;
        font-weight: 900 !important;
        margin-bottom: 10px;
    }

    .subtitulo {
        text-align: center;
        color: #555;
        font-size: 24px;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ======================================================
    # TÍTULO
    # ======================================================

    st.markdown("""
    <h1 class="titulo">
    📊 TELCO CUSTOMER CHURN - EDA
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="subtitulo">
    Análisis Exploratorio de Datos utilizando Python y Streamlit
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    # ======================================================
    # OBJETIVO DEL PROYECTO
    # ======================================================

    st.markdown("## 🎯 Objetivo del Proyecto")

    st.markdown("""
    <div class="card">

    El objetivo del presente proyecto es desarrollar un análisis exploratorio
    de datos (EDA) sobre un dataset de clientes de telecomunicaciones,
    con la finalidad de identificar patrones relacionados con la fuga de clientes
    (Customer Churn).

    A través de técnicas de limpieza, transformación, visualización y análisis
    estadístico, se busca comprender el comportamiento de los clientes
    y detectar variables relevantes asociadas al abandono del servicio.

    </div>
    """, unsafe_allow_html=True)

    # ======================================================
    # DATOS DEL AUTOR
    # ======================================================

    st.markdown("## 👩‍💻 Datos del Autor")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">

        ### 👤 Nombre
        
        Ana Fernanda Rashel Fernández Pamucena

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        ### 🎓 Curso
        
        Especialización en Python

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card">

        ### 📅 Año
        
        2026

        </div>
        """, unsafe_allow_html=True)

    # ======================================================
    # DATASET
    # ======================================================

    st.markdown("## 📂 Descripción del Dataset")

    st.markdown("""
    <div class="card">

    El dataset Telco Customer Churn contiene información sobre clientes
    de una empresa de telecomunicaciones, incluyendo características
    demográficas, servicios contratados, métodos de pago,
    facturación y estado de abandono del servicio.

    Entre las principales variables se encuentran:

    - Género
    - Tipo de contrato
    - Tiempo de permanencia (tenure)
    - Cargos mensuales
    - Servicio de internet
    - Método de pago
    - Variable objetivo Churn

    El análisis permitirá identificar patrones de comportamiento
    y factores asociados a la fuga de clientes.

    </div>
    """, unsafe_allow_html=True)

    # ======================================================
    # TECNOLOGÍAS
    # ======================================================

    st.markdown("## 🛠️ Tecnologías Utilizadas")

    tec1, tec2, tec3, tec4, tec5 = st.columns(5)

    with tec1:
        st.success("🐍 Python")

    with tec2:
        st.success("📊 Pandas")

    with tec3:
        st.success("🎨 Streamlit")

    with tec4:
        st.success("📈 Matplotlib")

    with tec5:
        st.success("🔥 Seaborn")

    # ======================================================
    # FOOTER
    # ======================================================

    st.divider()

    st.caption("""
    Proyecto académico desarrollado para el curso de Especialización en Python
    """)
    # Pie de página
    st.markdown("---")
    st.write("© 2026 - Proyecto Académico")

#Selección Carga del dataset
elif pagina == "📋 Carga del dataset":
    # Inicializar en sesión
    # CONFIGURACIÓN
    st.set_page_config(
        page_title="EDA Telco Customer Churn",
        page_icon="📊",
        layout="wide"
    )

    sns.set_style("whitegrid")

    # ESTILOS
    # ======================================================
    st.markdown("""
    <style>

    .main {
        background-color: #F5F7FA;
    }

    .titulo {
        text-align: center;
        color: #0E1117;
        font-size: 70px !important;
        font-weight: 900 !important;
        margin-bottom: 10px;
    }

    .subtitulo {
        text-align: center;
        font-size: 24px;
        color: #555;
        margin-bottom: 30px;
    }

    </style>
    """, unsafe_allow_html=True)


    # TÍTULO
    # ======================================================
    st.markdown("""
    <h1 class="titulo">
    📊 TELCO CUSTOMER CHURN - EDA
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="subtitulo">
    Análisis Exploratorio de Datos utilizando Python + Streamlit
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    # CLASE POO
    # ======================================================
    class DataAnalyzer:

        def __init__(self, df):
            self.df = df

        # Clasificación variables
        def clasificar_variables(self):

            numericas = self.df.select_dtypes(
                include=np.number
            ).columns.tolist()

            categoricas = self.df.select_dtypes(
                include=['object']
            ).columns.tolist()

            return numericas, categoricas

        # Estadísticas
        def estadisticas(self):
            return self.df.describe().T

        # Valores nulos
        def valores_nulos(self):
            return self.df.isnull().sum()

        # Información dataset
        def info_dataset(self):

            info = pd.DataFrame({
                'Tipo de dato': self.df.dtypes,
                'Valores nulos': self.df.isnull().sum(),
                'Valores únicos': self.df.nunique()
            })

            return info

        # Moda
        def moda(self, columna):
            return self.df[columna].mode()[0]

    # SIDEBAR
    # ======================================================

    st.sidebar.title("⚙️ Panel de Control")

    mostrar_dataset = st.sidebar.checkbox(
        "Mostrar dataset completo"
    )

    mostrar_correlacion = st.sidebar.checkbox(
        "Mostrar matriz de correlación"
    )

    bins = st.sidebar.slider(
        "Número de bins",
        min_value=5,
        max_value=50,
        value=2
    )

    # CARGA DATASET
    # ======================================================
    st.header("📂 Carga del Dataset")

    archivo = st.file_uploader(
        "Suba el archivo TelcoCustomerChurn.csv",
        type=['csv']
    )

    # ======================================================
    # VALIDACIÓN
    # ======================================================

    if archivo is not None:

        df = pd.read_csv(archivo)
        # LIMPIEZA Y PREPARACIÓN
        # ==========================================

        st.header("🧹 Limpieza y Preparación de Datos")

        df_clean = df.copy()

        # ELIMINAR ESPACIOS
        columnas_texto = df_clean.select_dtypes(
            include=['object']
        ).columns

        for col in columnas_texto:

            df_clean[col] = (
                df_clean[col]
                .astype(str)
                .str.strip()
            )

        # CONVERTIR TOTALCHARGES
        df_clean['TotalCharges'] = pd.to_numeric(
            df_clean['TotalCharges'],
            errors='coerce'
        )

        # REEMPLAZAR VACÍOS
        df_clean.replace(
            ['', ' ', 'NA', 'NaN'],
            np.nan,
            inplace=True
        )

        # DUPLICADOS
        duplicados = df_clean.duplicated().sum()

        df_clean.drop_duplicates(inplace=True)

        # NULOS NUMÉRICOS
        numericas_temp = df_clean.select_dtypes(
            include=np.number
        ).columns

        for col in numericas_temp:

            df_clean[col].fillna(
                df_clean[col].median(),
                inplace=True
            )

        # NULOS CATEGÓRICOS
        categoricas_temp = df_clean.select_dtypes(
            include=['object']
        ).columns

        for col in categoricas_temp:

            df_clean[col].fillna(
                df_clean[col].mode()[0],
                inplace=True
            )

        # UNIFORMIZAR TEXTO
        for col in categoricas_temp:

            df_clean[col] = (
                df_clean[col]
                .str.lower()
                .str.strip()
            )

        # RENOMBRAR COLUMNAS
        df_clean.columns = (
            df_clean.columns
            .str.strip()
            .str.replace(" ", "_")
        )

        # REEMPLAZAR DATASET
        df = df_clean.copy()

        st.success("✅ Dataset limpiado correctamente")

        # ======================================================
        # VISTA PREVIA
        # ======================================================

        st.subheader("👀 Vista previa del dataset")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        # ======================================================
        # DIMENSIONES
        # ======================================================

        filas, columnas = df.shape

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Filas", filas)

        with c2:
            st.metric("Columnas", columnas)

        with c3:
            st.metric(
                "Valores Nulos",
                int(df.isnull().sum().sum())
            )

        if mostrar_dataset:

            st.subheader("📄 Dataset completo")

            st.dataframe(
                df,
                use_container_width=True
            )

        # OBJETO POO
        # ======================================================

        analyzer = DataAnalyzer(df)

        numericas, categoricas = analyzer.clasificar_variables()

        # ======================================================
        # TABS
        # ======================================================

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs([
            "📌 Información",
            "📌 Variables",
            "📌 Estadísticas",
            "📌 Valores Nulos",
            "📌 Distribuciones",
            "📌 Categóricas",
            "📌 Num vs Cat",
            "📌 Cat vs Cat",
            "📌 Dinámico",
            "📌 Insights",
            "📌 Conclusión"
        ])

        # TAB 1
        # ======================================================

        with tab1:

            st.header("📌 Información General")

            st.dataframe(
                analyzer.info_dataset(),
                use_container_width=True
            )

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("Tipos de Datos")

                tipos = pd.DataFrame(
                    df.dtypes,
                    columns=['Tipo']
                )

                st.dataframe(
                    tipos,
                    use_container_width=True
                )

            with col2:

                st.subheader("Valores Nulos")

                nulos = pd.DataFrame(
                    df.isnull().sum(),
                    columns=['Nulos']
                )

                st.dataframe(
                    nulos,
                    use_container_width=True
                )

        # ======================================================
        # TAB 2
        # ======================================================

        with tab2:

            st.header("📌 Clasificación de Variables")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("🔢 Variables Numéricas")

                st.metric(
                    "Cantidad",
                    len(numericas)
                )

                num_df = pd.DataFrame({
                    "Variables Numéricas": numericas
                })

                st.dataframe(
                    num_df,
                    use_container_width=True,
                    height=400
                )

            with col2:

                st.subheader("🔤 Variables Categóricas")

                st.metric(
                    "Cantidad",
                    len(categoricas)
                )

                cat_df = pd.DataFrame({
                    "Variables Categóricas": categoricas
                })

                st.dataframe(
                    cat_df,
                    use_container_width=True,
                    height=400
                )

        # TAB 3
        # ======================================================

        with tab3:

            st.header("📌 Estadísticas Descriptivas")

            st.dataframe(
                analyzer.estadisticas(),
                use_container_width=True
            )

            variable = st.selectbox(
                "Seleccione variable numérica",
                numericas
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Media",
                    round(df[variable].mean(), 2)
                )

            with col2:

                st.metric(
                    "Mediana",
                    round(df[variable].median(), 2)
                )

            with col3:

                st.metric(
                    "Desv. Std",
                    round(df[variable].std(), 2)
                )

        # ======================================================
        # TAB 4
        # ======================================================

        with tab4:

            st.header("📌 Valores Faltantes")

            nulos = df.isnull().sum()

            col1, col2 = st.columns([1,2])

            with col1:

                st.dataframe(
                    pd.DataFrame(
                        nulos,
                        columns=['Nulos']
                    ),
                    use_container_width=True
                )

            with col2:

                fig, ax = plt.subplots(figsize=(10,4))

                nulos.plot(
                    kind='bar',
                    ax=ax
                )

                plt.xticks(rotation=45)

                plt.title(
                    "Valores Faltantes"
                )

                st.pyplot(fig)

            st.info("""
            Los valores faltantes pueden afectar
            la calidad del análisis y deben ser tratados.
            """)

        # TAB 5
        # ======================================================

        with tab5:

            st.header("📌 Distribución Variables Numéricas")

            variable_num = st.selectbox(
                "Seleccione variable",
                numericas,
                key='hist'
            )

            fig, ax = plt.subplots(figsize=(10,5))

            sns.histplot(
                data=df,
                x=variable_num,
                bins=bins,
                kde=True,
                ax=ax
            )

            plt.title(
                f"Distribución de {variable_num}"
            )

            st.pyplot(fig)

            st.write("""
            El histograma permite visualizar
            la distribución y concentración
            de los datos.
            """)

        # ======================================================
        # TAB 6
        # ======================================================

        with tab6:

            st.header("📌 Variables Categóricas")

            variable_cat = st.selectbox(
                "Seleccione variable categórica",
                categoricas,
                key='cat'
            )

            conteo = df[variable_cat].value_counts()

            col1, col2 = st.columns([1,2])

            with col1:

                st.subheader("Conteos")

                st.dataframe(
                    conteo,
                    use_container_width=True
                )

                proporciones = (
                    conteo / len(df) * 100
                ).round(2)

                st.subheader("Proporciones (%)")

                st.dataframe(
                    proporciones,
                    use_container_width=True
                )

            with col2:

                fig, ax = plt.subplots(figsize=(10,5))

                sns.countplot(
                    data=df,
                    x=variable_cat,
                    ax=ax
                )

                plt.xticks(rotation=45)

                plt.title(
                    f"Conteo de {variable_cat}"
                )

                st.pyplot(fig)

        # TAB 7
        # ======================================================

        with tab7:

            st.header("📌 Análisis Bivariado (Numérico vs Categórico)")

            col1, col2 = st.columns(2)

            with col1:

                num = st.selectbox(
                    "Seleccione variable numérica",
                    numericas,
                    key='num_tab7'
                )

            with col2:

                cat = st.selectbox(
                    "Seleccione variable categórica",
                    categoricas,
                    key='cat_tab7'
                )

            # DATASET REDUCIDO
            temp_df = df[[num, cat]].dropna()

            # LIMITAR REGISTROS
            if len(temp_df) > 3000:
                temp_df = temp_df.sample(3000)

            st.subheader(f"📊 {num} vs {cat}")

            fig, ax = plt.subplots(figsize=(10,5))

            sns.boxplot(
                data=temp_df,
                x=cat,
                y=num,
                ax=ax
            )

            plt.xticks(rotation=45)

            st.pyplot(fig)

            # TABLA RESUMEN
            resumen = temp_df.groupby(cat)[num].agg([
                'mean',
                'median',
                'std'
            ]).round(2)

            st.subheader("📈 Resumen Estadístico")

            st.dataframe(
                resumen,
                use_container_width=True
            )

        # ======================================================
        # TAB 8
        # ======================================================

        with tab8:

            st.header("📌 Análisis Categórico vs Categórico")

            col1, col2 = st.columns(2)

            with col1:

                cat1 = st.selectbox(
                    "Primera variable",
                    categoricas,
                    key='cat1_tab8'
                )

            with col2:

                cat2 = st.selectbox(
                    "Segunda variable",
                    categoricas,
                    key='cat2_tab8'
                )

            # TABLA CRUZADA REDUCIDA
            tabla = pd.crosstab(
                df[cat1],
                df[cat2]
            )

            # LIMITAR TAMAÑO
            tabla = tabla.iloc[:10, :10]

            col1, col2 = st.columns([1,2])

            with col1:

                st.subheader("📄 Tabla Cruzada")

                st.dataframe(
                    tabla,
                    use_container_width=True
                )

            with col2:

                fig, ax = plt.subplots(figsize=(10,5))

                tabla.plot(
                    kind='bar',
                    stacked=True,
                    ax=ax
                )

                plt.xticks(rotation=45)

                st.pyplot(fig)

        # ======================================================
        # TAB 9
        # ======================================================

        with tab9:

            st.header("📌 Análisis Dinámico")

            columnas_usuario = st.multiselect(
                "Seleccione columnas",
                df.columns.tolist(),
                default=df.columns.tolist()[:5]
            )

            if columnas_usuario:

                # SOLO 100 FILAS
                st.dataframe(
                    df[columnas_usuario].head(100),
                    use_container_width=True
                )

            filtro = st.selectbox(
                "Seleccione filtro",
                categoricas,
                key='filtro_tab9'
            )

            valores = df[filtro].dropna().unique()

            valor = st.selectbox(
                "Seleccione valor",
                valores,
                key='valor_tab9'
            )

            filtrado = df[df[filtro] == valor]

            st.subheader("📄 Dataset Filtrado")

            # LIMITAR FILAS
            st.dataframe(
                filtrado.head(100),
                use_container_width=True
            )

            st.info(
                f"Total registros encontrados: {len(filtrado)}"
            )

        # ======================================================
        # TAB 10
        # ======================================================

        with tab10:

            st.header("📌 Hallazgos Clave")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("📊 Resumen Estadístico")

                resumen = pd.DataFrame({
                    'Media': df[numericas].mean(),
                    'Mediana': df[numericas].median(),
                    'Desv Std': df[numericas].std()
                }).round(2)

                st.dataframe(
                    resumen,
                    use_container_width=True
                )

            with col2:

                st.subheader("📌 Moda Variables Categóricas")

                modas = {}

                # LIMITAR VARIABLES
                for col in categoricas[:10]:

                    try:
                        modas[col] = analyzer.moda(col)
                    except:
                        modas[col] = "N/A"

                moda_df = pd.DataFrame(
                    modas.items(),
                    columns=['Variable', 'Moda']
                )

                st.dataframe(
                    moda_df,
                    use_container_width=True
                )

            st.divider()

            st.success("✅ Principales Hallazgos")

            st.write("""
            • Clientes con contratos mensuales presentan mayor churn.
            """)

            st.write("""
            • Clientes con mayor MonthlyCharges muestran mayor fuga.
            """)

            st.write("""
            • Variables categóricas muestran diferencias relevantes.
            """)

            st.write("""
            • El análisis dinámico permite explorar segmentos específicos.
            """)

        # ======================================================
        # MATRIZ DE CORRELACIÓN
        # ======================================================

        if mostrar_correlacion:

            st.header("📌 Matriz de Correlación")

            corr = df[numericas].corr()

            fig, ax = plt.subplots(figsize=(10,5))

            sns.heatmap(
                corr,
                annot=False,
                cmap='coolwarm',
                ax=ax
            )

            st.pyplot(fig)

        # ITEM 11
        # =====================================================

        with tab11:

            st.header("📌 Conclusiones")

            # ======================================================
            # CONCLUSIÓN 1
            # ======================================================

            st.success("""
            ### 1️⃣ Clientes con contratos mensuales presentan mayor churn

            El análisis entre la variable Contract y Churn evidenció
            que los clientes con contratos mensuales (Month-to-month)
            tienen una mayor tendencia a abandonar el servicio.

            ✅ Toma de decisión:
            La empresa puede implementar estrategias de fidelización,
            beneficios por permanencia y promociones para incentivar
            contratos de mayor duración.
            """)

            # ======================================================
            # CONCLUSIÓN 2
            # ======================================================

            st.success("""
            ### 2️⃣ Clientes con mayores cargos mensuales muestran mayor fuga

            El análisis de MonthlyCharges vs Churn mostró que
            los clientes con cargos mensuales elevados presentan
            una mayor frecuencia de abandono.

            ✅ Toma de decisión:
            Se recomienda revisar los planes tarifarios y diseñar
            paquetes más competitivos para clientes con facturación alta.
            """)

            # ======================================================
            # CONCLUSIÓN 3
            # ======================================================

            st.success("""
            ### 3️⃣ Clientes con menor antigüedad presentan más abandono

            La variable tenure permitió identificar que los clientes
            con pocos meses en la empresa tienen mayor probabilidad
            de abandonar el servicio.

            ✅ Toma de decisión:
            Es importante fortalecer el proceso de onboarding,
            seguimiento y atención durante los primeros meses del cliente.
            """)

            # ======================================================
            # CONCLUSIÓN 4
            # ======================================================

            st.success("""
            ### 4️⃣ El tipo de servicio de internet influye en el churn

            El análisis categórico evidenció diferencias relevantes
            entre los tipos de InternetService y los niveles de churn.

            ✅ Toma de decisión:
            La empresa puede priorizar mejoras operativas y soporte técnico
            en los servicios con mayores niveles de fuga.
            """)

            # ======================================================
            # CONCLUSIÓN 5
            # ======================================================

            st.success("""
            ### 5️⃣ Métodos de pago automáticos muestran mayor estabilidad

            Los clientes que utilizan pagos automáticos y contratos
            de largo plazo presentan menores niveles de churn.

            ✅ Toma de decisión:
            Se recomienda incentivar métodos de pago automáticos
            y contratos anuales mediante descuentos y beneficios.
            """)