from app.models import Session, PolkaCategoryPoints

def add_points():

    session = Session()

    points = {
        "Meas": [
            50,
            30,
            20,
        ],
        "Duvel": [
            60,
            40,
            25,
        ]
    }

    for category, values in points.items():
        for position, point in enumerate(values):
            session.add(PolkaCategoryPoints(
                category=category, position=position, points=point
            ))
            session.flush()

    session.commit()
    session.close()

if __name__ == '__main__':
    add_points()
