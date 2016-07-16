library(foreach)

setwd("C:/LifeHistory/Lifehistory/")


#X <- read.csv("common_names_worksheet.csv")
X <- read.csv("breeding_dist_worksheet.csv")


OUT <- matrix(ncol=3,nrow=0)  
  
for(i in 1:nrow(X)){
  d1 <- data.frame(X[i,])
  test <- X[i,c(which(d1[1,]!=""))]
  species_id <- rep(as.character(X[i,1]),(ncol(test)-1))
  common_name <- as.character(unlist(test[2:length(test)]))
  common_name_id <- c(1:length(common_name)) 
  df <- cbind(species_id,common_name_id,common_name)
  print(df)
  OUT<-rbind(OUT,df)
  
  
}



