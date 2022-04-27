s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
d={"a":1,"b":3}
c={}
for i in (s,a,d):
    c.update(i)
print(c)