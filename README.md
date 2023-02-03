# Teste A/B Bayesiana


## 1. A empresa Electronic House

A Electronic House é um comercio online ( e-commerce ) de produtos de informática
para casas e escritórios. Os clientes podem comprar mouses, monitores, teclados,
computadores, laptops, cabos HDMI, fones de ouvido, cameras webcam, entre
outros, através de um site online e recebem os produtos no conforto de suas casas.
O time de UX designers vem trabalhando em uma nova página de vendas, com o
objetivo de aumentar a taxa de conversão de um produto da loja, um teclado
bluetooth. O product manager (gerente de produto) disse que a taxa de conversão
da página atual é de 13% em média, no último ano.

O objetivo do product manager é aumentar a taxa de conversão em 2%, ou seja, a
nova página de vendas, desenvolvida pelo time de UX, seria um sucesso se a sua
taxa de conversão fosse de 15%.

O teclado bluetooth possui um preço de venda de R$ 4.500,00 à vista ou parcelado
em 12% sem juros no cartão de crédito.

Antes de trocar a página de vendas antiga pela nova, o product manager gostaria
de testar a efetividade da nova página em um grupo menor de clientes, a fim de
correr menos riscos de queda da conversão, caso a página nova mostre uma
conversão pior do que a página atual.

## 2. O desafio
Você foi contratado como um freelancer pela Electronic House para ajudar o time de
Designers da nova página, a validar a sua efetividade de uma maneira mais segura,
com mais confiança e rigidez na análise.
Os entregáveis do seu trabalho são os seguintes:

 1. A conversão da nova página é realmente melhor do a conversão da página
atual?
 2. Qual o potencial de número de vendas que a nova página pode trazer?
 3. Qual o faturamento total na venda do teclado bluetooth através da nova página?

## Diferença entre os testes A/B

O teste A/B bayesiano possui diversas vantagens em relação a outros modos neste determinado desafio. Como podemos ver no desenho abaixo:

![testeab_1](https://user-images.githubusercontent.com/55566708/216536937-8bf02489-6566-42be-90ba-1a75f228115d.jpg)

O teste frequentista por todo a fase de testes envia páginas A para um determinado grupo e a B para outro numa taxa de 50% durante toda a duração do experimento. Assim sendo a página que te traz menos retorno irá ser muito enviada e por um tempo bem elevado fazendo com que o retorno financeiro seja menor. Já na Bayseana a transição é mais suave onde o algoritmo aprende em tempo real qual página tende a trazer mais retorno e suavemente vai substituindo a com baixo retorno.

![testeab_2](https://user-images.githubusercontent.com/55566708/216536958-b479bf68-3815-4d2f-9a04-d9ca55fe9f7b.jpg)

Por isso o teste A/B realizado foi a Baysiana.

## 3. Os dados

O conjunto de dados está disponível na plataforma do Kaggle, através desse link:
https://www.kaggle.com/datasets/zhangluyuan/ab-testing?select=ab_data.csv

## 4. Conclusão:

 1. O time de UX designers criaram uma nova página de vendas para um teclado
bluetooth.
 2. Eles gostariam de testar a nova página em um ambiente com menos riscos.
 3. A página de vendas atual tem uma conversão de 13%.
 4. O gerente de produto tem uma meta de conversão de 15% para a nova página.
 5. A empresa gostaria de saber o potencial de vendas e de faturamento da nova
página de vendas.
