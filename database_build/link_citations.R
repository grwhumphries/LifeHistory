### Assign citeID to citations
library(dplyr)
library(gdata)


setwd("C:/LifeHistory/Lifehistory/")

C <- read.csv("citation.csv")
D <- read.csv("Citation_Workbook.csv")

for(i in 1:nrow(D)){
  
  ind <- which(C$citation_name == as.character(D$citation_name[i]))
  D$cite_id[i] <- as.character(C$citation_id[ind])
  
  
  
}
write.csv(D,"sp_site_trait.csv",row.names=F)
