# Password Hash Cracker - Python

Este projeto é um script simples em Python para tentar descobrir a senha original a partir de um hash (SHA-256, SHA-1, MD5 e outros), usando um arquivo wordlist (lista de senhas comuns) para testar possíveis senhas.

## Como funciona?

O script lê um hash fornecido pelo usuário, tenta calcular o hash de cada senha da wordlist e compara com o hash alvo. Quando encontra uma senha cujo hash bate com o fornecido, exibe essa senha e para a execução.

## Funcionalidades

- Suporta múltiplos algoritmos de hash: sha256 (padrão), sha1, md5, entre outros suportados pelo Python.
- Usa a biblioteca `tqdm` para mostrar uma barra de progresso durante as tentativas.
- Lê o arquivo `rockyou.txt` (wordlist popular para testes de cracking) no mesmo diretório.
- Verifica se o algoritmo passado é válido antes de executar.

## Requisitos

- Python 3.x
- Biblioteca tqdm (`pip install tqdm`)
- Wordlist rockyou.txt ou qualquer outra de sua escolha

## Como usar

```bash
python cracker.py <hash> [algoritmo]
```
<hash>: o hash da senha que você quer descobrir.

[algoritmo]: (opcional) algoritmo usado para gerar o hash. Padrão é sha256. Exemplos: sha256, sha1, md5.

## Observações
O arquivo rockyou.txt deve estar no mesmo diretório do script, ou você pode modificar o caminho no código.

Este script é para fins educacionais, para entender como funciona o processo de cracking por força bruta.

Quebrar senhas sem autorização é ilegal e antiético.



