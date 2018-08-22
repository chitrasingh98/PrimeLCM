def Prime():
  m=1
  p=[True for i in range(100000000)]
  p[0],p[1]=False,False
  i=2
  while(i*i<=100000000):
    if(p[i]==True):
      m*=i
      for j in range(2*i,100000000,i):
        p[j]=False
    i+=1    
  for k in range(i,100000000):
    if i==True:
      m*=k  
  print(m% 1000000007)
Prime()   
