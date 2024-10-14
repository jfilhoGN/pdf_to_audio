# PDF para Audio

Python é uma ferramenta completa para inúmeros tipos de atividades, pesquisando um pouco mais das ferramentas que existem encontrei uma forma de gerar audiobooks a partir de um livro PDF, abaixo segue a explicação.

## PDF Plumber

Primeira ferramenta que iremos utilizar é o PDF Plumber seu objetivo é converter PDF para texto, aqui nesse tutorial será usado para realizar a conversão de PDF para texto e posteriormente de Texto para audio com a ferramenta gTTS.

Para converter de PDF para texto usamos essa parte do script

```python
pdf_text = ""

with pp.open("cortico.pdf") as pdf:
    for page in pdf.pages:
        pdf_text += page.extract_text()
```
Cria se uma variável pdf_text usada para armazenar todo o conteúdo textual e posteriormente abrindo o arquivo .pdf varremos cada pagina do arquivo pdf convertendo o mesmo para o texto. Após feito a parte de extração de texto vamos para a parte de traduzir para áudio.

Para converter o texto para áudio é usado a ferramenta GTTS que tem como objetivo converter texto para diversas linguagens, sendo a mais completa o inglês. Aqui no nosso script realizamos a conversão escrevendo as seguintes linhas de código

```python
tts = gTTS(pdf_text, lang="pt")
tts.save("cortico.mp3")
```
Onde iniciamente utilizando a função gTTS varro todo o conteúdo dentro da variável pdp_text e posteriormente salvo o arquivo com a função save passando como parametro o nome que irá ficar o arquivo.

Para ter mais conhecimento das duas ferramentas, abaixo trago a documentação de ambas as ferramentas.

## Documentação

- [PDF Plumber](https://github.com/jsvine/pdfplumber)
- [GTTs](https://gtts.readthedocs.io/en/latest/)