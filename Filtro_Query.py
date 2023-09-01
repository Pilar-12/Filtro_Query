#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn Filtro_Query:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: User

class moto(BaseModel):
    codigo:int
    marca: str
    modelo:str
    año:int
    precio:int
    tipo:str
    transmicion:str
    

motos_list=[

    moto(codigo=1, marca="Gottlieb", modelo="Daimler Reitwagen", año="1885", precio="10000", tipo="Snowmobile", transmicion="automatica"),
    moto(codigo=2, marca="Flying Merkel", modelo="Model V", año="1911", precio="10001", tipo="Trail", transmicion="semiautomatica"),
    moto(codigo=3, marca="Harley Davidson", modelo="Modelo 7D", año="1911", precio="10002", tipo="Dirt", transmicion="estandar"),
    moto(codigo=4, marca="Peugeot", modelo="Paris Nice", año="1913", precio="10003", tipo="Moped", transmicion="automatica"),
    moto(codigo=5, marca="Indian", modelo="Valve Board", año="1915", precio="10004", tipo="Adventure", transmicion="semiautomatica"),
    moto(codigo=6, marca="Megola ", modelo="Sport", año="1920", precio="10005", tipo="Bobber", transmicion="estandar"),
    moto(codigo=7, marca="Bmw", modelo="R32", año="1923", precio="10006", tipo="Atv", transmicion="automatica"),
    moto(codigo=8, marca="Bohmerland", modelo="Model 598", año="1925", precio="10007", tipo="Sports", transmicion="semiautomatica"),
    moto(codigo=9, marca="Ariel Square Four", modelo="MK", año="1931", precio="10008", tipo="Naked", transmicion="estandar"),
    moto(codigo=10, marca="Indian", modelo="Sport Scout", año="1934", precio="10009", tipo="Sports Touring", transmicion="automatica"),
    moto(codigo=11, marca="Triumph", modelo="Speed Twin", año="1938", precio="10011", tipo="Touring", transmicion="semiautomatica"),
    moto(codigo=12, marca="Vespa", modelo="Gts", año="1946", precio="10012", tipo="Chopper", transmicion="estandar"),
    moto(codigo=13, marca="Solex ", modelo="Velosolex", año="1946", precio="10013", tipo="Cruiser", transmicion="automatica"),
    moto(codigo=14, marca="Gilera", modelo="Saturno", año="1947", precio="10014", tipo="Cafe Racer", transmicion="semiautomatica"),
    moto(codigo=15, marca="Indian", modelo="Chief", año="1948", precio="10015", tipo="Classic", transmicion="estandar"),
    moto(codigo=16, marca="BSA", modelo="Gold Star", año="1952", precio="10016", tipo="Commuter", transmicion="automatica"),
    moto(codigo=17, marca="Montesa ", modelo="Brio 90", año="1953", precio="10017", tipo="Scooter", transmicion="semiautomatica"),
    moto(codigo=18, marca="Vespa", modelo="Gs", año="1955", precio="10018", tipo="Snowmobile", transmicion="estandar"),
    moto(codigo=19, marca="Vespa", modelo="180SS", año="1911", precio="10019", tipo="Trail", transmicion="automatica"), 
    moto(codigo=20, marca="Montesa", modelo="Cappra", año="1944", precio="10021", tipo="Dirt", transmicion="semiautomatica"),
    moto(codigo=21, marca="Montesca", modelo="Enduro", año="1944", precio="10021", tipo="Moped", transmicion="semiautomatica"),
    #-------
    moto(codigo=22, marca="Harley Davidson", modelo="Sportster XL", año="1957", precio="10022", tipo="Adventure", transmicion="automatica"),
    moto(codigo=23, marca="Honda", modelo="Super club", año="1991", precio="10023", tipo="Bobber", transmicion="semiautomatica"),
    moto(codigo=24, marca="Triumph", modelo="Bonneville", año="1958", precio="10024", tipo="Atv", transmicion="estandar"),                                                                       
    moto(codigo=25, marca="Harley Davidson", modelo="Duo Glide", año="1997", precio="10002", tipo="Trail", transmicion="automatica"),
    # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos9/?año=1997&precio=10002&tipo=Trail&transmicion=autonamtica&marca=Harley Davidson
    moto(codigo=26, marca="Bultaco", modelo="Tralla", año="1959", precio="10026", tipo="Naked", transmicion="semiautomatica"),
    moto(codigo=27, marca="Honda", modelo="CB", año="1960", precio="10027", tipo="Sports Touring", transmicion="estandar"),
    moto(codigo=28, marca="Montesa", modelo="Impala", año="1962", precio="10028", tipo="Touring", transmicion="automatica"),
    moto(codigo=29, marca="OSSA", modelo="GT", año="1962", precio="10029", tipo="Chopper", transmicion="semiautomatica"),
    moto(codigo=30, marca="Norton", modelo="Manx", año="1962", precio="10030", tipo="Cruiser", transmicion="estandar"),
    moto(codigo=31, marca="Bultaco", modelo="Sherpa T", año="1966", precio="10032", tipo="Cafe Racer", transmicion="automatica"),
    moto(codigo=32, marca="Bultaco", modelo="Metralla MK2", año="1966", precio="10032", tipo="Cafe Racer", transmicion="automatica"),
    #------------
    moto(codigo=33, marca="Derbi", modelo="Antorcha 50", año="1965", precio="10033", tipo="Commuter", transmicion="estandar"),
    moto(codigo=34, marca="Norton", modelo="Commando 750", año="1967", precio="10034", tipo="Scooter", transmicion="automatica"),
    moto(codigo=35, marca="Buell", modelo=" Mach III", año="1968", precio="10035", tipo="Snowmobile", transmicion="semiautomatica"),
    moto(codigo=36, marca="Vespa", modelo=" Vespino", año="1968", precio="10036", tipo="Trail", transmicion="estandar"),
    moto(codigo=37, marca=" Kawasaki", modelo=" Mach III", año="1968", precio="10037", tipo="Dirt", transmicion="automatica"),
    moto(codigo=38, marca="Montesa", modelo="Cota", año="1968", precio="10038", tipo="Moped", transmicion="semiautomatica"),
    moto(codigo=39, marca="Honda", modelo="Four", año="1969", precio="10039", tipo="Adventure", transmicion="estandar"),
    moto(codigo=40, marca="Suzuki", modelo="Gt", año="1968", precio="10040", tipo="Bobber", transmicion="automatica"),
    moto(codigo=41, marca="Brixton", modelo="Z1", año="1972", precio="10041", tipo="Atv", transmicion="semiautomatica"),
    moto(codigo=42, marca="Yamaha", modelo="RD", año="1972", precio="10042", tipo="Sports", transmicion="estandar"),
    moto(codigo=43, marca="Benelli", modelo="Sei", año="1973", precio="10043", tipo="Naked", transmicion="automatica"),
    moto(codigo=44, marca="Ducati", modelo="Road", año="1973", precio="10044", tipo="Sports Touring", transmicion="semiautomatica"),
    moto(codigo=45, marca="Sanglas", modelo="E", año="1973", precio="10045", tipo="Touring", transmicion="estandar"),
    moto(codigo=46, marca="Bultaco", modelo="Pursang MK8", año="1974", precio="10046", tipo="Chopper", transmicion="automatica"), 
    moto(codigo=47, marca="Ducati", modelo="SS 750", año="1974", precio="10047", tipo="Cruiser", transmicion="semiautomatica"),
    moto(codigo=48, marca="Laverda", modelo="SF 750", año="1974", precio="10048", tipo="Cafe Racer", transmicion="estandar"),
    moto(codigo=49, marca="Honda", modelo="Gold Wing", año="1975", precio="10049", tipo="Classic", transmicion="automatica"),
    moto(codigo=50, marca="Bultaco", modelo="Frontera", año="1975", precio="10050", tipo="Commuter", transmicion="semiautomatica"),
    moto(codigo=51, marca="BMW", modelo="R 90", año="1976", precio="10051", tipo="Scooter", transmicion="estandar"),
    moto(codigo=52, marca="OSSA", modelo="Yankee", año="1976", precio="10052", tipo="Snowmobile", transmicion="automatica"),
    moto(codigo=53, marca="Guzzi", modelo="Le Mans", año="1977", precio="10053", tipo="Trail", transmicion="semiautomatica"),
    moto(codigo=54, marca="Ariic", modelo="XT 500", año="1977", precio="10054", tipo="Dirt", transmicion="estandar"),
    moto(codigo=55, marca="Honda", modelo="CBX", año="1978", precio="10055", tipo="Moped", transmicion="automatica"),
    moto(codigo=56, marca="Buell", modelo=" Z 1300", año="1978", precio="10056", tipo="Adventure", transmicion="semiautomatica"),
    moto(codigo=57, marca="Yamaha", modelo="SR 500", año="1975", precio="10057", tipo="Bobber", transmicion="automatica"),
    moto(codigo=58, marca="BMW", modelo="R 80", año="1980", precio="10058", tipo="Atv", transmicion="semiautomatica"),
    moto(codigo=59, marca="Suzuki", modelo="Katana", año="1981", precio="10059", tipo="Sports", transmicion="estandar"),
    moto(codigo=60, marca="Suzuki", modelo="RG 250", año="1975", precio="10060", tipo="Naked", transmicion="automatica"),
    moto(codigo=61, marca="BMW", modelo="K 100", año="1984", precio="10061", tipo="Sports Touring", transmicion="semiautomatica"),
    moto(codigo=62, marca="Kawasaki", modelo="GPZ 900", año="1984", precio="10062", tipo="Touring", transmicion="estandar"),
    moto(codigo=63, marca="Yamaha", modelo="rd 500", año="1984", precio="10063", tipo="Chopper", transmicion="automatica"),
    moto(codigo=64, marca="Arena", modelo="Max V", año="1985", precio="10064", tipo="Cruiser", transmicion="semiautomatica"),
    moto(codigo=65, marca="Bicose", modelo="GSX", año="1985", precio="10065", tipo="Cafe Racer", transmicion="estandar"),
    moto(codigo=66, marca="Yamaha", modelo="FZ 750", año="1985", precio="10066", tipo="Classic", transmicion="automatica"),
    moto(codigo=67, marca="Ariic", modelo="VFR", año="1986", precio="10067", tipo="Commuter", transmicion="semiautomatica"),
    moto(codigo=68, marca="Arc", modelo="FZR", año="1984", precio="10068", tipo="Scooter", transmicion="estandar"),
    moto(codigo=69, marca="Beta", modelo="Zero", año="1989", precio="10069", tipo="Snowmobile", transmicion="automatica"),
    moto(codigo=70, marca="Yamaha", modelo="Super Tenere", año="1989", precio="10070", tipo="Trail", transmicion="semiautomatica"),
    moto(codigo=71, marca="Bimota", modelo="Tesi", año="1990", precio="10071", tipo="Dirt", transmicion="estandar"),
    moto(codigo=72, marca="Honda", modelo="Africa Twin", año="1990", precio="10072", tipo="Moped", transmicion="automatica"),
    moto(codigo=73, marca="Kawasaki", modelo="ZZ-R", año="1990", precio="10073", tipo="Adventure", transmicion="semiautomatica"),
    moto(codigo=74, marca="Caviga", modelo="DR Big", año="1990", precio="10074", tipo="Bobber", transmicion="estandar"),
    moto(codigo=75, marca="Honda", modelo="CBR", año="1991", precio="10075", tipo="Atv", transmicion="automatica"),                                    
    moto(codigo=76, marca=" Honda", modelo="NR", año="1992", precio="10076", tipo="Sports", transmicion="semiautomatica"),
    moto(codigo=77, marca="Ducati", modelo="Monster", año="1993", precio="10077", tipo="Naked", transmicion="estandar"),
    moto(codigo=78, marca="Sanglas", modelo="LS", año="1994", precio="10078", tipo="Sports Touring", transmicion="automatica"),
    moto(codigo=79, marca="Triumph", modelo="Speed Triple", año="1994", precio="10079", tipo="Touring", transmicion="semiautomatica"),
    moto(codigo=80, marca="KTM", modelo="Duke", año="1994", precio="10080", tipo="Chopper", transmicion="estandar"),
    moto(codigo=81, marca="BMW", modelo="R 1200", año="1997", precio="10081", tipo="Cruiser", transmicion="automatica"),
    moto(codigo=82, marca="MV ", modelo="Agusta", año="1998", precio="10082", tipo="Cafe Racer", transmicion="semiautomatica"),
    moto(codigo=83, marca="Suzuki", modelo="Burgman", año="1998", precio="10083", tipo="Classic", transmicion="estandar"),
    moto(codigo=84, marca="Caviga", modelo="R1J", año="1998", precio="10084", tipo="Commuter", transmicion="automatica"),
    moto(codigo=85, marca="Suzuki", modelo="GSX 1300", año="1999", precio="10085", tipo="Scooter", transmicion="semiautomatica"),
    moto(codigo=86, marca="Yamaha", modelo="T max", año="2000", precio="10086", tipo="Snowmobile", transmicion="estandar"),
    moto(codigo=87, marca="BMW", modelo="C1", año="2001", precio="10087", tipo="Trail", transmicion="automatica"),
    moto(codigo=88, marca="Harley Davidson", modelo="V Rod", año="1997", precio="10002", tipo="Trail", transmicion="automatica"),
    # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos9/?año=1997&precio=10002&tipo=Trail&transmicion=autonamtica&marca=Harley Davidson
    moto(codigo=89, marca="KTM", modelo="Adventure", año="2003", precio="10089", tipo="Moped", transmicion="estandar"),
    moto(codigo=90, marca="Honda", modelo="CBR RR", año="2004", precio="10090", tipo="Scooter", transmicion="automatica"),
    moto(codigo=91, marca="Montesa", modelo="Cota RT", año="2005", precio="10091", tipo="Snowmobile", transmicion="semiautomatica"),
    moto(codigo=92, marca="Piaggio", modelo="MP3", año="2006", precio="10092", tipo="Trail", transmicion="estandar"),
    moto(codigo=93, marca="Triumph", modelo="Street Triple", año="2007", precio="10093", tipo="Dirt", transmicion="automatica"),
    moto(codigo=94, marca="Zero", modelo="S", año="2009", precio="10094", tipo="Moped", transmicion="semiautomatica"),
    moto(codigo=95, marca="BMW", modelo="C Evolution", año="2011", precio="10095", tipo="Adventure", transmicion="estandar"),
    moto(codigo=96, marca="BMW", modelo="C 650", año="2011", precio="10095", tipo="Bobber", transmicion="estandar"),
    #-----------------------
    moto(codigo=97, marca="Yamaha", modelo="MT 09", año="2013", precio="10097", tipo="Atv", transmicion="semiautomatica"),
    moto(codigo=98, marca="Ducati", modelo="Scrambler", año="2015", precio="10098", tipo="Sports", transmicion="estandar"),
    moto(codigo=99, marca="Honda", modelo="X ADV", año="2017", precio="10099", tipo="Naked", transmicion="automatica"),
    moto(codigo=100, marca="Ducati", modelo="Superleggera", año="2017", precio="10100", tipo="Sports Touring", transmicion="semiautomatica"),
    moto(codigo=101, marca="BMW", modelo="HP4", año="2017", precio="10101", tipo="Touring", transmicion="estandar"),
    moto(codigo=102, marca="Yamaha", modelo="Nlken", año="2018", precio="10102", tipo="Chopper", transmicion="automatica"),
    moto(codigo=103, marca="KYMCO", modelo="Lonex", año="2018", precio="10103", tipo="Cruiser", transmicion="semiautomatica"),
    moto(codigo=104, marca="Harley Davidson", modelo="Livewire", año="1997", precio="10002", tipo="Trail", transmicion="automatica"),
    # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos9/?año=1997&precio=10002&tipo=Trail&transmicion=autonamtica&marca=Harley Davidson
    moto(codigo=105, marca="Daelim", modelo="Daystar", año="2015", precio="10105", tipo="Classic", transmicion="automatica"),
    moto(codigo=106, marca="Yamaha", modelo="Fazer N", año="2011", precio="10106", tipo="Commuter", transmicion="semiautomatica"),
    moto(codigo=107, marca="Hyosung", modelo="Karion", año="2012", precio="10107", tipo="Scooter", transmicion="estandar"),
    moto(codigo=108, marca="Hyosung", modelo="GT Pro comet", año="2012", precio="10108", tipo="Snowmobile", transmicion="automatica"),
    moto(codigo=109, marca="Hyosung", modelo="ST7", año="2012", precio="10109", tipo="Trail", transmicion="semiautomatica"), 
    moto(codigo=110, marca="KTM", modelo="SMC R", año="2001", precio="10110", tipo="Dirt", transmicion="estandar"),
    moto(codigo=111, marca="KTM", modelo="Super Duke R", año="2017", precio="10112", tipo="Moped", transmicion="automatica"),
    moto(codigo=112, marca="Yamaha", modelo="SR400", año="2013", precio="10113", tipo="Adventure", transmicion="semiautomatica"),
    moto(codigo=113, marca="Kawasaki", modelo="ERN", año="2012", precio="10114", tipo="Bobber", transmicion="estandar"),
    moto(codigo=114, marca="Colove", modelo="Inazumas 250", año="2013", precio="10115", tipo="Atv", transmicion="automatica"),
    moto(codigo=115, marca="Suzuki", modelo="Vanvan", año="2014", precio="10116", tipo="Sports", transmicion="semiautomatica"),
    moto(codigo=116, marca="Suzuki", modelo="GSX R", año="2014", precio="10117", tipo="Naked", transmicion="estandar"),
    moto(codigo=117, marca="Colove", modelo="Intruder M", año="2002", precio="10118", tipo="Sports Touring", transmicion="automatica"),
    moto(codigo=118, marca="KTM", modelo="RCB R", año="2003", precio="10119", tipo="Touring", transmicion="semiautomatica"),
    moto(codigo=119, marca="BMW", modelo="GS R", año="2003", precio="10120", tipo="Chopper", transmicion="estandar"),
    moto(codigo=120, marca="Derbi", modelo="S XR", año="2014", precio="10121", tipo="Cruiser", transmicion="automatica"),
    moto(codigo=121, marca="BMW", modelo="RR SL", año="2003", precio="10122", tipo="Cafe Racer", transmicion="semiautomatica"),
    moto(codigo=122, marca="Suzuki", modelo="Bandit s", año="2014", precio="10123", tipo="Classic", transmicion="estandar"),
    moto(codigo=123, marca="Derbi", modelo="V strom ABS", año="2013", precio="10124", tipo="Commuter", transmicion="automatica"),
    moto(codigo=124, marca="Suzuki", modelo="Hayabusa", año="2004", precio="10125", tipo="Scooter", transmicion="semiautomatica"),
    moto(codigo=125, marca="Kawasaki", modelo="Vulcan S", año="2004", precio="10126", tipo="Snowmobile", transmicion="estandar"),
    moto(codigo=126, marca="BMW", modelo="GUM", año="2004", precio="10127", tipo="Trail", transmicion="automatica"),
    moto(codigo=127, marca="Triumph", modelo="Trophy", año="2005", precio="10128", tipo="Dirt", transmicion="semiautomatica"),
    moto(codigo=128, marca="Felo", modelo="ZSL", año="2005", precio="10129", tipo="Moped", transmicion="estandar"),
    moto(codigo=129, marca="Suzuki", modelo="Gladius T", año="2017", precio="10130", tipo="Adventure", transmicion="automatica"),
    moto(codigo=130, marca="Kawasaki", modelo="Ninja", año="2014", precio="10131", tipo="Bobber", transmicion="semiautomatica"),
    moto(codigo=131, marca="Hanway", modelo="Versy L", año="2006", precio="10132", tipo="Atv", transmicion="estandar"),
    moto(codigo=132, marca="Ducati", modelo="Panigale", año="2013", precio="10133", tipo="Sports", transmicion="automatica"),
    moto(codigo=133, marca="Triumpg", modelo="Tiger XC", año="2012", precio="10134", tipo="Naked", transmicion="semiautomatica"),
    moto(codigo=134, marca="Hanway", modelo="Gold Wing", año="2012", precio="10135", tipo="Sports Touring", transmicion="estandar"),
    moto(codigo=135, marca="Honda", modelo="Fireblade", año="2007", precio="10136", tipo="Touring", transmicion="automatica"),
    moto(codigo=136, marca="Kawasaki", modelo="Z", año="2007", precio="10137", tipo="Chopper", transmicion="semiautomatica"),
    moto(codigo=137, marca="Felo", modelo="VFR", año="2007", precio="10138", tipo="Cruiser", transmicion="estandar"),
    moto(codigo=138, marca="Ducati", modelo="Urban Enduro", año="2007", precio="10139", tipo="Cafe Racer", transmicion="automatica"),
    moto(codigo=139, marca="KTM", modelo="Adventure K", año="2007", precio="10140", tipo="Classic", transmicion="semiautomatica"),
    moto(codigo=140, marca="Triumph", modelo="Tiger Explorer XC", año="2012", precio="10141", tipo="Commuter", transmicion="estandar"),
    moto(codigo=141, marca="Kawasaki", modelo="Versys", año="2011", precio="10142", tipo="Scooter", transmicion="automatica"),
    moto(codigo=142, marca="Ducati", modelo="Monster 821", año="20012", precio="10143", tipo="Snowmobile", transmicion="semiautomatica"),
    moto(codigo=143, marca="Ducati", modelo="Multistrada", año="2008", precio="10144", tipo="Trail", transmicion="estandar"),
    moto(codigo=144, marca="CfMoto", modelo="Nike", año="2018", precio="10145", tipo="Dirt", transmicion="automatica"),
    moto(codigo=145, marca="Benelli", modelo="BN R", año="2018", precio="10146", tipo="Moped", transmicion="semiautomatica"),
    moto(codigo=146, marca="Royal Enfield", modelo="Himalaya", año="2018", precio="10147", tipo="Adventure", transmicion="estandar"),
    moto(codigo=147, marca="Fantic Caballero", modelo="Flat Track", año="2018", precio="10148", tipo="Bobber", transmicion="automatica"),
    moto(codigo=148, marca="Aprilia", modelo="Factory", año="2017", precio="10149", tipo="Atv", transmicion="semiautomatica"),
    moto(codigo=149, marca="Husqvarna", modelo="Vitpilen", año="2018", precio="10150", tipo="Sports", transmicion="estandar"),
    moto(codigo=150, marca="Husqvarn", modelo="Svartpilen", año="2016", precio="10151", tipo="Naked", transmicion="automatica"),
    moto(codigo=151, marca="Goes ", modelo="GP", año="2018", precio="10152", tipo="Sports Touring", transmicion="semiautomatica"),
    moto(codigo=152, marca="Goes", modelo="TK", año="2017", precio="10153", tipo="Touring", transmicion="estandar"),
    moto(codigo=153, marca="MV Agusta", modelo="F3", año="2018", precio="10154", tipo="Chopper", transmicion="automatica"),
    moto(codigo=154, marca="MV Agusta", modelo="Brutale", año="2019", precio="10155", tipo="Cruiser", transmicion="semiautomatica"),
    moto(codigo=155, marca="CFMoto", modelo="Papio", año="2018", precio="10156", tipo="Cafe Racer", transmicion="estandar"),
    moto(codigo=156, marca="Moto Guzzi", modelo="Milano", año="2017", precio="10157", tipo="Classic", transmicion="automatica"),
    moto(codigo=157, marca="Mitt", modelo="Scrambler", año="2017", precio="10158", tipo="Commuter", transmicion="semiautomatica"),
    moto(codigo=158, marca="MH", modelo="WYN", año="2019", precio="10159", tipo="Scooter", transmicion="estandar"),
    moto(codigo=159, marca="MH", modelo="Lord Martin", año="2019", precio="10159", tipo="Snowmobile", transmicion="estandar"),
    moto(codigo=160, marca="MH", modelo="Bogga", año="2019", precio="10161", tipo="Trail", transmicion="semiautomatica"),
    # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos8/?marca=MH&transmicion=estandar&año=2019&precio=10159
    moto(codigo=161, marca="Malaguti", modelo="XTM", año="2019", precio="10162", tipo="Dirt", transmicion="estandar"),
    moto(codigo=162, marca="Malaguti", modelo="Monte Pro", año="2020", precio="10163", tipo="Moped", transmicion="automatica"),
    moto(codigo=163, marca="Brixton", modelo="BX", año="2020", precio="10164", tipo="Adventure", transmicion="semiautomatica"),
    moto(codigo=164, marca="Brixton", modelo="Saxby", año="2020", precio="10165", tipo="Bobber", transmicion="estandar"),
    moto(codigo=165, marca="Macbor", modelo="Fun", año="2021", precio="10166", tipo="Atv", transmicion="automatica"),
    moto(codigo=166, marca="Keeway", modelo="RKF", año="2021", precio="10167", tipo="Sports", transmicion="semiautomatica"),
    moto(codigo=167, marca="Triumph", modelo="Street Triple R", año="2021", precio="10168", tipo="Naked", transmicion="estandar"),
    moto(codigo=168, marca="Voge", modelo="R500", año="2020", precio="10169", tipo="Sports Touring", transmicion="automatica"),
    moto(codigo=169, marca="Keeway", modelo="Superlight", año="2020", precio="10170", tipo="Touring", transmicion="semiautomatica"),
    moto(codigo=170, marca="Zero", modelo="SR", año="2020", precio="10171", tipo="Chopper", transmicion="estandar"),
    moto(codigo=171, marca="Zontes", modelo="V", año="2021", precio="10172", tipo="Cruiser", transmicion="automatica"),
    moto(codigo=172, marca="MV", modelo="Dragster", año="2020", precio="10173", tipo="Cafe Racer", transmicion="semiautomatica"),
    moto(codigo=173, marca="Voge", modelo="DS", año="2020", precio="10174", tipo="Classic", transmicion="estandar"),
    moto(codigo=174, marca="FB Mondial", modelo="HPS", año="2021", precio="10175", tipo="Commuter", transmicion="automatica"),
    moto(codigo=175, marca="Motron", modelo="Tokyo", año="2021", precio="10175", tipo="Scooter", transmicion="semiautomatica"),
    moto(codigo=196, marca="Motron", modelo="Revolver", año="2021", precio="10175", tipo="Scooter", transmicion="semiautomatica"), 
    moto(codigo=177, marca="Motron", modelo="Vizion", año="2022", precio="10178", tipo="Trail", transmicion="automatica"),
    # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos7/?marca=Motron&precio=10175&tipo=Scooter
    moto(codigo=198, marca="Zontes", modelo="GX1", año="2022", precio="10179", tipo="Dirt", transmicion="semiautomatica"),
    moto(codigo=179, marca="Urbet", modelo="Gadiro", año="2023", precio="10180", tipo="Moped", transmicion="estandar"),
    moto(codigo=180, marca="Orcal", modelo="Astor", año="2022", precio="10181", tipo="Adventure", transmicion="automatica"),
    moto(codigo=181, marca="Zontes", modelo="U1", año="2023", precio="10182", tipo="Bobber", transmicion="semiautomatica"),
    moto(codigo=182, marca="Urbet", modelo="Nura", año="2023", precio="10183", tipo="Atv", transmicion="estandar"),
    moto(codigo=183, marca="Bimoto", modelo="Tesi", año="2022", precio="10184", tipo="Sports", transmicion="automatica"),
    moto(codigo=184, marca="Super Soco", modelo="TS Street Hunter", año="2022", precio="10185", tipo="Naked", transmicion="semiautomatica"),
    moto(codigo=185, marca="QJ SRK", modelo="S", año="2023", precio="10186", tipo="Sports Touring", transmicion="estandar"),
    moto(codigo=186, marca="Mutt", modelo="Mushman", año="2023", precio="10187", tipo="Touring", transmicion="automatica"),
    moto(codigo=187, marca="QJ SRK", modelo="X", año="2023", precio="10188", tipo="Chopper", transmicion="semiautomatica"),
    moto(codigo=188, marca="RGNT", modelo="Scrambler", año="2022", precio="10189", tipo="Cruiser", transmicion="estandar"),
    moto(codigo=189, marca="RGNT", modelo="Clasicc", año="2023", precio="10190", tipo="Cafe Racer", transmicion="automatica"),
    moto(codigo=190, marca="OX One", modelo="Montecarlo", año="2021", precio="10191", tipo="Classic", transmicion="semiautomatica"),
    moto(codigo=191, marca="Orcal", modelo="SK03", año="2021", precio="10192", tipo="Commuter", transmicion="estandar"),
    moto(codigo=192, marca="Leonart", modelo="Rigger", año="2023", precio="10193", tipo="Scooter", transmicion="automatica"),
    moto(codigo=198, marca="Macbor Rockster", modelo="Flat", año="2017", precio="10194", tipo="Snowmobile", transmicion="semiautomatica"),
    moto(codigo=194, marca="Triumph", modelo="Trident", año="2024", precio="10195", tipo="Trail", transmicion="estandar"),
    moto(codigo=195, marca="Rieju", modelo="Century", año="2024", precio="10196", tipo="Dirt", transmicion="automatica"),
    moto(codigo=196, marca="Keeway", modelo="V3C", año="2023", precio="10197", tipo="Moped", transmicion="semiautomatica"),
    moto(codigo=197, marca="Energica", modelo="Experia", año="2024", precio="10198", tipo="Adventure", transmicion="estandar"),
    moto(codigo=198, marca="Triumph", modelo="Rocket 3", año="2017", precio="10199", tipo="Bobber", transmicion="automatica"),
    moto(codigo=199, marca="Macbor Rockster", modelo="Mot", año="2024", precio="10200", tipo="Atv", transmicion="semiautomatica"),
    moto(codigo=200, marca="Vmoto", modelo="Stash", año="2024", precio="10201", tipo="Sports", transmicion="estandar") 
    ] 
 
 #***Get con Filtro Query

