import subprocess
import sys

# Lista com os nomes dos arquivos dos scripts das práticas
arquivos = ["3_1.py", "3_2.py", "3_3.py", "4_1.py", "4_2.py"]

for arquivo in arquivos:
  print(f"\n--- Executando: {arquivo} ---")
  try:
    # Executa cada script usando o interpretador Python atual
    resultado = subprocess.run(
        [sys.executable, arquivo], check=True, text=True
    )
    print(f"[{arquivo}] Executado com sucesso!")
  except subprocess.CalledProcessError as e:
    print(f"Erro ao executar {arquivo}: {e}")
  except FileNotFoundError:
    print(
        f"Arquivo '{arquivo}' não encontrado. Verifique se ele está na mesma"
        " pasta."
    )

print("\n--- Todos os scripts foram processados! ---")