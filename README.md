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

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Python 3.7](https://www.python.org/downloads/release/python-376/)
* [Pipenv](https://github.com/pypa/pipenv)
* [Microframework Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Guia de Instalação

1. Tenha Docker e Docker Compose instalados (preferencialmente nas ultimas versões)

2. Siga o exemplo de `contrib/env-sample` e crie um arquivo `.env` na raiz do projeto.

3. Execute o projeto
    > $ docker-compose up

3. *(opicional)* Outra opção para execução é subir primeiramente o container do banco
    e em seguida o da aplicação
    > $ docker-compose up -d db

    > $ docker-compose run --service-ports --rm web
