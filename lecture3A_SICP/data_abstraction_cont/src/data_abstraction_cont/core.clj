(ns data-abstraction-cont.core
  (:gen-class))

;; vector data abstraction
;; representation
(defn make-vector [a b]
  (cons' a b))

(defn cons' [a b]
  (cons a [b]))

(make-vector 2 3)

(defn xcor [v] (first v))

(defn ycor [v] (second v))

;; use
(def v (make-vector 2 3))

(ycor v)

;; add vectors
(defn +vector [v1 v2]
  (make-vector (+ (xcor v1) (xcor v2))
               (+ (ycor v1) (ycor v2))))

(def v1 (make-vector 2 3))
(def v2 (make-vector 4 5))
(+vector v1 v2)

;; scale a vector
(defn scale [s v]
  (make-vector (* s (xcor v))
               (* s (ycor v))))

(scale 2 v1)

;; representing line segments
(def make-segment cons')
(def seg-start first)
(def seg-end second)

(def ln (make-segment (make-vector 2 3)
                      (make-vector 4 5)))
ln




