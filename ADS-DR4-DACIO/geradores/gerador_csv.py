import pandas as pd
import random
import csv
from faker import Faker

fake = Faker('pt_BR')
Faker.seed(42)
random.seed(42)

def generate_record():
    record = {}
    record['nome'] = fake.name()
    record['idade'] = random.choice([random.randint(18, 90), '', None])  # idade válida ou vazio
    record['sexo'] = random.choice(['M', 'F', 'Outro', '', None])  # gênero válido ou vazio
    record['cpf'] = random.choice([fake.cpf(), '123.456.789-00', '', None])  # CPF válido ou sujo
    record['escolaridade'] = random.choice(['Ensino Fundamental', 'Ensino Médio', 'Graduação', 'Mestrado', 'Doutorado', '', None])  # escolaridade válida ou vazio
    record['data_nasc'] = random.choice([fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'), '32/13/2000', '', None])  # data válida ou suja
    return record

# Generate 1000 records
records = [generate_record() for _ in range(1000)]

# Convert to DataFrame
df = pd.DataFrame(records)

# Save to CSV
df.to_csv('dados_sujos.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

print("CSV com dados sujos gerado com sucesso.")
