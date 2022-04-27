mat= matrix(nrow =1,ncol=300)
for(j in 1:300)
{
  for (i in 1:30)
  {
    {
      temp=1
      for(k in 1:29)
      {
        temp<-(temp*(365-k)/365)
      }
    }
  }
  mat[j]=temp*(29/365)
}
print(sum(mat[])/300)