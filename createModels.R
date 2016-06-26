setwd("C:/LifeHistory/Lifehistory/")

X <- read.csv("Seabirds-edited.csv")

nList <- names(X)

count<-0
for(i in nList){
  
  msg <- paste("traits.",i,"=","row[",count,"]",sep="")
  
  
  print(msg)
  count<-count+1

}