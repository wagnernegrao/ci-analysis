# Continuous Integration Analysis

Base de dados utilizada  'travistorrent_11_1_2017.csv.gz',  disponivel em <a href="https://travistorrent.testroots.org/page_access/">TravisTorrent</a>, se faz necessário extrair o arquivo CSV para o mesmo diretório do código.

## Data Description

Nesta página <a href="https://travistorrent.testroots.org/page_dataformat/">aqui</a>, está descrito o formato de dados do TravisTorrent.


### Análise da frequência de commits
Dataset foi dividido em projetos de baixa, média e alta frequência e posteriormente foi analisado o quão frequente são projetos que usam CI? Mas que fazem commits infrequentes (menor que a média)? <a href="https://github.com/wagnerfns/ci-analysis/blob/master/src/analise_%20requencia_commits%20.ipynb">aqui</a>

### Tamanho de projetos e frequencia de commits por dia e meses
Foi realizado um filtro para definir tamanho dos projetos e suas respequitivas frequências, sendo estas por dia da semana e mês. <a href="https://github.com/wagnerfns/ci-analysis/blob/master/src/project_size_week_frequency.ipynb">aqui</a>

### How to run
For Linux environments, use the command on the terminal ```jupyter notebook``` to run the jupyter notebook locally.

Easy ways to run your Jupyter Notebook in the cloud:

* <a href="https://mybinder.org/">Binder</a>
* <a href="https://www.kaggle.com/kernels">Kaggle Kernels</a>
* <a href="https://colab.research.google.com/notebooks/welcome.ipynb">Google Colaboratory (Colab)</a>
* <a href="https://notebooks.azure.com/">Microsoft Azure Notebooks</a>
* <a href="https://cocalc.com/">CoCalc</a>
* <a href="https://datalore.io/">Datalore</a>

##  License
<a href="https://github.com/wagnerfns/ci-analysis/blob/master/LICENSE">MIT</a>
