n<-9000
ngroup<-300
gsize<-n/300

solve<-function(){
    bdays <- sample(1:365, gsize, replace = TRUE)
  any(duplicated(bdays))
}
val<-replicate(ngroup,solve())
print(mean(val))
plot(val)