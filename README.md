# FarmTech-na-Era-da-Cloud-Computing
# 🌱 FarmTech Solutions – Fase 5

**Aluna:** Luana Brito da Silva | **RM:** 566632 | **Curso:** IA – FIAP

---

## 📁 O que tem nesse repositório

| Arquivo | Descrição |
|---|---|
| `LuanaBritoSilva_rm566632_pbl_fase4.ipynb` | Notebook com toda a solução de Machine Learning |
| `crop_yield.csv` | Dataset com dados da fazenda |
| `README.md` | Este arquivo |

---

# 📓 Entrega 1 – Machine Learning

O notebook resolve o problema de prever o rendimento de safras de uma fazenda de 200 hectares usando Machine Learning. Ele está dividido em 8 etapas:

1. Importação de bibliotecas
2. Carregamento e leitura dos dados
3. Análise Exploratória (gráficos e estatísticas)
4. Clusterização com K-Means e detecção de outliers
5. Preparação dos dados para os modelos
6. Treinamento de 5 modelos de regressão
7. Comparação dos modelos com métricas (MAE, RMSE, R²)
8. Conclusões

### 👉 [Acesse o Notebook completo aqui](./LuanaBritoSilva_rm566632_pbl_fase4.ipynb)

### 🎥 Vídeo – Entrega 1
📹 [Assista no YouTube](https://www.youtube.com/LINK_AQUI)

---

# ☁️ Entrega 2 – Computação em Nuvem AWS

## Por que usar a nuvem?

O modelo de Machine Learning desenvolvido na Entrega 1 precisa funcionar de forma contínua, recebendo dados dos sensores da fazenda e gerando previsões em tempo real. Para isso, ele precisa estar hospedado em um servidor sempre disponível — e a **AWS (Amazon Web Services)** é uma das principais plataformas de nuvem do mundo, oferecendo servidores sob demanda com alta disponibilidade.

---

## Qual servidor usar?

O enunciado pede uma máquina com as seguintes configurações:

| Especificação | Valor exigido |
|---|---|
| Sistema Operacional | Linux |
| CPUs | 2 |
| Memória RAM | 1 GiB |
| Rede | Até 5 Gbps |
| Armazenamento | 50 GB |
| Modalidade de pagamento | On-Demand (100%) |

A instância da AWS que atende **exatamente** essas especificações é a **t3.micro**:

| Característica | t3.micro |
|---|---|
| vCPUs | 2 |
| Memória | 1 GiB |
| Rede | Até 5 Gbps |
| Família | General Purpose |
| Sistema | Linux |

---

## Comparação de Custos: São Paulo × Virgínia do Norte

Os valores abaixo foram obtidos diretamente na **AWS Pricing Calculator** (calculadora oficial da Amazon), com as configurações exigidas: instância t3.micro, Linux, On-Demand, 50 GB de armazenamento.

| | 🇧🇷 São Paulo (sa-east-1) | 🇺🇸 Virgínia do Norte (us-east-1) |
|---|---|---|
| EC2 t3.micro (mensal) | $12,26 USD | $7,59 USD |
| Armazenamento 50 GB (mensal) | $7,60 USD | $4,00 USD |
| **Total mensal** | **$19,86 USD** | **$11,59 USD** |
| **Total anual** | **~$238,32 USD** | **~$139,08 USD** |

> 📸


### Gráfico comparativo

```
Custo Mensal – t3.micro + 50GB (On-Demand / Linux)
────────────────────────────────────────────────────
🇧🇷 São Paulo         ████████████████████  $19,86
🇺🇸 Virgínia do Norte ████████████          $11,59
────────────────────────────────────────────────────
                      $0        $10        $20
```

A Virgínia do Norte é cerca de **41% mais barata** do que São Paulo para essa configuração.

---

## Qual região escolher?

Apesar de Virgínia do Norte ser mais barata, a melhor escolha para este projeto é **São Paulo**. Veja o porquê:

### 1. Acesso rápido aos sensores (latência)

Os sensores da fazenda estão no Brasil. Quando um sensor envia dados para o servidor, quanto mais longe o servidor estiver, mais tempo demora para receber e processar os dados. Esse atraso se chama **latência**.

| | 🇧🇷 São Paulo | 🇺🇸 Virgínia do Norte |
|---|---|---|
| Distância até a fazenda | ~100–500 km | ~8.000 km |
| Latência típica | 5 a 20 ms | 150 a 250 ms |
| Ideal para sensores em tempo real? | ✅ Sim | ❌ Não |

Para uma API que processa dados de sensores agrícolas em tempo real, uma latência de 200ms pode comprometer a velocidade das previsões.

### 2. Restrições legais – LGPD

A **Lei Geral de Proteção de Dados (LGPD – Lei nº 13.709/2018)** é uma lei brasileira que regula como os dados devem ser armazenados e tratados. Ela impõe restrições ao envio de dados para servidores fora do Brasil.

Ao hospedar em **São Paulo**, todos os dados ficam em território nacional, garantindo:
- ✅ Conformidade total com a LGPD
- ✅ Sem risco de penalidades legais
- ✅ Soberania dos dados da fazenda

### 3. A diferença de preço é pequena

A diferença entre as duas regiões é de apenas **$8,27 USD por mês** (cerca de R$ 41,00). Para uma fazenda comercial de 200 hectares, esse valor é mínimo perto dos benefícios de latência baixa e segurança jurídica.

---

## Decisão Final

| Critério | 🇧🇷 São Paulo | 🇺🇸 Virgínia do Norte |
|---|---|---|
| Custo mensal | ❌ $19,86 | ✅ $11,59 |
| Latência para sensores no Brasil | ✅ Baixa (5–20ms) | ❌ Alta (150–250ms) |
| Conformidade com a LGPD | ✅ Total | ❌ Risco legal |
| Dados em território nacional | ✅ Sim | ❌ Não |
| **Escolha final** | ✅ **ESCOLHIDA** | ❌ |

> ✅ **Conclusão:** A região de **São Paulo (sa-east-1)** é a escolha correta para este projeto. Embora seja mais cara, ela garante baixa latência para os sensores da fazenda e total conformidade com a legislação brasileira de proteção de dados.

---

## 🎥 Vídeo – Entrega 2
📹 [Assista no YouTube](https://www.youtube.com/LINK_AQUI)

---

*Projeto desenvolvido para a Fase 5 do curso de Inteligência Artificial – FIAP | 2025*
