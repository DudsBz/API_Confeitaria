from conexao import get_conexao


def get_cardapio():
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cardapio;")
    cardapio = cursor.fetchall()
    cursor.close()
    conn.close()

    return cardapio
    