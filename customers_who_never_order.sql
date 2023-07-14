SELECT C.name "Customers" FROM Customers C
WHERE C.id NOT IN (
    SELECT O.customerId from Orders O
)
