#Crie um programa que simule a operação de dois grupos de amigos decidindo para quais filmes irão juntos ao cinema:
#Cada grupo tem sua própria lista de filmes preferidos (com possíveis duplicatas).
#O programa deve determinar quais filmes são comuns a ambos os grupos (interseção) e sugerir essas opções.

grupo_a = [
    "Forrest Gump",
    "A Origem (Inception)",
    "Clube da Luta (Fight Club)",
    "O Cavaleiro das Trevas (The Dark Knight)",
    "Star Wars: Uma Nova Esperança (Star Wars: A New Hope)",
    "Pulp Fiction: Tempo de Violência (Pulp Fiction)",
    "Harry Potter e a Pedra Filosofal (Harry Potter and the Philosopher's Stone)",
    "Gladiador (Gladiator)",
    "O Silêncio dos Inocentes (The Silence of the Lambs)",
    "A Lista de Schindler (Schindler's List)",
    "Se7en - Os Sete Crimes Capitais (Se7en)",
    "Coração Valente (Braveheart)"
]

grupo_b = [
    "O Poderoso Chefão (The Godfather)",
    "Vingadores: Ultimato (Avengers: Endgame)",
    "Matrix",
    "Titanic",
    "A Origem (Inception)",
    "O Cavaleiro das Trevas (The Dark Knight)",
    "O Senhor dos Anéis: O Retorno do Rei (The Lord of the Rings: The Return of the King)",
    "Star Wars: O Império Contra-Ataca (Star Wars: The Empire Strikes Back)",
    "Pulp Fiction: Tempo de Violência (Pulp Fiction)",
    "Forrest Gump",
    "O Resgate do Soldado Ryan (Saving Private Ryan)",
    "Harry Potter e a Pedra Filosofal (Harry Potter and the Philosopher's Stone)",
    "Gladiador (Gladiator)",
    "O Senhor dos Anéis: A Sociedade do Anel (The Lord of the Rings: The Fellowship of the Ring)",
    "O Silêncio dos Inocentes (The Silence of the Lambs)",
    "De Volta para o Futuro (Back to the Future)",
    "A Lista de Schindler (Schindler's List)",
    "O Rei Leão (The Lion King)",
    "Jurassic Park",
]

set_grupo_a = set(grupo_a)
set_grupo_b = set(grupo_b)
filmes_em_comum = set_grupo_a.intersection(set_grupo_b)
print(f'Filmes em comuns entre os grupos:\n{filmes_em_comum}')
