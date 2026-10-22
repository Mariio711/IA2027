
(deftemplate entidad
   (slot id)
   (slot categoria)
   (slot lugar)
   (slot descripcion (type STRING)))

(deftemplate lugar
   (slot id)
   (slot nombre (type STRING))
   (slot descripcion (type STRING)))

(deftemplate guardian
   (slot id)
   (slot lugar)
   (slot descripcion (type STRING))
   (slot estado (allowed-values patrulla alerta despistado desactivado) (default patrulla))
)

(deffacts meseta
   (entidad (id explorador) (categoria actor) (lugar pico))
   (entidad (id tablilla) (categoria objeto) (lugar explorador))
   (entidad (id capa) (categoria objeto) (lugar templo))
   (entidad (id manzana) (categoria objeto) (lugar bosque))
   (entidad (id pedestal) (categoria escenario) (lugar camara)
      (descripcion "Tiene la forma exacta de la tablilla."))

   (lugar (id camara) (nombre "Camara del Letargo")
      (descripcion "Una sala de piedra. Al norte hay una puerta."))
   (lugar (id explanada) (nombre "Explanada de las ruinas")
      (descripcion "Columnas derruidas rodeadas de hierba alta."))
   (lugar (id templo) (nombre "Templo derruido")
      (descripcion "Un templo sin techo. El tiempo parece no haber pasado en su interior."))
   (lugar (id bosque) (nombre "Bosque de los susurros")
      (descripcion "Arboles viejos y un murmullo que no sabes de donde viene."))
   (lugar (id pico) (nombre "Pico helado")
      (descripcion "Desde aqui ves que la meseta esta rodeada de acantilados."))

   (camino camara norte explanada abierto)
   (camino explanada sur camara abierto)
   (camino explanada norte templo abierto)
   (camino templo sur explanada abierto)
   (camino explanada oeste bosque abierto)
   (camino bosque este explanada abierto)
   (camino pico oeste explanada abierto)

   (resistencia 60))

(deffacts atalaya
   (lugar (id atalaya) (nombre "Atalaya en ruinas") (descripcion "Una torre derruida al borde del acantilado."))
   (camino pico este atalaya abierto)
   (camino atalaya oeste pico abierto)
   (entidad (id paravela) (categoria objeto) (lugar atalaya) (descripcion "Una tela resistente tensada que permite planear."))
   (guardian (id atalaya1) (lugar atalaya) (descripcion "Un automata antiguo cubierto de escarcha"))
    
)

(deffacts 

)

(defrule inicio
   (declare (salience 20))
   =>
   (println "Tras entrar en calor junto a la hoguera, oteas el horizonte.")
   (println "Al este, una atalaya en ruinas se recorta contra el cielo."))

(defrule orden_desconocida
   (declare (salience -10))
   ?o <- (orden $?)
   =>
   (retract ?o)
   (println "No entiendes muy bien lo que quieres hacer."))

(defrule mover
   ?o <- (orden ir ?dir)
   ?e <- (entidad (id explorador) (lugar ?l))
   (camino ?l ?dir ?destino abierto)
   =>
   (retract ?o)
   (modify ?e (lugar ?destino)))

(defrule describir_lugar
   (declare (salience 10))
   (entidad (id explorador) (lugar ?l))
   (lugar (id ?l) (nombre ?n) (descripcion ?d))
   =>
   (println "[" ?n "] " ?d))

(defrule recoger
   ?o <- (orden recoger | tomar $? ?c)
   (entidad (id explorador) (lugar ?l))
   ?f <- (entidad (id ?c) (categoria objeto) (lugar ?l))
   =>
   (retract ?o)
   (modify ?f (lugar explorador))
   (println "Recoges: " ?c))

(defrule ver_objetos
   (declare (salience 5))
   (entidad (id explorador) (lugar ?l))
   (entidad (id ?c) (categoria objeto) (lugar ?l))
   =>
   (println "Ves: " ?c))

(defrule paravela_custodiada
   (declare (salience 10))
   ?o <- (orden recoger | tomar $? paravela)
   (entidad (id explorador) (lugar atalaya))
   (not (guardian (lugar atalaya) (estado desactivado)))
   =>
   (retract ?o)
   (println "No parece seguro coger la paravela en este momento.")
)

(defrule sin_camino
   ?o <- (orden ir ?dir)
   (not (camino ?l ?dir ?destino ?estado))
=>
   (retract ?o)
   (println "No hay ningun camino hacia el" ?destino)

)