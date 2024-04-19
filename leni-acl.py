#Consultas ACL IPV4
aclNum = int(input("Ingrese el número de ACL IPV4? "))
if aclNum >= 1 and aclNum <= 99:
    print("Esta es una ACL IPv4 estándar!!!.")
elif aclNum >=100 and aclNum <= 199:
    print("Esta es una ACL IPv4 extendida!!!")
else:
    print("Esta ACL IPv4 no es extendida o estandar!!! .")
