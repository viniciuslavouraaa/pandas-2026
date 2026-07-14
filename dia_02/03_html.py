# %%
import pandas as pd
import requests

# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

resposta = requests.get(url, headers=headers)
resposta.raise_for_status()

dfs = pd.read_html(resposta.text)
dfs