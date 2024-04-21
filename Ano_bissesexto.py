"""(def)Função para verificar se um ano é bissexto ou não.

O (IF) e para Verificar se o ano é divisível por 4 ou por 400,se for divisível por 100 ele retorna else,pois nao seram bissexto.

(def main()) Ela é comumente usada como uma convenção,Função principal do programa."""

def verifica_bissexto(ano):
    if (ano  % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


def main():
    ano = int(input("Digite o ano desejado: "))
    if verifica_bissexto(ano):
        print(f"O ano {ano} é bissexto e possui 366 dias.")
    else:
        print(f"O ano {ano} não é bissexto e possui 365 dias.")
        
if __name__ == "__main__":
    main()




