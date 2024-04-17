# kaggle-ingest

### Primeiros passos:

1. Acessar conta no Kaggle (criar caso não possua). Ir para `Settings -> API -> Create New Token`. Este passo criará 
suas chaves de autenticação e realizará o download para a sua máquina.
2. Criar uma pasta `~/.kaggle` na sua home e mover o arquivo *kaggle.json* para dentro dela.
3. Setar as permissões de leitura para o arquivo com `chmod 600 ~/.kaggle/kaggle.json`

### Ambiente virtual
Para qualquer projeto em Python, recomenda-se a instalação de um ambiente virtual. Portanto, escolha um de sua preferência e 
instale as dependências dentro do mesmo.

### Instalando as dependências

```commandline
pip install -r requirements.txt
```

### Executando o script
Dentro da pasta `/app`, executar o comando:

```commandline
python main.py
```
