import os
from tempfile import NamedTemporaryFile
from fastapi import UploadFile

async def save_upload_file(upload_file: UploadFile, destination_folder: str = "temp") -> str:
    """
    Salva o arquivo enviado em uma pasta temporária.

    Parâmetros:
    - upload_file (UploadFile): Arquivo recebido pelo endpoint.
    - destination_folder (str): Pasta onde o arquivo será salvo.

    Retorna:
    - str: Caminho completo do arquivo salvo.
    """
    # Criar a pasta de destino, se não existir
    os.makedirs(destination_folder, exist_ok=True)

    # Criar um arquivo temporário dentro da pasta de destino
    temp_file_path = os.path.join(destination_folder, upload_file.filename)
    
    try:
        # Salvar o conteúdo do arquivo
        with open(temp_file_path, "wb") as temp_file:
            content = await upload_file.read()
            temp_file.write(content)
    finally:
        await upload_file.close()

    return temp_file_path
