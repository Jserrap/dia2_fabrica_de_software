# Verificar se numero é impar ou par
# Mesma coisa do dia 1
def imparOuPar(): 
    # Recebe numero
    numero = float(input('Digite um número: '));
    # Operador ternario, se resto da divisão por 2 = 0 é par, se não, impar
    numero = 'par' if numero % 2 == 0 else 'Impar';
    print(numero);

# fazer loop com while e com for 
# Fazer duas funções que retornam qualquer valor
# Juntei ambas em uma

# Recebe valor maximo
def loopFor(max):
    # Array de retorno que recebera um valor novo a cada iteraçãi
    retorno = []
    # Executa
    for val in range(0,max + 1):
        # Adiciona valor ao retorno
        retorno.append(val);
    # retorna o array
    return retorno

loopFor(40);

# Recebe valor maximo
def loopWhile(max):
    # Array de retorno que recebera um valor novo a cada iteração
    retorno = []
    # contador
    i = 0;
    # Enquanto contador for menor ou igual ao parametro ele executa
    while i <= max: 
        # adiciona ao array
        retorno.append(i)
        # contador + 1
        i += 1;
    # retorna o array
    return retorno

loopWhile(40);

# recebe um nome, e escreve-o
def escreveNome(nome):
    print(nome);

escreveNome('Joao')

