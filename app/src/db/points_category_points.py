from app.models import Session, PointsCategoryPoints

def add_points():

    session = Session()

    points = {
        "Stella": [
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
            session.add(PointsCategoryPoints(
                category=category, position=position, points=point
            ))
            session.flush()

    session.commit()
    session.close()

if __name__ == '__main__':
    add_points()