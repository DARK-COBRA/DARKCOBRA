from sqlalchemy import Column, String

from . import BASE, SESSION


class Moidata(BASE):
    __tablename__ = "moidata"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Moidata.__table__.create(checkfirst=True)


def add_usersid_in_db(chat_id: int):
    id_user = Moidata(str(chat_id))
    SESSION.add(id_user)
    SESSION.commit()


def get_all_users():
    stark = SESSION.query(Moidata).all()
    SESSION.close()
    return stark


def already_added(chat_id):
    try:
        return SESSION.query(Moidata).filter(Moidata.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()
