# GITZWC IMG Decrypt

Uma ferramenta simples para descriptografar arquivos .img de avatares que são criptografados no GitzWC

## Funcionalidades

- **Descriptografia individual**: Processa um arquivo .img específico
- **Descriptografia em lote**: Processa todos os arquivos .img em um diretório
- **Interface interativa**: Menu simples para facilitar o uso
- **Processamento otimizado**: Apenas os primeiros 5000 bytes são processados (suficiente para descriptografia)

## Pré-requisitos

- Python 3.x instalado no sistema

## Como Usar

1. Clone ou baixe este repositório:

   ```bash
   git clone https://github.com/samuelrizzo/gitzwc-img-decrypt.git
   cd gitzwc-img-decrypt
   ```

2. Execute o script:

   ```bash
   python main.py
   ```

3. Escolha uma das opções do menu:

   - **Opção 1**: Descriptografar todos os arquivos .img de um diretório
   - **Opção 2**: Descriptografar um arquivo .img específico
   - **Opção 3**: Sair do programa

## Exemplo de Uso

### Descriptografando um diretório:

```
Digite o caminho do diretório: /caminho/para/imagens
Encontrados 3 arquivo(s) .img:
  1. imagem1.img
  2. imagem2.img
  3. imagem3.img

Descriptografando com chave 94...
✓ Sucesso! Arquivo descriptografado: imagem1_decrypted.img
  Processados 5000 bytes do arquivo original de 245760 bytes
✓ Sucesso! Arquivo descriptografado: imagem2_decrypted.img
  Processados 5000 bytes do arquivo original de 122880 bytes

=== Resultado ===
✓ 2/3 arquivos descriptografados com sucesso
```

## Detalhes Técnicos

- **Algoritmo**: XOR com chave fixa (94)
- **Limite de processamento**: 5000 bytes iniciais (somente esses são encriptados)
- **Formato de saída**: `_decrypted.img` (adicionado ao nome original)
- **Compatibilidade**: Arquivos .img encryptados do GitzWC

## Autor

Criado por rizzo
