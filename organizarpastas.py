"""
   Autor: Jackson R B Alfonso
   Data: 04/11/2022
   Objetivo: ORGANIZAR ARQUIVOS DENTRO DA PASTA DE DOWNLOAD, SEPARANDO PELA EXTENSÃO.
"""

import os
import shutil 
from os import path
import pathlib 

pastas_organizacao = ('Documentos', 'Aplicativos', 'Compactados', 'Planilhas', 'PDF', 'Imagens', 'APK', 'OUTROS', 'Videos','Musicas', 'TXT','DEV')
matriz_arquivos = [['Documentos',['DOC', 'DOCX']], ['Aplicativos', ['EXE','MSI']], ['Compactados', ['ZIP','RAR']], ['Planilhas', ['XLS', 'XLSX', 'XLSM']], 
                   ['Imagens',['JPEG','JPG', 'PNG']], ['APK', ['APK']], ['PDF', ['PDF']], ['OUTROS', ['NONE']], ['Videos',['ASF','AVI','MP4','M4V','MOV','MPG','MPEG','WMV']],
                   ['Musicas',['WMA','WAV','M4A','MP4','MP3','MID','MIDI','AU','AIFF']], ['TXT',['TXT']],['DEV',['IPYNB','PY','PSF','DATA','DB']]]

def cria_estrutura_de_organizacao(root_path):
    for items in pastas_organizacao:
        path = os.path.join(root_path, items)

        if  os.path.isdir(path):
            pass
        else:
            os.mkdir(path)

def remove_arquivo_destino(arquivo_remover):
    if os.path.isfile(arquivo_remover):
            os.remove(arquivo_remover)


def move_arquivo(file, root_path, root_destino):
    shutil.move(os.path.join(root_path,file), root_destino)

def busca_destino_extensao(file_extension):
    for pasta, extensao in matriz_arquivos:
        for tipo_arquivo in extensao:
            if file_extension == tipo_arquivo:
                return pasta

def organiza_arquivos_pc(root_path):

    # PERCORRE TUDO O QUE EXISTEM NO DIRETORIO: SUBDIRETORIOS E ARQUIVOS
    for file in os.listdir(root_path):
        d = os.path.join(root_path, file)
        if os.path.isdir(d):
            # SE FOR UM DIRETORIO SÓ PULO NÃO FAÇO NADA
            #print(f'Pasta: {file}')
            pass
        else:
            # SE FOR UM ARQUIVO VALIDOONDE ELE DEVE FICAR E PROCESSO A COPIA E REMOÇÃO PARA NÃO DUPLICAR
            file_extension = pathlib.Path(file).suffix.replace('.','').upper()
            pasta_destino = busca_destino_extensao(file_extension)
            
            # SE ALGUM ARQUIVO NÃO TIVER UM DESTINO MAPEADO, JOGO EM UMA PASTA GENÉRICA - OUTROS
            if pasta_destino == None:
                pasta_destino = 'OUTROS'

            # MOSTRA OS ARQUIVOS ENCONTRADOS COM AS EXTENSÕES E PARA ONDE DEVEM SER COPIADOS
            #print(f'Arquivo: {file} - Extensão: {file_extension} | Pasta de Destino: {pasta_destino}' )

            remove_arquivo_destino(path.join(root_path, pasta_destino)+'\\'+file)
            move_arquivo(file, root_path, path.join(root_path, pasta_destino))
    
    print(f'ROTINA DE ORGANIZAÇÃO DE ARQUIVOS CONCLUIDA')


main_folder = path.join(path.expanduser("~"), "Downloads")
cria_estrutura_de_organizacao(main_folder)
organiza_arquivos_pc(main_folder)
