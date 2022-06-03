"""
    Classe que representa cada unidade de informação (nodo) da
    árvore binária de busca
    É formada por três partes:
    1) Informação relevante para o usuário (data)
    2) Ponteiro para a subárvore esquerda (left)
    3) Ponteiro para a subárvore direita (right)
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

"""
    ESTRUTURA DE DADOS ÁRVORE BINÁRIA DE BUSCA
    * Árvore ~> é uma estrutura de dados não-linear, hierárquica,
      formada recursivamente por outras árvores (subárvores)
    * Árvore binária ~> uma árvore na qual cada nodo tem grau máximo
      igual a 2. Em outras palavras, cada nodo pode ter até dois
      descendentes diretos
    * Árvore binária de busca ~> é uma árvore binária em que as inserções
      são feitas de forma ordenada, de modo a otimizar a operação de busca
      binária
"""
class BinarySearchTree:

    """ Método construtor """
    def __init__(self):
        self.__root = None      # Raiz da árvore

    """
        Método PÚBLICO para inserção de um VALOR na árvore
    """
    def insert(self, val):
        # Cria um novo nodo para armazenar o valor passado pelo usuário
        inserting = Node(val)

        # 1º caso: a árvore está vazia. O primeiro nodo inserido será a raiz
        if self.__root is None: self.__root = inserting

        # 2º caso: a raiz já existe. É necessário procurar recursivamente
        # pela posição de inserção do novo nodo
        else: self.__insert_node(self.__root, inserting)

    """
        Método PRIVADO para inserção de um NODO na árvore
    """
    def __insert_node(self, root, inserting):
        # 1º caso: o valor do novo nodo é MENOR que o valor na raiz
        if inserting.data < root.data:
            # Se a esquerda da raiz estiver desocupada, faz aí a inserção
            if root.left is None: root.left = inserting
            # Senão, passa a considerar o nodo da esquerda como raiz
            else: self.__insert_node(root.left, inserting)
        # 2º caso: o valor do novo nodo é MAIOR que o valor da raiz
        elif inserting.data > root.data:
            # Se a direita da raiz estiver desocupada, faz aí a inserção
            if root.right is None: root.right = inserting
            # Senão, passa a considerar o nodo da direita como raiz
            else: self.__insert_node(root.right, inserting)
    """
        Método que percorre a árvore em ordem
        1º percorre a subárvore esquerda
        2º percorre a raiz
        3º percorre a subárvore direita
    """        
    def in_order_traversal(self, root = False):   # Percorre a árvore em ordem
        newline = False                           # Flag para quebra de linha 
        if root is False:                         # Se não for passado um nodo como parâmetro
            root = self.__root                    # Se não foi passado um nodo, considera a raiz
            newline = True                        # Imprime uma quebra de linha no início
        if root is not None:                      # Se a raiz não for nula
            self.in_order_traversal(root.left)    # percorre a subárvore esquerda
            print(str(root.data) + ' ', end='')   # imprime a raiz
            self.in_order_traversal(root.right)   # percorre a subárvore direita



#######################################################################################


    """ Método que percorre a árvore pré-ordem
        1º percorre a raiz
        2º percorre a subárvore esquerda
        3º percorre a subárvore direita
    """        
    def pre_order_traversal(self, root = False):   # Percorre a árvore em ordem
        newline = False                            # Flag para quebra de linha 
        if root is False:                          # Se não for passado um nodo como parâmetro
            root = self.__root                     # Se não foi passado um nodo, considera a raiz
            newline = True                         # Imprime uma quebra de linha no início
        if root is not None:                       # Se a raiz não for nula
            print(str(root.data) + ' ', end='')    # imprime a raiz
            self.pre_order_traversal(root.left)    # percorre a subárvore esquerda
            self.pre_order_traversal(root.right)   # percorre a subárvore direita
        if newline: print('\n')                    # Se a flag de quebra de linha estiver ativa, imprime uma quebra de linha

#######################################################################################


    """ Método que percorre a árvore post-ordem
        1º percorre a raiz
        2º percorre a subárvore esquerda
        3º percorre a subárvore direita
    """        
    def post_order_traversal(self, root = False):   # Percorre a árvore em ordem
        newline = False                             # Flag para quebra de linha 
        if root is False:                           # Se não for passado um nodo como parâmetro
            root = self.__root                      # Se não foi passado um nodo, considera a raiz
            newline = True                          # Imprime uma quebra de linha no início
        if root is not None:                        # Se a raiz não for nula
            self.post_order_traversal(root.left)    # percorre a subárvore esquerda
            self.post_order_traversal(root.right)   # percorre a subárvore direita
            print(str(root.data) + ' ', end='')     # imprime a raiz
        if newline: print('\n')                     # Se a flag de quebra de linha estiver ativa, imprime uma quebra de linha
        
        

        
arvore = BinarySearchTree() # Cria uma árvore

arvore.insert(37)  
arvore.insert(20)
arvore.insert(51)
arvore.insert(3)
arvore.insert(43)
arvore.insert(0)
arvore.insert(72)
arvore.insert(11)
arvore.insert(40)
arvore.insert(8)
arvore.insert(66)
arvore.insert(19)
arvore.insert(75)

print(60 * '-')
print("In-order")
arvore.in_order_traversal() # Percorre a árvore em ordem
print('\n')
print(60 * '-')

print("Pre-order")
arvore.pre_order_traversal() # Percorre a árvore em ordem
print(60 * '-')

print("Post-order")
arvore.post_order_traversal() # Percorre a árvore em ordem
print(60 * '-')
        