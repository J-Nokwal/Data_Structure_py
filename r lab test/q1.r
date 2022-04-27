getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
getmeandeviation <-function(v) {
  t <-getmode(v)
  n = 0
  return (sum(v-mean(v))/length(v))
}

sample1<-rnorm(1500,55,10)
sample2<-runif(1500,1,100)
# print(paste(sample1))



print("with rnorm")
print(paste("mean of subject",mean(sample1, na.rm=FALSE)))
print(paste("mode of subject ",getmode(sample1)))
print(paste("median of subject ",median(sample1)))
print(paste("Range of subject ",max(sample1)-min(sample1)))
print(paste("Mean Deviation of subject ",getmeandeviation(sample1)))
print(paste("standard Deviation of subject ",sd(sample1)))
print(paste("Variance of subject ",var(sample1)))
print(paste(""))

print("with runif")
print(paste("mean of subject",mean(sample2, na.rm=FALSE)))
print(paste("mode of subject ",getmode(sample2)))
print(paste("median of subject ",median(sample2)))
print(paste("Range of subject ",(max(sample2)-min(sample2))))
print(paste("Mean Deviation of subject ",getmeandeviation(sample2)))
print(paste("standard Deviation of subject ",sd(sample2)))
print(paste("Variance of subject ",var(sample2)))




