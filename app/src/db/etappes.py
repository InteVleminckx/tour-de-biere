from app.models import Session, Etappe, Objectives, Objective


def create_etappe(name: str, objectives: dict):

    session = Session()

    etappe = Etappe(name=name)
    session.add(etappe)
    session.flush()

    for order, (obj_type, category) in objectives.items():
        obj = Objective(objective_type=obj_type, category=category)
        session.add(obj)
        session.flush()
        objs = Objectives(etappe_id=etappe.id, objective_id=obj.id, objective_order=order)
        session.add(objs)
        session.flush()

    session.commit()
    session.close()


if __name__ == '__main__':
    create_etappe("Etappe 1", {
        0: ("climb", "Stella"),
        1: ("sprint", "Stella"),
    })