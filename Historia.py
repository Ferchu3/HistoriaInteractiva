import pygame
import sys
import time

escena1="""Te encuentras volando en un avión cuando, de repente, se empiezan a oír ligeras turbulencias, 
en un momento se siente una gran explosion que hace caer el avión…"""
escena2="""Despiertas bajo un asiento del avión sin mayores heridas, notas que el avión está completamente destruido y 
parece no haber supervivientes, sales de los escombros y solo encuentras un gran desastre ¿Deseas revisar los restos del avión?"""
escena3="""Revisas los restos del avión y te encuentras con algunas provisiones, una linterna y una vieja mochila que contiene un radio en mal estado, 
guardas todo en la mochila, se está haciendo tarde, ¿Decides salir del avión e investigar?"""
escena4="""Decides no revisar los restos del avión y en cambio emprender tu aventura para buscar la salida de donde te encuentras, 
caminas un tiempo y encuentras un río, ¿Decides pasar de largo?"""
escena5="""Sales del avión con los peligros de la pronta noche, en tu camino notas un pequeño destello de luz proveniente desde una montaña, 
¿Decides ir a investigar?"""
escena6="""Decides quedarte a pasar la noche en un pequeño refugio con los restos del avión, durante la noche escuchas ruidos raros, ¿Decides investigar?"""
escena7="""Pasas de largo el río y sigues con tu expedición, empiezas a sentir un poco de hambre y tus provisiones ya son pocas, ¿Te detienes a conseguir algo?"""
escena8="""Te detienes un tiempo en la orilla del río, mientras estás sentado recuerdas lo útil que puede ser un río para una civilización, 
con eso en mente ¿Tratar de construir una pequeña balsa con madera?"""
escena9="""Atraviesas una gran parte del bosque hasta encontrar la fuente de ese destello de luz, ya se hizo de noche y empiezas a oir ruidos de animales salvajes, 
encuentras materiales para hacer un pequeño campamento ¿Decides seguir avanzando?"""
escena10="""No le tomas importancia a los brillos y decides continuar con tu camino hacia algún lado, 
la noche empieza a caer y te estas quedando sin suministros, a lo lejos ves un pequeño lago. ¿Decides ir al lago?"""
escena11="""Decides investigar los ruidos y estos provenían de la radio del avión, no se entiende casi nada y no parecen responder a tus gritos, ¿Decides rendirte?"""
escena12="""Sigues durmiendo en una plácida noche en un avión destruido, otros ruidos te molestan en la noche, esta vez se oyen más fuertes, ¿Sigues durmiendo?"""
escena13="""Te detienes a conseguir un poco de comida para avanzar en tu camino, cuando te dispones a volver a comenzar escuchas sonidos de ayuda desde dentro del bosque ¿Ayudar?"""
escena14="""Decides seguir con tu camino y en un lapso de tiempo empiezas a sentir hambre, la noche está al caer y no tienes donde quedarte, 
empiezas a andar más rápidamente pero no encuentras ningún lugar, de repente te tropiezas con algo, ¿Investigar?"""
escena15="""Recolectas la madera y logras formar un pequeño cuadrado que flote sobre la superficie del río, notas que está un poco flojo uno de los nudos. 
¿Tomarle importancia?"""
escena16="""Decides hacer un pequeño campamento para pasar la noche, armas una pequeña casa de acampar junto a una fogata, 
tienes una sensación de que debes salir de ahí a toda costa, ¿Abandonas tu mini campamento?"""
escena17="""Casi muerto llegas al lago donde encuentras una pequeña construcción de madera a lo lejos, 
no estás seguro de si logras llegar andando hacia esa taberna, ¿Decides tratar de llamar la atención de los que se encuentran ahí?"""
escena18="""Decides hacer caso omiso a tus instintos y pasas la noche en tu base improvisada, a la mañana siguiente despiertas temprano y listo para seguir con tu camino, 
aun un poco oscuro pero es buena hora para partir. ¿Deseas esperar unas horas más?"""
escena19="""Decidiste arreglar los nudos de tu balsa y ahora si zarpar hacia tu salvación, el rio corre muy fuerte pero tu balsa logra aguantarlos, 
vez una pequeña casa a lo lejos, ¿Decides desembarcar rápidamente?"""
escena20="""No logras comunicarte por la radio y decides volver a dormir, en el medio de la noche vuelves a escuchar la radio, ¿Decides intentarlo de nuevo?"""
escena21="Te despiertas y te das cuenta del peligro del oso, rápido, elige a donde correr, ¿Izquierda o Derecha?"
Final1="""Encontrado, Los destellos de luz provenían de un grupo de rescatistas que buscaba a las personas del avión, 
te dieron hospedaje y alimentación en su pequeño campamento, lo lograste, volverás a casa"""
Final1v2="""Encontrado, Un grupo de rescatistas empezó una excursión para encontrar a las personas del avión, gracias a que tu campamento se vio desde lejos te encontraron, 
te dieron hospedaje y alimentación en su pequeño campamento, lo lograste, volverás a casa."""
Final1v3="""Encontrado, Decides ir andando hacia la taberna  y con tus últimas fuerzas entras en ella, 
las personas que se encontraban dentro corren a auxiliarte, las personas salvan tu vida y te ayudan a volver a tu hogar."""
Final1v4="""Encontrado, Los gritos que lanzabas a la radio lograron ser recibidos por los encargados del avión, logras dar tus coordenadas, lo lograste, volverás a casa."""
Final1v5="""Encontrado, Mientras corrias a la derecha sin llamar la atencion del oso te encuentras con un campamento que organizaron para encontrar a tu tripulacion perdida,
te dieron hospedaje y alimentación en su pequeño campamento, lo lograste, volverás a casa"""
Final2="""Devorado, Decidiste confiar en tu instinto y seguiste con tu camino, 
lamentablemente te topaste con un gran oso que estaba decidido a proteger su territorio."""
Final2v2="""Devorado, Mientras la radio sigue sonando decides salir a tomar un poco el aire, lamentablemente te topaste con un gran oso que estaba decidido a proteger su territorio"""
Final2v3="""Devorado, No le tomaste atencion a los ruidos, lo ultimo que escuchas es a un oso abriendose paso por el avion directi hacia ti..."""
Final2v4="""Devorado, Decidiste confiar en tu instinto y corriste a la izquierda, 
lamentablemente te topaste con el gran oso que estaba decidido a proteger su territorio."""
Final3="""Cazado, Empiezas un nuevo camino esa mañana, lamentablemente te encontrabas en una zona donde la gente suele hacer caza furtiva y 
en un mal disparo una bala impacta contigo causandote la muerte."""
Final3v2="""Tratas de llegar a esa casa sin darte cuenta que era propiedad de unos cazadores, no muy felices con tu visita tratan de ahuyentarte 
lamentablemente en un mal disparo una bala impacta contigo causandote la muerte."""
Final3v3="""Cazado, lamentablemente te encontrabas en una zona donde la gente suele hacer caza furtiva y 
en un mal disparo una bala impacta contigo causandote la muerte."""
Final4="""Perdido, Decidiste seguir tu camino sin detenerte, lamentablemente sin comida, 
sin agua y con mucho frío la aventura se te complico, sin más caes al suelo rendido y muerto."""
Final4v2="""Perdido, haces ruido, lanzas cosas y hasta tratas de encender fuego con tus últimas fuerzas, 
nadie te ve, sin más caes al suelo rendido y muerto."""
Final5="""Accidente, Mientras tratas de ir a pie persiguiendo el río tropiezas con una piedra y caes al río, un río que corría agresivamente del que no puedes escapar."""
Final5v2="""Accidente, Mientras tratas de navegar en el río chocas con una piedra, tu balsa empieza a desarmarse y caes al río, un río que corría agresivamente del que no puedes escapar."""
Final6="""Civilización, llegas a otro puerto donde desembarcas y encuentras una civilización en el bosque, las personas te ayudan con tu situación y te ayudan a volver a tu hogar."""
Final6v2="""Civilización, Al ayudar al señor que se encontraba bajo un árbol le contaste tu situación y te llevo al pueblo, ahí las personas te ayudaron y pudiste volver a casa."""
Final7="""Secreto, tropezaste con lo que parecía una compuerta a un bunker, cuando entraste encontraste provisiones para mucho tiempo, pero tu no debias estar ahí, s
ientes un golpe en la nuca y caes desmayado…"""

