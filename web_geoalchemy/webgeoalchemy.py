from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.session import make_transient
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Sequence

from geoalchemy2.functions import ST_Perimeter , ST_Intersects , ST_Contains, ST_DWithin, ST_Transform  
from geoalchemy2 import Geometry

from timeit import default_timer as timer

import statistics

Base = declarative_base()

class Limitescommune(Base):
    __tablename__ = 'limitesCommunes_limitescommunes'
    id = Column('id', Sequence('{table}_id_seq'.format(table=__tablename__)), primary_key=True, nullable=False)
    id_geofla =Column('id_geofla',String(24))
    code_com = Column('code_com',String(3))
    insee_com = Column('insee_com',String(5))
    nom_com = Column('nom_com',String(50))
    statut = Column('statut',String(25))
    x_chf_lieu = Column('x_chf_lieu', Integer)
    y_chf_lieu = Column('y_chf_lieu', Integer)
    x_centroid = Column('x_centroid', Integer)
    y_centroid = Column('y_centroid', Integer)
    z_moyen = Column('z_moyen', Integer)
    superficie = Column('superficie', Float)
    population = Column('population', Float)
    code_arr = Column(String(1))
    code_dept = Column(String(2))
    nom_dept = Column(String(30))
    code_reg = Column(String(2))
    nom_reg = Column(String(35))
    geom = Column(Geometry(geometry_type='MULTIPOLYGON'))


class Prefectures(Base):
    __tablename__ = "limitesCommunes_prefectures"
    id = Column('id', Sequence('{table}_id_seq'.format(table=__tablename__)), primary_key=True, nullable=False)
    gml_id = Column('gml_id',String(100))
    gid = Column('gid', Integer)
    insee_commune = Column('insee_commune',String(100))
    nom_commune = Column('nom_commune',String(100))
    type = Column('type',String(100))
    geom = Column(Geometry(geometry_type='MULTIPOINT'))

