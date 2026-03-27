# 👕 Sistema de Cobrança: Atacado de Camisetas

Este projeto é um sistema de cobrança automatizado que utiliza funções modulares para calcular orçamentos de vendas em atacado, aplicando descontos progressivos e taxas de logística.

### ⚙️ Funcionalidades:
- **Seleção de Modelo**: Interface para escolha entre diferentes tipos de camisetas (Manga Curta/Longa, com ou sem estampa).
- **Cálculo de Desconto Progressivo**: Lógica que aplica descontos (5%, 7%, 12%) baseados no volume do pedido.
- **Gestão de Frete**: Opções integradas para transportadora, Sedex ou retirada no local.
- **Tratamento de Erros**: Uso de blocos `try/except` para garantir que o programa não encerre ao receber dados não numéricos.

### 🧠 Conceitos Técnicos Avançados Aplicados:
- **Programação Modular**: Uso de funções independentes para cada etapa do processo (`escolha_modelo`, `num_camisetas`, `frete`).
- **Escopo e Retorno**: Implementação de `return` para passar dados entre funções e o corpo principal do programa.
- **Robustez de Código**: Validação de entradas e limites máximos de pedido (20.000 unidades).
- **Lógica Matemática**: Aplicação de fórmulas para cálculo de total final: `(modelo * num_camisetas) + frete`.
