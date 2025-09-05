import os
import sys

def decrypt_file(input_file, output_file=None, key=94):
    """
    Descriptografa os 5000 primeiros bytes do arquivo IMG usando XOR

    Args:
        input_file: Caminho do arquivo de entrada
        output_file: Caminho do arquivo de saída (opcional)
    """
    if not os.path.exists(input_file):
        print(f"Erro: Arquivo '{input_file}' não encontrado!")
        return False

    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_decrypted.img"

    print(f"Descriptografando '{os.path.basename(input_file)}' com chave {key}...")

    try:
        with open(input_file, 'rb') as f_in:
            data = bytearray(f_in.read())

        bytes_to_process = min(5000, len(data))

        for i in range(bytes_to_process):
            data[i] ^= key

        with open(output_file, 'wb') as f_out:
            f_out.write(data)

        print(f"✓ Sucesso! Arquivo descriptografado: {os.path.basename(output_file)}")
        print(f"  Processados {bytes_to_process} bytes do arquivo original de {len(data)} bytes")

        return True

    except Exception as e:
        print(f"✗ Erro durante a descriptografia: {e}")
        return False

def decrypt_directory(directory_path, key=94):
    """
    Descriptografa todos os arquivos .img em um diretório

    Args:
        directory_path: Caminho do diretório
    """

    if not os.path.exists(directory_path):
        print(f"Erro: Diretório '{directory_path}' não encontrado!")
        return False

    if not os.path.isdir(directory_path):
        print(f"Erro: '{directory_path}' não é um diretório!")
        return False

    img_files = []
    for file in os.listdir(directory_path):
        if file.lower().endswith('.img'):
            img_files.append(file)

    if not img_files:
        print(f"Nenhum arquivo .img encontrado no diretório '{directory_path}'")
        return False

    print(f"Encontrados {len(img_files)} arquivo(s) .img:")
    for i, file in enumerate(img_files, 1):
        print(f"  {i}. {file}")

    print(f"\nDescriptografando com chave {key}...")

    success_count = 0
    for file in img_files:
        input_path = os.path.join(directory_path, file)
        output_file = f"{os.path.splitext(file)[0]}_decrypted.img"
        output_path = os.path.join(directory_path, output_file)

        if decrypt_file(input_path, output_path, key):
            success_count += 1

    print(f"\n=== Resultado ===")
    print(f"✓ {success_count}/{len(img_files)} arquivos descriptografados com sucesso")

    return success_count > 0

def show_menu():
    print("\n" + "="*60)
    print("DESCRIPTOGRAFADOR DE ARQUIVOS .IMG DO GITZWC - rizzo")
    print("="*60)
    print("1 - Decryptar todos os .img de um diretório")
    print("2 - Decryptar um arquivo .img específico")
    print("3 - Sair")
    print("="*60)

def main():
    current_key = 94 # chave usada pelo gitzwc até a publicação do script (05 de setembro de 2025)

    while True:
        show_menu()

        try:
            choice = input("\nEscolha uma opção (1-3): ").strip()

            if choice == "1":
                directory = input("Digite o caminho do diretório: ").strip()
                if not directory:
                    directory = "."

                decrypt_directory(directory, current_key)
                input("\nPressione Enter para continuar...")

            elif choice == "2":
                file_path = input("Digite o caminho do arquivo .img: ").strip()

                if not file_path:
                    print("Caminho do arquivo não pode estar vazio!")
                else:
                    output_file = input("Digite o nome do arquivo de saída (ou Enter para automático): ").strip()
                    if not output_file:
                        output_file = None

                    success = decrypt_file(file_path, output_file, current_key)
                    if success:
                        print("\n✓ Arquivo descriptografado com sucesso!")
                    else:
                        print("\n✗ Falha na descriptografia!")

                input("\nPressione Enter para continuar...")

            elif choice == "3":
                break

            else:
                print("Opção inválida! Digite um número de 1 a 3.")
                input("Pressione Enter para continuar...")

        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
