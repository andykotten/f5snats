Python program to show connections on a F5 load balancer(basically API version of #tmsh show sys connection).
Particularly useful when using sNAT and true source ip is not visible on servers.

Takes as input the name of which datacenter the load balancer is in, then finds its ip to log into. Also choose whether to check connections for a particular VIP or a pool member.
