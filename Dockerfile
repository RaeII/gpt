# Use a imagem oficial do Python como base
FROM python:3.10.6

# Defina a variável de ambiente PYTHONUNBUFFERED para garantir que os logs do Python sejam enviados para o console
#ENV PYTHONUNBUFFERED=1

# Crie um diretório de trabalho e defina-o como o diretório de trabalho padrão
WORKDIR /app

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt /app/

#=======
#RUN pip install --upgrade pip

#COPY requirements.txt .
#RUN pip install --no-cache-dir --upgrade -r requirements.txt
#=======

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto para o diretório de trabalho
COPY . /app/

