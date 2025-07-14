import random
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
from inventario import herois_lista, viloes_lista
from rich.progress import Progress, BarColumn, TextColumn
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()
historico = []

'''
Opção do historico das ações fetias dentro do jogo
'''
def exibir_historico():
    print("\nHistorio do Jogo")
    for acao in historico:
        print(acao)
        print("****************************************************************************\n")


'''
Barras de Vida
'''
def barras_vida(heroi, vilao, vida_max_heroi, vida_max_vilao):
    progress = Progress(
        TextColumn("[bold]{task.description}"),
        BarColumn(bar_width=None),
        TextColumn("[green]{task.fields[life]}"),
    )
    
    with progress:
        task_heroi = progress.add_task(f"[red]{heroi.nome}", total=vida_max_heroi, completed=heroi.vida, life=f"Vida: {heroi.vida}/{vida_max_heroi}")
        task_vilao = progress.add_task(f"[blue]{vilao.nome}", total=vida_max_vilao, completed=vilao.vida, life=f"Vida: {vilao.vida}/{vida_max_vilao}")
        
        progress.update(task_heroi, completed=heroi.vida)
        progress.update(task_vilao, completed=vilao.vida)


def main():
    while True:
        '''
        Tela Inicial contendo as opções
        '''
        console.print(
            Panel.fit(
                "[bold]Selecione uma opção: \n"
                "1. Iniciar Novo Jogo\n"
                "2. Ver Historico\n"
                "3. Sair",
                title="[bold magenta] Menu Principal[/]", border_style="green", box=box.ROUNDED
                ),
                justify="center"
        )
        escolha = input("Escolha uma opção: ").strip()


        '''
        Bloco de seleção dos personagens usando enumerate pra enumerar os personganes facilitando a escolha
        '''
        if escolha == "1":
            heroi_selecionado_dados = None
            while heroi_selecionado_dados is None:
                console.print(
                    Panel.fit(
                        "\n".join(f"{i+1}. {h['nome']} (Vida: {h['vida']})" for i, h in enumerate(herois_lista)), title="[bold blue]Seleção de Herois[/]", border_style="blue"
                    ), justify="center"
                )
                print("Player 1 escolha seu heroi.")

                heroi_selecionado = input("Escolha um heroi: ").strip()

                indice_heroi = int(heroi_selecionado) - 1
                if 0 <= indice_heroi < len(herois_lista):
                    heroi_selecionado_dados = herois_lista[indice_heroi]
                else:
                    print('Escolha invalida!')


            vilao_selecionado_dados = None
            while vilao_selecionado_dados is None:
                console.print(
                    Panel.fit(
                        "\n".join(f"{i+1}. {v['nome']} (Vida: {v['vida']})" for i, v in enumerate(viloes_lista)),
                        title="[bold red]Seleção de Vilões[/]",
                        border_style="red"
                    ),
                    justify="center")
                
                vilao_selecionado = input("Escolha um heroi: ").strip()

                indice_vilao = int(vilao_selecionado) - 1
                if 0 <= indice_vilao < len(viloes_lista):
                    vilao_selecionado_dados = viloes_lista[indice_vilao]
                else:
                    print('Escolha invalida!')

            
            if heroi_selecionado_dados['tipo'] == 'Heroi':
                heroi = Heroi(heroi_selecionado_dados['nome'],
                heroi_selecionado_dados['idade'],
                heroi_selecionado_dados['vida'],
                heroi_selecionado_dados['ataque'],
                heroi_selecionado_dados['defesa'])
            else:
                heroi = Personagem(
                    heroi_selecionado_dados['nome'],
                    heroi_selecionado_dados['idade'],
                    heroi_selecionado_dados['vida']
                )


            if vilao_selecionado_dados['tipo'] == 'Vilao':
                vilao = Vilao(vilao_selecionado_dados['nome'],
                vilao_selecionado_dados['idade'],
                vilao_selecionado_dados['vida'],
                vilao_selecionado_dados['ataque'],
                vilao_selecionado_dados['defesa'])
            else:
                vilao = Personagem(
                    vilao_selecionado_dados['nome'],
                    vilao_selecionado_dados['idade'],
                    vilao_selecionado_dados['vida']
                )


            print('Iniciando jogo...')
            print(f"Personagens escolhidos: {heroi} vs {vilao}")

            counter_rodads = 1
            while heroi.vida > 0 and vilao.vida > 0:
                print(f"- Rodada {counter_rodads} -")
                (heroi, vilao, heroi_selecionado_dados['vida'], vilao_selecionado_dados['vida'])

                aleatory_numero = random.randint(1, 2)
                if aleatory_numero == 1:
                    print(f"\n- Turno de {heroi.nome} -")
                    action = input("Insira sua ação (atacar, defender, cura, poção): ")
                    if action == 'atacar':
                        heroi.atacar(vilao)
                        heroi.dialogar('ataque')
                    elif action == 'defender':
                        heroi.defesa += 5
                        heroi.dialogar('defesa')
                    elif action == 'cura':
                        heroi.cura()
                        heroi.dialogar('cura')
                    elif action == 'pocao':
                        heroi.usar_pocao()
                        print('Fortificando golpe!')
                    else:
                        print('Ação invalida! você perdeu o turno.')
                else:
                    print(f"\n- Turno de {vilao.nome} -")
                    action = input("Insira sua ação (atacar, defender, cura, maldicao): ")
                    if action == 'atacar':
                        vilao.atacar(heroi)
                        vilao.dialogar('ataque')
                    elif action == 'defender':
                        vilao.defesa += 5
                        vilao.dialogar('defesa')
                    elif action == 'cura':
                        vilao.cura()
                        vilao.dialogar('cura')
                    elif action == 'maldicao':
                        vilao.maldicao()
                        print('Enfermidades aqueles que ousam contra mim!')
                    else:
                        print('Ação invalida! você perdeu o turno.')
                    
                
                if heroi.vida <= 0:
                    print(f"{heroi.nome} foi derrotado! {vilao.nome} venceu o jogo!")
                    print(f"{heroi.nome}:", end='')
                    heroi.dialogar('morte')
                elif vilao.vida <= 0:
                    print(f"{vilao.nome} foi derrotado! {heroi.nome} venceu o jogo!")
                    print(f"{vilao.nome}:", end='')
                    vilao.dialogar('morte')

                    

                eventos_jogo = f"Rodada {counter_rodads}: {heroi.nome if aleatory_numero == 1 else vilao.nome} usou {action}"
                historico.append(eventos_jogo)
                counter_rodads += 1


            print('Fim de jogo!')
        elif escolha == "2":
            exibir_historico()
        elif escolha == "3":
            print("Saindo do jogo... See u <3")
            break
        else:
            print('Opção invalida. try again :)')





if __name__ == "__main__":
    main()
