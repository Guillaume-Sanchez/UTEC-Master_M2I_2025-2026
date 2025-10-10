
supprimer une liste : 
no access-list 1

access-list 1 deny host 192.168.20.1
access-list 1 permit any
interface GigabitEthernet0/1
ip access-group 1 out
