import PySimpleGUI as pg


jogador = "X"
x_o = ""
pt_x = 0
pt_o = 0
vez = True
layout = [
    [pg.Text(f"É a vez do jogador: {jogador}", key="jg")],
    [pg.Button(f"{x_o}", size=(10, 5), key="bt1"), pg.Button(f"{x_o}", size=(10, 5), key="bt2"), pg.Button(f"{x_o}", size=(10, 5), key="bt3")],
    [pg.Button(f"{x_o}", size=(10, 5), key="bt4"), pg.Button(f"{x_o}", size=(10, 5), key="bt5"), pg.Button(f"{x_o}", size=(10, 5), key="bt6"), pg.Button("Resetar", size=(7, 3), key="reset")],
    [pg.Button(f"{x_o}", size=(10, 5), key="bt7"), pg.Button(f"{x_o}", size=(10, 5), key="bt8"), pg.Button(f"{x_o}", size=(10, 5), key="bt9")],
    [pg.Text(f"Pontuação X: {pt_x}", key="ptx"), pg.Button("+1", key="M1X"), pg.Button("-1", key="ME1X")],
    [pg.Text(f"Pontuação O: {pt_o}", key="pto"), pg.Button("+1", key="M1O"), pg.Button("-1", key="ME1O")]
]
janela = pg.Window("Jogo da velha", layout, size=(500, 500))


while True:
    event, values = janela.read()
    if event == pg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == "reset":
        for i in range(9):
            i += 1
            janela[f"bt{i}"].update("")


    if event == "M1X":
        pt_x += 1
        janela["ptx"].update(f"Pontuação X: {pt_x}")

    if event == "ME1X":
        pt_x -= 1
        janela["ptx"].update(f"Pontuação X: {pt_x}")

    if event == "M1O":
        pt_o += 1
        janela["pto"].update(f"Pontuação X: {pt_o}")

    if event == "ME1O":
        pt_o -= 1
        janela["pto"].update(f"Pontuação X: {pt_o}")

    if vez:
        jogador = "O"

        janela["jg"].update(f"É a vez do jogador: {jogador}")
        if event == "bt1":
            janela["bt1"].update("x")
            vez = False

        if event == "bt2":
            janela["bt2"].update("x")
            vez = False

        if event == "bt3":
            janela["bt3"].update("x")
            vez = False

        if event == "bt4":
            janela["bt4"].update("x")
            vez = False

        if event == "bt5":
            janela["bt5"].update("x")
            vez = False

        if event == "bt6":
            janela["bt6"].update("x")
            vez = False

        if event == "bt7":
            janela["bt7"].update("x")
            vez = False

        if event == "bt8":
            janela["bt8"].update("x")
            vez = False

        if event == "bt9":
            janela["bt9"].update("x")
            vez = False

    else:
        jogador = "X"

        janela["jg"].update(f"É a vez do jogador: {jogador}")
        if event == "bt1":
            janela["bt1"].update("o")
            vez = True

        if event == "bt2":
            janela["bt2"].update("o")
            vez = True

        if event == "bt3":
            janela["bt3"].update("o")
            vez = True

        if event == "bt4":
            janela["bt4"].update("o")
            vez = True

        if event == "bt5":
            janela["bt5"].update("o")
            vez = True

        if event == "bt6":
            janela["bt6"].update("o")
            vez = True

        if event == "bt7":
            janela["bt7"].update("o")
            vez = True

        if event == "bt8":
            janela["bt8"].update("o")
            vez = True

        if event == "bt9":
            janela["bt9"].update("o")
            vez = True



janela.close()

