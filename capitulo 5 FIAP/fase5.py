import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.cluster import KMeans
import numpy as np

print("Bibliotecas importadas!")

# 1. CARREGAR OS DADOS

df = pd.read_csv("crop_yield.csv")

# Renomeia as colunas para português
df.columns = ["Cultura", "Precipitacao", "Umidade_Especifica", "Umidade_Relativa", "Temperatura", "Rendimento"]

print("\n--- Primeiras linhas do dataset ---")
print(df.head())

# 2. ANÁLISE EXPLORATÓRIA

print("\n--- Informações gerais ---")
print(f"Linhas: {df.shape[0]} | Colunas: {df.shape[1]}")
print(f"\nValores nulos:\n{df.isnull().sum()}")
print(f"\nEstatísticas:\n{df.describe().round(2)}")
print(f"\nCulturas presentes:\n{df['Cultura'].value_counts()}")

# Gráfico 1 - Rendimento médio por cultura
df.groupby("Cultura")["Rendimento"].mean().sort_values().plot(kind="barh", color="steelblue")
plt.title("Rendimento Médio por Cultura")
plt.xlabel("Rendimento Médio")
plt.tight_layout()
plt.savefig("grafico1_rendimento.png")
plt.show()

# Gráfico 2 - Boxplot do rendimento por cultura
sns.boxplot(data=df, x="Cultura", y="Rendimento")
plt.title("Distribuição do Rendimento por Cultura")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("grafico2_boxplot.png")
plt.show()

# Gráfico 3 - Correlação entre variáveis numéricas
colunas = ["Precipitacao", "Umidade_Especifica", "Umidade_Relativa", "Temperatura", "Rendimento"]
sns.heatmap(df[colunas].corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlação entre Variáveis")
plt.tight_layout()
plt.savefig("grafico3_correlacao.png")
plt.show()

# 3. CLUSTERIZAÇÃO (K-MEANS)

print("\n--- Clusterização ---")

# Transforma a coluna Cultura em número (o modelo não entende texto)
le = LabelEncoder()
df["Cultura_num"] = le.fit_transform(df["Cultura"])

# Seleciona as colunas para clusterizar
X_cluster = df[["Precipitacao", "Umidade_Especifica", "Umidade_Relativa", "Temperatura", "Rendimento", "Cultura_num"]]

# Normaliza os dados
scaler_c = StandardScaler()
X_cluster_norm = scaler_c.fit_transform(X_cluster)

# Método do cotovelo - descobre o melhor número de clusters
inercias = []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_cluster_norm)
    inercias.append(km.inertia_)

plt.plot(range(2, 11), inercias, marker="o", color="steelblue")
plt.title("Método do Cotovelo")
plt.xlabel("Número de Clusters")
plt.ylabel("Inércia")
plt.tight_layout()
plt.savefig("grafico4_cotovelo.png")
plt.show()

# Aplica K-Means com 4 clusters (um por cultura)
km = KMeans(n_clusters=4, random_state=42, n_init=10)
df["Cluster"] = km.fit_predict(X_cluster_norm)

print("Média de rendimento por cluster:")
print(df.groupby("Cluster")["Rendimento"].mean().round(2))

# Detecta outliers com IQR
Q1 = df["Rendimento"].quantile(0.25)
Q3 = df["Rendimento"].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df["Rendimento"] < Q1 - 1.5 * IQR) | (df["Rendimento"] > Q3 + 1.5 * IQR)]
print(f"\nOutliers encontrados: {len(outliers)}")
print(outliers[["Cultura", "Rendimento"]])

# 4. PREPARAÇÃO PARA OS MODELOS

# Features (variáveis de entrada) e target (o que queremos prever)
X = df[["Precipitacao", "Umidade_Especifica", "Umidade_Relativa", "Temperatura", "Cultura_num"]]
y = df["Rendimento"]

# Divide em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normaliza
scaler = StandardScaler()
X_train_norm = scaler.fit_transform(X_train)
X_test_norm  = scaler.transform(X_test)

print(f"\nTreino: {X_train.shape[0]} amostras | Teste: {X_test.shape[0]} amostras")

# 5. OS 5 MODELOS DE REGRESSÃO

# Função para calcular e mostrar as métricas de cada modelo
def avaliar(nome, y_real, y_previsto):
    mae  = mean_absolute_error(y_real, y_previsto)
    rmse = np.sqrt(mean_squared_error(y_real, y_previsto))
    r2   = r2_score(y_real, y_previsto)
    print(f"\n{nome}")
    print(f"  MAE  (erro médio absoluto): {mae:,.0f}")
    print(f"  RMSE (erro quadrático):     {rmse:,.0f}")
    print(f"  R2   (acurácia):            {r2:.4f}")
    return {"Modelo": nome, "MAE": round(mae, 2), "RMSE": round(rmse, 2), "R2": round(r2, 4)}

print("\n--- RESULTADOS DOS MODELOS ---")
resultados = []

# Modelo 1 - Regressão Linear
m1 = LinearRegression()
m1.fit(X_train_norm, y_train)
resultados.append(avaliar("Regressão Linear", y_test, m1.predict(X_test_norm)))

# Modelo 2 - Árvore de Decisão
m2 = DecisionTreeRegressor(max_depth=5, random_state=42)
m2.fit(X_train, y_train)
resultados.append(avaliar("Árvore de Decisão", y_test, m2.predict(X_test)))

# Modelo 3 - Random Forest
m3 = RandomForestRegressor(n_estimators=100, random_state=42)
m3.fit(X_train, y_train)
resultados.append(avaliar("Random Forest", y_test, m3.predict(X_test)))

# Modelo 4 - Gradient Boosting
m4 = GradientBoostingRegressor(n_estimators=100, random_state=42)
m4.fit(X_train, y_train)
resultados.append(avaliar("Gradient Boosting", y_test, m4.predict(X_test)))

# Modelo 5 - SVR
m5 = SVR(kernel="rbf", C=100)
m5.fit(X_train_norm, y_train)
resultados.append(avaliar("SVR", y_test, m5.predict(X_test_norm)))

# 6. COMPARAÇÃO FINAL DOS MODELOS

tabela = pd.DataFrame(resultados).sort_values("R2", ascending=False).reset_index(drop=True)
print("\n--- TABELA COMPARATIVA ---")
print(tabela)

# Gráfico comparativo de R2
plt.barh(tabela["Modelo"], tabela["R2"], color="steelblue", edgecolor="black")
plt.title("Comparação de R2 entre os Modelos")
plt.xlabel("R2 (quanto maior, melhor)")
plt.tight_layout()
plt.savefig("grafico5_comparacao_r2.png")
plt.show()

print(f"\nMelhor modelo: {tabela.iloc[0]['Modelo']} com R2 = {tabela.iloc[0]['R2']}")
print("\nCódigo finalizado! Todos os gráficos foram salvos na pasta.")