#----------
@app.get("/motos/")
async def motosclass(codigo:int):
    motos=filter (lambda motos: motos.codigo == codigo, motos_list)  #Función de orden superior
    try:
        return list(motos)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
#http://127.0.0.1:8000/motos/?codigo=198



#Ruta que filtra elementos por marca y año 2 criterios
@app.get("/motos6/")
async def get_motos(marca: str, año: int):
    filtrar_motos = filter (lambda moto: moto.marca == marca and 
    moto.año == año, motos_list)
    return list(filtrar_motos)
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos6/?marca=Honda&año=1991


#Ruta que filtra elementos por marca, precio y tipo 3 criterios
@app.get("/motos7/")
async def get_motos(marca: str, precio: int, tipo: str):
    filtrar_motos = filter (lambda moto: moto.marca == marca and 
    moto.precio == precio 
    and moto.tipo == tipo, motos_list)
    return list(filtrar_motos)
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos7/?marca=Motron&precio=10175&tipo=Scooter


#Ruta que filtra elementos por marca, transmicion, año y precio 4 criterios
@app.get("/motos8/")
async def get_motos(marca: str, transmicion: str, año: int, precio: int):
    filtrar_motos = filter (lambda moto: moto.marca == marca and 
    moto.transmicion == transmicion
    and moto.año == año and moto.precio == precio, motos_list)
    return list(filtrar_motos)
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos8/?marca=MH&transmicion=estandar&año=2019&precio=10159


#Ruta que filtra elementos por año, precio, tipo, transmicion y marca 5 criterios
@app.get("/motos9/")
async def get_motos(año: int, precio: int, tipo: str, transmicion: str, marca:str):
    filtrar_motos = filter (lambda moto: moto.año == año and 
    moto.precio == precio
    and moto.tipo == tipo and moto.transmicion == transmicion
    and moto.marca == marca, motos_list)
    return list(filtrar_motos)
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/motos9/?año=1997&precio=10002&tipo=Trail&transmicion=automatica&marca=Harley Davidson
#uvicorn Filtro_Query:app --reload