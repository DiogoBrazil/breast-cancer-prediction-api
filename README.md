
# **Previsão de Câncer de Mama - API com FastAPI** 🩺

Este projeto é uma **API desenvolvida em Python utilizando FastAPI**, que disponibiliza um **modelo de machine learning** para prever a probabilidade de uma imagem indicar **câncer de mama** ou ser **normal**. O modelo foi treinado utilizando **TensorFlow** e está hospedado localmente na aplicação.

---

## **Índice**
- [Descrição](#descrição)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Exemplo de Uso](#exemplo-de-uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Autor](#autor)

---

## **Descrição**

A aplicação recebe uma **imagem via endpoint HTTP**, faz o pré-processamento necessário e realiza a **predição usando um modelo TensorFlow**. A resposta é fornecida em **JSON**, contendo as probabilidades (em porcentagens) para cada classe:
- **Câncer**
- **Normal**

---

## **Instalação**

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/DiogoBrazil/breast_cancer_api.git
   cd breast_cancer_api
   ```

2. **Crie e Ative o Ambiente Virtual** (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

3. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Como Usar**

1. **Execute o Servidor**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Acesse a Interface de Documentação**:
   - Abra [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) no navegador.
   - Use a interface Swagger para enviar imagens e ver as predições.

---

## **Exemplo de Uso via `curl`**

```bash
curl -X POST \
-F "file=@caminho/para/imagem.jpg" \
http://127.0.0.1:8000/predict/
```

**Resposta:**
```json
{
  "prediction": {
    "cancer": "85.34%",
    "normal": "14.66%"
  }
}
```

---

## **Estrutura do Projeto**

```
/breast_cancer_api
│
├── models/
│   └── best-23-10-2024.keras       # Modelo TensorFlow treinado
├── main.py                         # Código da API com FastAPI
├── requirements.txt                # Dependências do projeto
└── README.md                       # Documentação do projeto
```

---

## **Autor**

Projeto desenvolvido por [DiogoBrazil](https://github.com/DiogoBrazil).  
Sinta-se à vontade para contribuir ou abrir issues no repositório.

---

## **Licença**

Este projeto está sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## **Conclusão**

Este projeto demonstra como integrar **machine learning** com **FastAPI** para criar uma API eficiente e escalável. Se você tiver sugestões ou dúvidas, entre em contato ou abra uma issue no repositório.
