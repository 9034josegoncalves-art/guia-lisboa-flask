from app import app, db
from app.models import Local

# Cria as tabelas na base de dados (database.db) se ainda nao existirem
with app.app_context():
    db.create_all()

    # Se a tabela dos locais estiver vazia mete os 3 locais que estavam no html
    if Local.query.count() == 0:
        db.session.add(Local(
            nome="Torre de Belém",
            descricao="Construída no século XVI às margens do Rio Tejo, a Torre de Belém é um dos monumentos mais emblemáticos do estilo manuelino e simboliza a era das navegações portuguesas.",
            link="https://pt.wikipedia.org/wiki/Torre_de_Bel%C3%A9m",
            imagem="https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fa/Bel%C3%A9m_Tower_in_Lisbon%2C_Portugal.jpg/330px-Bel%C3%A9m_Tower_in_Lisbon%2C_Portugal.jpg?utm_source=pt.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"
        ))
        db.session.add(Local(
            nome="Castelo de São Jorge",
            descricao="Localizado numa das colinas mais altas de Lisboa, este castelo medieval oferece uma vista panorâmica incrível sobre toda a cidade e o Rio Tejo.",
            link="https://pt.wikipedia.org/wiki/Castelo_de_S%C3%A3o_Jorge",
            imagem="https://thumb.wikimedia.org/wikipedia/commons/thumb/1/17/Castelo_de_S%C3%A3o_Jorge_%2810251035013%29.jpg/330px-Castelo_de_S%C3%A3o_Jorge_%2810251035013%29.jpg?utm_source=pt.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"
        ))
        db.session.add(Local(
            nome="Bairro da Alfama",
            descricao="O bairro mais antigo de Lisboa, famoso pelas ruas estreitas, varandas com roupa a secar e pelo som do Fado a ecoar pelas tavernas.",
            link="https://pt.wikipedia.org/wiki/Alfama",
            imagem="https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c1/Alfama%2C_Lisboa_-_2010-09-09.jpg/250px-Alfama%2C_Lisboa_-_2010-09-09.jpg?utm_source=pt.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"
        ))
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
