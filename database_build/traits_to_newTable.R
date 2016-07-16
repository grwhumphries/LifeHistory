library(dplyr)
library(foreach)
setwd("C:/LifeHistory/database_build/")

X <- read.csv("traits_new.csv")
Y <- names(X)


### Selects mean, uppers and lowers column names

meansvals <- lapply(Y,function(x) grep(pattern="*mean",x))
means <- Y[which(meansvals == 1)]

rangevals <- lapply(Y,function(x) grep(pattern="*range",x))
ranges <- Y[which(rangevals == 1)]

uncertvals <- lapply(Y,function(x) grep(pattern="*uncertainty",x))
uncert <- Y[which(uncertvals == 1)]

### Bind together the others, and find all variables that aren't in that list already

Z <- c(means,ranges,uncert)
Ytb <- tbl_df(data.frame(Y))
others <- Ytb %>% filter(!Y %in% Z)
othervars <- c(as.character(others$Y))[3:(nrow(others)-3)]

############################################################################################
## trim "mean" off var names ##

vars1 <- sapply(1:length(means), function(x) substr(means[[x]],1,(nchar(means[[x]])-5)))

#### Merge vars together
varnames1 <- c(vars1)
varnames <- gsub("_"," ",varnames1)


## Create varname field
traits <- rep(varnames,nrow(X))
species_ids <- as.character(unlist(lapply(X$species_id, function(x) rep(x,length(varnames)))))


####################
df <- data.frame(feature_id = c(1:length(traits)), species_id = species_ids, traits = traits, mean=rep(NA,length(varnames)),range=rep(NA,length(varnames)),uncertainty=rep(NA,length(varnames)))


##################
### Now we loop through the species ids
### Within that loop, we pull the appropriate row so we can append to df




for(i in 1:nrow(X)){
  cat(i,"\n")
  INDEX <- which(df$species_id ==X$species_id[i])
  
  OUT <- foreach(j = varnames1,.combine='rbind') %do%{
    pattern <- paste("\\b",j,"*",sep="")
    dat <- X[i,Y[which(lapply(Y,function(x) grep(pattern=pattern,x)) == 1)]]
    names(dat)<-c("mean","range","uncertainty")
    dat$mean<-as.character(dat$mean)
    dat$range<-as.character(dat$range)
    dat$uncertainty<-as.character(dat$uncertainty)
    return(dat)
  }
  df$mean[INDEX] <- OUT$mean
  df$range[INDEX] <- OUT$range
  df$uncertainty[INDEX] <- OUT$uncertainty
}




write.csv(df,"newtraits.csv",row.names=F)



#####################################################################################################
library(reshape2)
library(dplyr)
library(foreach)
setwd("C:/LifeHistory/database_build/")

X <- tbl_df(read.csv("OtherData.csv"))
df <- X %>% select(-comments,-username,-dt)

df2<-melt(df, id.vars=c("species_id"))

df2 <- data.frame(trtid = c(1:nrow(df2)),df2)
df2$comments <- rep(NA,nrow(df2))
df2$username <- rep('grant',nrow(df2))
df2$dt <- rep('17/07/2016',nrow(df2))
df2$variable <- gsub("_"," ",df2$variable)






