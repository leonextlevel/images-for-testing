# IMAGES FOR TESTING

## Informações Básicas

**SOBRE:** Esse projeto é um Trabalho de Gradução (TG) desenvolvido sob o formato "Relatório Técnico" da FATEC São
José dos Campos - Profº Jessen Vidal, na disciplina de Laboratório de Engenharia de Software.

**ALUNO:** Leandro Lopes Bueno.

**ORIENTADOR:** Fabricio Galande Marques de Carvalho.

**TEMA:** Sistema web para geração de casos de teste de imagens digitais.

**JUSTIFICATIVA:** Muitos sistemas utilizados em reconhecimento de imagens necessitam de casos de teste para avaliar sua
robustez em relação a diversos fatores, tais como reamostragem, transformações afins, etc. A geração de imagens de teste
pode se tornar uma tarefa fastidiosa caso não seja automatizada. Esse trabalho preocupa-se com especificação e com o
desenvolvimento de um sistema para geração de casos de teste envolvendo diversas transformações associadas a imagens
digitais.

**PROPOSTA:** O trabalho desenvolverá tanto os módulos para execução de tais transformações, como um sistema web que os utilize
e exemplifique o resultado da geração de casos de teste.

## Ferramentas

* [Python 3.7](https://www.python.org/downloads/release/python-376/)
* [Pipenv](https://github.com/pypa/pipenv)
* [Microframework Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Guia de Instalação

1. Tenha devidamente instalado em sua máquina o **Python 3.7** e **Pip**

2. Instale o gerenciador de dependencias e ambiente virtual **pipenv**
    > $ pip install pipenv

3. Na raiz do projeto instale as dependencias de desenvolvimento com o pipenv *(Isso irá criar um ambiente virtual com elas automaticamente)*
    > $ pipenv sync -d

4. Para ativar o ambiente virtual execute na raiz do projeto
    > $ pipenv shell

5. Crie um arquivo .env na raiz com base em `contrib/env-sample`

6. Crie um banco de dados e aplique as migrações para estruturá-lo *(Só executar o comando já criará um banco sqlite, é a maneira mais simples)*
    > $ flask db upgrade

7. Por último, se tudo estiver certo, basta executar a aplicação
    > $ flask run