print(escena1)
time.sleep(2)
print(escena2)
time.sleep(.5)
opcion=input("Escribe Y/N para avanzar  ")
if opcion== "Y":
    time.sleep(1)
    print(escena3)
    opcion=input("Escribe Y/N para avanzar  ")
    if opcion== "Y":
        time.sleep(1)
        print(escena5)
        opcion=input("Escribe Y/N para avanzar  ")
        if opcion== "Y":
            time.sleep(1)
            print(escena9)
            opcion=input("Escribe Y/N para avanzar  ")
            if opcion== "Y":
                time.sleep(1)
                print(Final1)
            elif opcion =="N":
                time.sleep(1)
                print(escena16)
                opcion=input("Escribe Y/N para avanzar  ")
                if opcion== "Y":
                    time.sleep(1)
                    print(Final2)
                elif opcion =="N":
                    time.sleep(1)
                    print(escena18)
                    opcion=input("Escribe Y/N para avanzar  ")
                    if opcion== "Y":
                        time.sleep(1)
                        print(Final1v2)
                    elif opcion =="N":
                        time.sleep(1)
                        print(Final3)
        elif opcion =="N":
            time.sleep(1)
            print(escena10)
            opcion=input("Escribe Y/N para avanzar  ")
            if opcion== "Y":
                time.sleep(1)
                print(escena17)
                opcion=input("Escribe Y/N para avanzar  ")
                if opcion== "Y":
                    time.sleep(1)
                    print(Final4v2)
                elif opcion =="N":
                    time.sleep(1)
                    print(Final1v3)
            elif opcion =="N":
                time.sleep(1)
                print(Final4)
    elif opcion =="N":
        time.sleep(1)
        print(escena6)
        opcion=input("Escribe Y/N para avanzar  ")
        if opcion== "Y":
            time.sleep(1)
            print(escena11)
            opcion=input("Escribe Y/N para avanzar  ")
            if opcion== "Y":
                time.sleep(1)
                print(escena20)
                opcion=input("Escribe Y/N para avanzar  ")
                if opcion== "Y":
                    time.sleep(1)
                    print(Final1v4)
                elif opcion =="N":
                    time.sleep(1)
                    print(Final2v2)
            elif opcion =="N":
                time.sleep(1)
                print(Final1v4)
        elif opcion =="N":
            time.sleep(1)
            print(escena12)
            opcion=input("Escribe Y/N para avanzar  ")
            if opcion== "Y":
                time.sleep(1)
                print(Final2v3)
            elif opcion =="N":
                time.sleep(1)
                print(escena21)
                opcion=input("Escribe L/R para avanzar  ")
                if opcion== "L":
                    time.sleep(1)
                    print(Final2v4)
                elif opcion =="R":
                    time.sleep(1)
                    print(Final1v5)
