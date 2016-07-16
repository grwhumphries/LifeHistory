setwd("C:/LifeHistory/Lifehistory/")

X <- read.csv("species.csv")

nList <- names(X)

count<-0
for(i in nList){
  
  #msg <- paste("traits.",i,"=","row[",count,"]",sep="")
  msg <- paste(i," character(50),",sep="")
  
  
  print(msg)
  count<-count+1

}

#### Creates the values for csv download


Y <- read.csv("Fieldnames.csv")
Z <- list()
count<-1
for(i in Y$names){
  Z[count]<-as.character(i)
  count<-count+1
}

A <- paste(Z,collapse="', '")
B <- paste("Traits.objects.all().values('",A,"')",sep = '')




#### Create list of unique citations for the citation table

A <- read.csv("Citation_Workbook.csv")

NameList<-unique(A$citation_name)

out <- data.frame(sort(as.character(NameList)))

write.csv(out,"citation.csv")





