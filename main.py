import requests
import os
import time
from arquivos import links, sorteador
tempo = 5


while True:
    try:
        def download_image(url, caminho_da_pasta):
            try: 
                resposta = requests.get(url)

                if resposta.status_code == 200:

                    filename = os.path.join(caminho_da_pasta, os.path.basename(url))

                    with open(filename, 'wb') as f:

                        f.write(resposta.content)
                    print(f'Imagem Baixada!:{filename}')
                else:
                    print(f'Falha ao baixar a imagem. Statu code:{resposta.status_code}')

            except Exception as e:
                print(f'Erro ao baixar imagem: {e}') 

        if __name__=="__main__":
            url = links.links[sorteador.sorteador()]

            caminho_da_pasta = "C:\\Users\\breno\\Downloads"

            if not os.path.exists(caminho_da_pasta):
                os.makedirs(caminho_da_pasta)

        download_image(url, caminho_da_pasta)

    except Exception as e:
        print(f'Erro Detectado: {e}')
        pass

    time.sleep(tempo)
