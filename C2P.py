import os
import subprocess

def main():
    print("="*45)
    print("      SKB CODE2PKG - ORQUESTRADOR FINAL")
    print("="*45)

    # 1. LOCALIZAR PROJETOS
    # Lista apenas pastas, ignorando arquivos e a pasta oculta do git
    pastas = [f for f in os.listdir('.') if os.path.isdir(f) and not f.startswith('.')]
    
    if not pastas:
        print("[!] Nenhuma pasta de projeto encontrada aqui!")
        print("[*] Dica: Crie uma pasta para o seu projeto antes de rodar.")
        return

    print("\nProjetos disponíveis:")
    for i, pasta in enumerate(pastas):
        print(f"  [{i}] {pasta}")

    # 2. SELEÇÃO DA PASTA
    try:
        escolha = input("\n-> Selecione o número ou nome da pasta: ").strip()
        if escolha.isdigit():
            pasta_alvo = pastas[int(escolha)]
        else:
            pasta_alvo = escolha

        if not os.path.exists(pasta_alvo):
            print(f"[!] Erro: A pasta '{pasta_alvo}' não existe.")
            return
    except Exception as e:
        print(f"[!] Entrada inválida: {e}")
        return

    print(f"\n[*] Alvo selecionado: {pasta_alvo}")

    # 3. DADOS DO PARAM.SFO (TITLE e ID)
    nome_app = input(f"-> Nome do App no PS3 (Enter para '{pasta_alvo}'): ") or pasta_alvo
    title_id = input("-> Title ID (Ex: SKB00001): ").strip() or "SKB00001"

    # 4. CRIAÇÃO DA ESTRUTURA (Se não existir)
    caminho_usrdir = os.path.join(pasta_alvo, "USRDIR")
    os.makedirs(caminho_usrdir, exist_ok=True)

    # 5. EXECUÇÃO DOS MÓDULOS SEPARADOS
    # Chamando o SFO_GEN
    print(f"\n[*] Gerando PARAM.SFO em {pasta_alvo}...")
    # Passamos os argumentos: NOME, ID e PASTA DESTINO
    subprocess.run(["python", "sfo_gen.py", nome_app, title_id, pasta_alvo])

    # Procurando o binário (ELF) para gerar o EBOOT
    # O script tenta achar um .elf dentro da pasta ou usa um padrão
    elf_path = os.path.join(pasta_alvo, "main.elf")
    if os.path.exists(elf_path):
        print(f"[*] Gerando EBOOT.BIN selado...")
        subprocess.run(["python", "eboot_gen.py", elf_path, pasta_alvo])
    else:
        print(f"[!] Aviso: 'main.elf' não encontrado em {pasta_alvo}. Pulando EBOOT.")

    print("\n" + "="*45)
    print(f" [✔] PROCESSO CONCLUÍDO PARA: {pasta_alvo}")
    print(f" [!] Estrutura USRDIR e PARAM.SFO prontos.")
    print("="*45)

if __name__ == "__main__":
    main()