class run():
    
    engine = create_engine('postgresql://postgres:postgres@db/postgres', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()


    nogentSurSeine = Limitescommune(
    id_geofla = "COMMUNE11111111111111111",
    code_com = "888",
    insee_com = "88888",
    nom_com = "NOGENT-SUR-SEINE",
    statut = "Commune simple",
    x_chf_lieu = 670782,
    y_chf_lieu = 6861478,
    x_centroid = 670247,
    y_centroid = 68611277,
    z_moyen = 74,
    superficie = 780,
    population = 24913,
    code_arr = 5,
    code_dept = 77,
    nom_dept = "AUBE",
    code_reg = 11,
    nom_reg = "CHAMPAGNE-ARDENNES",
    geom = "SRID=2154;MULTIPOLYGON(((739256.19999999296851456 6823042.70000104419887066, 739039.69999999296851456 6822961.60000104364007711, 738923.19999999296851456 6822897.70000104419887066, 738792.19999999296851456 6822769.80000104382634163, 738684.09999999310821295 6822635.8000010447576642, 738616.29999999317806214 6822531.50000104308128357, 738855.39999999303836375 6821735.00000104680657387, 738954.99999999301508069 6821226.40000104904174805, 738710.59999999299179763 6820918.20000104885548353, 738472.39999999315477908 6820528.00000104960054159, 738490.49999999313149601 6820309.00000105239450932, 738725.29999999306164682 6819948.20000105164945126, 738659.09999999299179763 6819915.80000105313956738, 738329.79999999317806214 6819832.60000105202198029, 737978.29999999317806214 6819782.10000105202198029, 737034.09999999334104359 6819666.00000105332583189, 736381.09999999334104359 6819477.20000105258077383, 735594.9999999935971573 6819109.10000105388462543, 735712.29999999364372343 6818771.3000010559335351, 735150.49999999371357262 6818597.70000105444341898, 735091.39999999373685569 6818774.70000105537474155, 735001.39999999373685569 6819324.20000105444341898, 734929.49999999371357262 6819680.50000105239450932, 734911.19999999366700649 6819764.60000105295330286, 734848.49999999371357262 6820039.00000105146318674, 734637.69999999366700649 6820162.70000105258077383, 734206.49999999382998794 6820392.80000105034559965, 733980.49999999394640326 6820564.00000104960054159, 733894.39999999396968633 6820654.70000105071812868, 733888.39999999396968633 6820660.70000105071812868, 733844.29999999399296939 6820763.00000105053186417, 733801.29999999399296939 6820874.3000010484829545, 733772.79999999399296939 6821047.50000104866921902, 733797.99999999394640326 6821190.20000104885548353, 733830.79999999399296939 6821295.80000104662030935, 733862.29999999399296939 6821355.50000104960054159, 733897.49999999394640326 6821376.20000104699283838, 733932.49999999394640326 6821375.90000104904174805, 734519.29999999387655407 6821641.80000104662030935, 734954.59999999369028956 6821941.90000104624778032, 735084.89999999373685569 6822218.60000104550272226, 735171.99999999371357262 6822329.60000104364007711, 735173.79999999376013875 6822331.8000010447576642, 735766.29999999364372343 6823090.80000104382634163, 736339.89999999350402504 6823660.70000104047358036, 736966.09999999334104359 6824435.60000103805214167, 737617.49999999324791133 6824722.60000103712081909, 737723.69999999320134521 6824752.60000103898346424, 737747.59999999322462827 6824748.4000010397285223, 737805.69999999320134521 6824758.90000103879719973, 737855.8999999932711944 6824791.50000103935599327, 737893.69999999320134521 6824882.10000103712081909, 737905.49999999324791133 6824984.00000103749334812, 737900.79999999329447746 6825065.50000103656202555, 737896.69999999320134521 6825121.90000103786587715, 738005.59999999322462827 6825239.00000103749334812, 738177.59999999322462827 6825364.400001036003232, 738274.99999999324791133 6825420.60000103618949652, 738634.49999999313149601 6825507.50000103656202555, 738724.49999999313149601 6825509.70000103581696749, 738801.19999999308492988 6825491.10000103525817394, 738843.89999999315477908 6825447.70000103674829006, 738893.19999999308492988 6825369.30000103730708361, 738925.39999999303836375 6825162.20000103767961264, 738960.99999999313149601 6825119.90000103879719973, 738931.09999999310821295 6825016.20000103767961264, 738929.49999999301508069 6824938.30000103823840618, 738965.79999999306164682 6824858.10000103712081909, 739115.39999999303836375 6823523.60000104270875454, 739256.19999999296851456 6823042.70000104419887066)))"
    )   
    
    champsSurMarne = Limitescommune(
    id_geofla = "COMMUNE10000000000000000",
    code_com = "999",
    insee_com = "99999",
    nom_com = "CHAMPS-SUR-MARNE",
    statut = "Commune simple",
    x_chf_lieu = 670782,
    y_chf_lieu = 6861478,
    x_centroid = 670247,
    y_centroid = 68611277,
    z_moyen = 74,
    superficie = 780,
    population = 24913,
    code_arr = 5,
    code_dept = 77,
    nom_dept = "SEINE-ET-MARNE",
    code_reg = 11,
    nom_reg = "ILE-DE-FRANCE",
    geom = "SRID=2154;MULTIPOLYGON( ((668729.4000000050291419 6861567.20000093337148428, 669030.60000000498257577 6861734.50000093225389719, 669413.60000000486616045 6861988.70000093244016171, 669651.00000000488944352 6862299.00000093225389719, 669753.90000000491272658 6862653.90000093076378107, 669725.50000000488944352 6862834.00000093039125204, 669725.60000000486616045 6862854.00000093039125204, 669805.40000000491272658 6862833.40000093076378107, 669855.40000000479631126 6862832.9000009298324585, 669905.50000000488944352 6862852.50000092945992947, 670055.90000000479631126 6862908.70000092964619398, 670186.20000000472646207 6862955.100000092908740044, 670331.50000000477302819 6863003.80000092927366495, 670481.80000000481959432 6863047.50000093039125204, 670516.80000000481959432 6863047.20000092871487141, 670592.50000000477302819 6863021.60000092908740044, 670657.30000000481959432 6862996.100000092908740044, 670627.40000000479631126 6862960.50000092852860689, 670725.700000004610004674 6862810.60000092908740044, 670898.40000000467989594 6862564.20000093244016171, 671037.200000004610004674 6862427.80000093020498753, 671121.60000000463332981 6862351.60000093001872301, 671196.00000000465661287 6862286.00000093132257462, 671476.90000000456348062 6861818.90000093169510365, 671565.00000000454019755 6861308.50000093318521976, 671573.70000000449363142 6860855.20000093523412943, 671480.200000004610004674 6860126.40000093821436167, 671407.50000000465661287 6859034.20000093895941973, 671407.100000000463332981 6858994.20000094175338745, 671247.50000000465661287 6859020.50000094156712294, 670943.200000004610004674 6859088.00000094063580036, 670489.60000000474974513 6859222.80000094044953585, 670056.00000000488944352 6859351.30000093951821327, 669791.60000000486616045 6859408.50000093970447779, 669630.90000000491272658 6859434.900000941000832939, 669621.100000000486616045 6859459.90000093821436167, 669236.50000000500585884 6860364.000000936910510006, 668753.80000000505242497 6861502.00000093411654234, 668729.4000000050291419 6861567.20000093337148428)))"
    )
    
    prefect = Prefectures(
    gml_id = "testprefect",
    gid = 1000,
    insee_commune = "prefect",
    nom_commune = "prefect",
    type = "POINT",
    geom = "SRID=2154;MULTIPOINT(669745.8 6860174.2)"
    )
    
    def test_add(self,commune,ntimes=1000):
        '''
        Mesure le temps pour ajouter un objet dans la base puis le supprime
        '''
        delta = []
        for i in range(ntimes):
            # Ajout d'une nouvelle instance de commune a session  
            make_transient(commune)

            start = timer()  
            self.session.add(commune)
            self.session.commit()
            end = timer()
            
            tmp = self.session.query(Limitescommune).filter(Limitescommune.id_geofla == commune.id_geofla).all()
            #Il peut y avoir plusieurs fois un objet avec le mm id geofla, pres plusieurs test donc on fait une boucle sur le resultat
            for c in tmp:
                self.session.delete(c)
            self.session.commit()
            delta.append(abs(start-end))
        print("Moyenne : "+str(statistics.mean(delta))+" secondes et écart-type : "+str(statistics.pstdev(delta))+" secondes")
    
    def test_delete(self,commune,ntimes=1000):
        '''
        Ajoute puis mesure le temps de suppression d'un objet dans une base
        '''
        delta = []
        for i in range(ntimes):
            # Ajout d'une nouvelle instance de commune a session  
            make_transient(commune)
            self.session.add(commune)
            self.session.commit()
            
            start = timer()  
            self.session.delete(commune)
            self.session.commit()
            end = timer()
            
        
            delta.append(abs(start-end))
        print("Moyenne : "+str(statistics.mean(delta))+" secondes et écart-type : "+str(statistics.pstdev(delta))+" secondes")
        
    def test_update(self,commune1,commune2,ntimes=1000):
        '''
        Mesure le temps de modification d'un objet dans une base. Echange la geometrie une fois sur 2.
        '''
        delta = []
        for i in range(ntimes):
            # Ajout d'une nouvelle instance de commune a session  
            make_transient(commune1)
            if (i%2): 
                start = timer()
                self.session.query(Limitescommune).filter(Limitescommune.id_geofla == commune1.id_geofla).update({"geom": commune2.geom}, synchronize_session='fetch')
                self.session.commit()
                end = timer()
                delta.append(abs(start-end))
            else :
                start = timer()
                self.session.query(Limitescommune).filter(Limitescommune.id_geofla == commune2.id_geofla).update({"geom": commune1.geom}, synchronize_session='fetch')
                self.session.commit()
                end = timer()
                delta.append(abs(start-end))
        print("Moyenne : "+str(statistics.mean(delta))+" secondes et écart-type : "+str(statistics.pstdev(delta))+" secondes")
    
    def test_perimeter(self,commune,ntimes=1000):
        '''
        Mesure le temps pour calculer le perimetre d'un multipolygon depuis la base de donnees
        '''
        delta = []
        for i in range(ntimes):
            start = timer()
            self.session.query(ST_Perimeter(commune.geom))
            end = timer()
            delta.append(abs(start-end))
        print("Moyenne : "+str(statistics.mean(delta))+" secondes et écart-type : "+str(statistics.pstdev(delta))+" secondes")
        
    def test_intersects(self,point,commune,ntimes=1000):
        '''
        Mesure le temps pour calculer une intersection d'un multipolygon depuis la base de donnees
        '''
        delta = []
        for i in range(ntimes):
            start = timer()
            self.session.query(ST_Intersects(point.geom,commune.geom))
            end = timer()
            delta.append(abs(start-end))
        print("Moyenne : "+str(statistics.mean(delta))+" secondes et écart-type : "+str(statistics.pstdev(delta))+" secondes")
    
    def test_contains(self,commune,point,ntimes=1000):
        '''
        Mesure le temps pour calculer si une commune contient un point d'un multipolygon depuis la base de donnees
        '''
        delta = []
        for i in range(ntimes):
            start = timer()
            self.session.query(ST_Contains(commune.geom,point.geom))
            end = timer()
            delta.append(abs(start-end))
        print("Moyenne : "+str(statistics.mean(delta))+" secondes et écart-type : "+str(statistics.pstdev(delta))+" secondes")
    
    def test_dwithin(self,commune,point,ntimes=1000):
        '''
        Ajoute puis mesure le temps de suppression d'un objet dans une base
        '''
        delta = []
        for i in range(ntimes):
            start = timer()
            self.session.query(ST_Contains(commune.geom,point.geom))
            end = timer()
            delta.append(abs(start-end))
        print("Moyenne : "+str(statistics.mean(delta))+" secondes et écart-type : "+str(statistics.pstdev(delta))+" secondes")

if __name__ == '__main__':
    pass
    #~ test = load()
    #~ test.test_add(test.nogentSurSeine)
    #~ test_delete(nogentSurSeine)
    #~ test_update(nogentSurSeine,champsSurMarne)
    #~ test_perimeter(nogentSurSeine)
    #~ test_intersects(prefect,nogentSurSeine)
    #~ test_contains(nogentSurSeine,prefect)   
