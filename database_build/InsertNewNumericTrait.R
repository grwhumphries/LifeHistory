##########################################################
######### Insert new feature into numerictraits ##########
##########################################################
library(dplyr)
library(foreach)


setwd("C:/LifeHistory/Lifehistory/database_build/CSVs_for_db/")
X <- read.csv("citation_numerictrait_species.csv")
Y <- tbl_df(read.csv("numeric_traits.csv"))


Y$mean <- as.double(as.character(Y$mean))
Y$traits <- as.character(Y$traits)
Y$dt <- as.character(Y$dt)

slist <- unique(Y$species_id)

newtrait <- "foraging distance"
units <- "km"

OUT <- foreach(x = slist, .combine='rbind') %do% {
  cat(x,'\n')
  Z <- Y %>% filter(species_id == as.character(x))
  row <- c((max(Z$feature_id)+1),as.character(x),newtrait,NA,NA,NA,units,NA,"citation311","grant","07/15/2016")
  O <- rbind(Z,row)
  return(O)
}

OUT$feature_id <- c(1:nrow(OUT))


write.csv(OUT,"numeric_traits.csv",row.names=F)

###############################################

setwd("C:/LifeHistory/Lifehistory/database_build/CSVs_for_db/")
X <- read.csv("species_citation.csv")
Y <- read.csv("numeric_traits.csv")


speclist <- unique(X$species_id)

OUT <- foreach(s = speclist,.combine='rbind') %do% {
  featureids <- Y$feature_id[which(Y$species_id == as.character(s))]
  J <- which(X$species_id == s)
  spcs <- length(J)
  reps <- rep(featureids,spcs)
  citeids <- as.character(X[J,3])
  cites<-unlist(lapply(citeids,function(x) rep(x,length(featureids))))
  df <- data.frame(feature_id = reps,cite_id = cites,species_id = as.character(s))
  return(df)
}

OUT <- data.frame(relation_id = c(1:nrow(OUT)),OUT)

write.csv(OUT,"citation_numerictrait_species.csv",row.names=F)














