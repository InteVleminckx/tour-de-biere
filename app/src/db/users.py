from app.models import Session, Users, GeneralClassification, PointsClassification, PolkaClassification

def create_user(name: str):
    session = Session()
    user = Users(name=name)
    session.add(user)
    session.flush()

    gc = GeneralClassification(user_id=user.id)
    pc = PointsClassification(user_id=user.id)
    polka = PolkaClassification(user_id=user.id)

    session.add_all([gc, pc, polka])
    session.commit()
    session.close()

    return user


def delete_user(name: str):
    session = Session()
    try:
        # Find the user by name
        user = session.query(Users).filter_by(name=name).first()

        if not user:
            print(f"No user found with name '{name}'")
            return False

        session.delete(user)
        session.commit()
        print(f"User '{name}' and all related classifications deleted.")
        return True
    except Exception as e:
        session.rollback()
        print(f"Error deleting user '{name}': {e}")
        return False
    finally:
        session.close()

def _create_users(names: list[str]):
    for name in names:
        create_user(name)

def _delete_users(names: list[str]):
    for name in names:
        delete_user(name)

def _reset_users(names: list[str]):
    _delete_users(names)
    _create_users(names)

if __name__ == "__main__":
    users = ["Inte", "Ab"]
    _create_users(users)