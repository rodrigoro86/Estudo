# DASH

### Instalalção 
`pip install dash`

### 1° Código 

```
from dash import Dash
from dash_html_components import H1

app = Dash(__name__)

app.layout=H1('Boas vindas')

app.run_server(debug=True)
```  

## DHC - Dash HTML Components
Existem duas formas de usar CSS no Dash. Uma delas é usando um arquivo CSS local:  
Deve adicionar ele em /assets/style.css  
Outra froma é usar links de estilo externos:  
`app = Dash(__name__,external_stylesheets=external_stylesheets)`  

## DCC - Dash Core Components 
Os core components são os componentes base para interação. 
- Um campo de texto.  
- Um campo de seleção.  
- Um campo de escolha.  
