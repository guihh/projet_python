Projet_Python
===========

Pour lancer :

    git clone https://github.com/guihh/projet_python.git
    cd projet_python/
    sudo docker-compose up

Pour accéder à un des containers de ton choix {projet_db_1|projet_web_1|projet_web_geoalchemy_1}

    sudo docker exec -t -i {choix} /bin/bash

Pour accéder à la classe qui contient les tests :

    - projet_web_1 :

    python manage.py shell
    from limitesCommunes import load
    load.run() #Ajoute le fichier shape ds la DB
    load.test_{add()|delete()|update()|contains()|intersects()|lenght()|export_communes_json()}

    - projet_web_geoalchemy :

    python3
    import webgeoalchemy
    load = webgeoalchemy.run()
    load.test_{add()|delete()|update()|contains()|intersects()|perimeter()}

Il existe 2 objets limitescommunes multipolygon, stockées dans la classe nogentSurSeine & champsSurMarne, et également 1 objet multipoint, nommé prefec, pour faire les tests avec les méthodes du dessus.
