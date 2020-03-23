(ns newton-method.core
  (:gen-class))

(defn myadd [a b]
  (if (= 0 a)
    b
    (myadd (inc a) (dec b))))

(defn myadd [a b]
  (if (= 0 a)
    b
    (myadd (inc (inc a) b))))

;; sum of integers from a upto b inclusive
(defn sum [a b]
  (if (> a b)
    0
    (+ a (sum (inc a) b))))

(defn sum-square [a b]
  (def sq #(* % %))
  (if (> a b)
    0
    (+ (sq a) (sum-square (inc a) b))))

;; abstraction of summation
(defn summation [term a nxt b]
  (if (> a b)
    0
    (+ (term a) (summation term (nxt a) nxt b))))

(defn mysum [a b]
  (summation identity a inc b))
            
(= (sum 1 4)
   (mysum 1 4))

(defn sumofsqrs [a b]
  (summation sq a inc b))

(=
 (sumofsqrs 2 4)
 (sum-square 2 4))

;; code leading upto newton's method for finding 
;; fixed points square root and other















