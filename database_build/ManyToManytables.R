####### Use citation workbook to create species_citation table #########
setwd("C:/LifeHistory/database_build/")

X <- read.csv("Citation_Workbook.csv")
Y <- read.csv("CSVs_for_db/citation.csv")

for(i in 1:nrow(Y)){
  index <- which(X$citation_name == Y$citation_name[i])
  X[index,2] <- as.character(Y$cite_id[i])
  
}
X <- data.frame(relation_id=c(1:nrow(X)),X)


############# Create many to many species/citation/trait table ###############

setwd("C:/LifeHistory/database_build/")
X <- read.csv("CSVs_for_db/species_citation.csv")
Y <- read.csv("newtraits.csv")
library(foreach)


speclist <- unique(X$species_id)

OUT <- foreach(s = speclist,.combine='rbind') %do% {
  featureids <- Y$feature_id[which(Y$species_id == as.character(s))]
  J <- which(X$species_id == s)
  spcs <- length(J)
  reps <- rep(featureids,spcs)
  citeids <- as.character(X[J,3])
  cites<-unlist(lapply(citeids,function(x) rep(x,30)))
  df <- data.frame(feature_id = reps,cite_id = cites)
  return(df)
}


################ Many to many other traits to citation ############

setwd("C:/LifeHistory/database_build/CSVs_for_db/")
X <- read.csv("species_citation.csv")
Y <- read.csv("other_traits.csv")

speclist <- unique(X$species_id)

OUT <- foreach(s = speclist,.combine='rbind') %do% {
  featureids <- Y$trtid[which(Y$species_id == as.character(s))]
  J <- which(X$species_id == s)
  spcs <- length(J)
  reps <- rep(featureids,spcs)
  citeids <- as.character(X[J,3])
  cites<-unlist(lapply(citeids,function(x) rep(x,7)))
  df <- data.frame(feature_id = reps,cite_id = cites)
  return(df)
}

OUT <- data.frame(relation_id = c(1:nrow(OUT)),OUT)









