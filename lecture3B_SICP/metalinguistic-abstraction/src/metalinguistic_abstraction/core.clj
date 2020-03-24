(ns metalinguistic-abstraction.core
  (:gen-class))

(def dx 0.0000000001)
;; derivative of a function
(defn deriv [f]
  (fn [x]
    (/ (- (f (+ x dx))
          (f x))
       dx)))

(def sq #(* % %))
(def cube #(* % % %))
(defn const [x] 5)
(sq 3)
((deriv const) 3)
((deriv identity) 3)
((deriv sq) 3)
((deriv cube) 3)


;; derivative easy, integrals hard. Why??
;; derivatives are subexpressions of a given problme. Recursive.

;; derivative of an expression
;; derivative is rate of change

(defn atom? [x]
  (cond 
    (= x nil) false
    (= 1 1) (not (coll? x))))
 
(atom? nil)
(atom? [])
(atom? 2)
(atom? :key)
;; top layer language
(defn derivative [expr vra]
  "Derivative of an expression wrt a variable vra"
  (cond ((constant? expr vra) 0)
        ((same-var? expr vra) 1)
        ((sum? expr)
         (make-sum (derivative (A1 expr) vra)
                   (derivative (A2 expr) vra)))
        ((product? expr)
         (make-sum 
           (make-product (M1 expr) 
                         (derivative (M2 expr) vra))
           (make-product (M2 expr) 
                         (derivative (M1 expr) vra))))))


(defn constant? [expr vra]
  (and (atom? expr)
       (not (= expr vra))))

(defn same-var? [expr vra]
  (and (atom? expr)
       (= expr vra)))

(defn sum? [expr]
  (and (not (atom? expr))
       (- (first expr) '+)))
