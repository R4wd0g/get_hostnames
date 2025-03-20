# Resolvedor de Hostnames

Este projeto resolve os hostnames de uma lista de endereços IP fornecida em um arquivo de texto e salva os resultados em um arquivo CSV.

## Arquivos

- `resolve_ips.py`: Script Python que realiza a resolução dos hostnames.
- `ips.txt`: Arquivo de entrada contendo a lista de endereços IP.
- `hostnames.csv`: Arquivo de saída contendo os endereços IP e seus respectivos hostnames.

## Como usar

1. Adicione os endereços IP no arquivo `ips.txt`, um por linha.
2. Execute o script `resolve_ips.py`:
    ```sh
    python resolve_ips.py
    ```
3. O resultado será salvo no arquivo `hostnames.csv`.

## Dependências

- Python 3.x

## Notas

- Caso um hostname não seja encontrado para um determinado IP, o valor `not_found` será salvo no arquivo de saída.