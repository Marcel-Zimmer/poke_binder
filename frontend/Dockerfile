# Usa uma imagem do Node.js leve
FROM node:20-alpine

# Define a pasta de trabalho
WORKDIR /app

# Instala o Angular CLI globalmente
RUN npm install -g @angular/cli

# Copia os arquivos de dependência primeiro (melhora o cache do Docker)
COPY package.json package-lock.json* ./

# Instala as dependências do projeto
RUN npm install

# Copia o restante do código
COPY . .

# Expõe a porta 4200
EXPOSE 4200

# Comando para iniciar o Angular, acessível externamente (--host 0.0.0.0)
CMD ["ng", "serve", "--host", "0.0.0.0", "--poll", "2000"]