# Imagem base do Ubuntu 22.04
FROM ubuntu:22.04

# Evita seleções interativas durante a instalação de pacotes
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza pacotes e instala Python, pip e utilitários do sistema
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instala o Jupyter Notebook e o Kernel Python
RUN pip3 install --no-cache-dir jupyter notebook ipykernel

# Configura o diretório de trabalho padrão dentro do container
WORKDIR /app

# Expõe a porta do Jupyter Notebook
EXPOSE 8888

# Mantém o terminal interativo disponível
CMD ["bash"]