elif opcion =="N":
    time.sleep(1)
    print(escena4)    
    opcion=input("Escribe Y/N para avanzar  ")
    if opcion== "Y":
        time.sleep(1)
        print(escena7)
        opcion=input("Escribe Y/N para avanzar  ")
        if opcion== "Y":
            time.sleep(1)
            print(escena13)
            opcion=input("Escribe Y/N para avanzar  ")
            if opcion== "Y":
                time.sleep(1)
                print(Final6v2)
            elif opcion =="N":
                time.sleep(1)
                print(Final3v3)
        elif opcion =="N":
            time.sleep(1)
            print(escena14)
            opcion=input("Escribe Y/N para avanzar  ")
            if opcion== "Y":
                time.sleep(1)
                print(Final7)
            elif opcion =="N":
                time.sleep(1)
                print(Final4)
    elif opcion =="N":
        time.sleep(1)
        print(escena8)
        opcion=input("Escribe Y/N para avanzar  ")
        if opcion== "Y":
            time.sleep(1)
            print(escena15)
            opcion=input("Escribe Y/N para avanzar  ")
            if opcion== "Y":
                time.sleep(1)
                print(escena19)
                opcion=input("Escribe Y/N para avanzar  ")
                if opcion== "Y":
                    time.sleep(1)
                    print(Final3v2)
                elif opcion=="N":
                    time.sleep(1)
                    print(Final6)
            elif opcion== "N":
                time.sleep(1)
                print(Final5v2)
        elif opcion =="N":
            time.sleep(1)
            print(Final5)