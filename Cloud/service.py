from zeep import Client
wsdl = "http://localhost:8080/WebApplication1/inrtoDollr?wsdl"
cli = Client(wsdl)
a=int(input("Enter amount in dollars : "))
result = cli.service.INRTODOLLAR(a)
print(result)