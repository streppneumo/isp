
library(Biobase)
library(GEOquery)

# a list of all the GEO accession numbers
geo.names <- c("GDS3572","GDS3562","GDS3251","GDS3174","GDS2870","GDS2869",
               "GDS2764","GDS2502",
               "GDS2377","GDS2317","GDS2111","GDS1910","GDS1469")

# not used:  "GDS2377","GDS2111","GDS1910","GDS1469"

# retreive GDS objects for each geo.name
geo.sets <- lapply(geo.names,getGEO)
# convert the GDS objects into expression sets
esets <- lapply(geo.sets,function(x) GDS2eSet(x,do.log2=TRUE))


# below is all Pseudomonas aeruginosa specific stuff

is.row.name <- function(x) (regexpr("PA\\d{4,4}",x) > 0)

trim.row.name <- function(x) {
  if (regexpr("PA\\d{4,4}",x) > 0) {
    substr(x,1,6)
  } else {
    x
  }
}

# pull out only genes in CORES
create.gene.subset <- function(e) {
  e <- as.data.frame(e)
  e <- t(e[,vapply(names(e),is.row.name,TRUE)])
  
  row.names(e) <- vapply(row.names(e),trim.row.name,"")
  sub.e <- e[vapply(row.names(e),is.row.name,TRUE),]
}

# reduce the esets to only have these genes
esets <- lapply(esets,create.gene.subset)

# combines the expression data from two esets into a matrix
combine.esets <- function(a,b) {
  e <- merge(a,b,by=0)
  row.names(e) <- e[,1]
  e <- e[,-1]
}

# reduce all of the esets to a single matrix
eset <- Reduce(combine.esets,esets)

# normalize the expression data
norm.eset <- apply(eset,2,function(x){x[is.na(x)] <- 0; (x - mean(x))/sd(x)})

# bring in the cores
pao.raw.cores <- as.matrix(read.csv("rxn_cores.csv",header=TRUE))
# remove cores with only one enzyme
pao.cores <- pao.raw.cores[apply(pao.raw.cores,1,sum) > 1,]
pao.genes <- dimnames(pao.raw.cores)[[2]]
# find genes with complete expression
in.eset <- pao.genes %in% row.names(eset)
in.a.core <- apply(pao.cores,2,sum) > 0

pao.genes <- pao.genes[in.eset]
pao.cores <- pao.cores[,in.eset]

eset <- norm.eset[pao.genes,]

# testing for the cores ==================================
remove.diag <- function(x) {
  dims <- dim(x)
  to.remove <- seq(1,prod(dims),dims[[2]])
  as.vector(x)[-to.remove]
}
  
test.core <- function(core,eset) {
  core <- as.logical(core)
  e.in <- eset[core,]
  e.out <- eset[!core,]
  x <- remove.diag(cor(t(e.in)))
  y <- remove.diag(cor(t(e.out)))
  t.test(x=x,y=y,alternative="greater")
}

ts <- apply(pao.cores,1,function(x) test.core(x,eset))
p.vals <- vapply(ts,function(x) x$p.value,0)
print(sum(p.vals < 0.05))

# magic happens here (transpose to calculate between genes, the rows)
r <- cor(t(eset))

test.in.out <- function(core,r) {
  core <- as.logical(core)
  r.in <- r[core,core]
  x <- remove.diag(r.in)
  r.out <- r[!core,!core]
  y <- as.vector(r.out)
  t <- t.test(x=x,y=y,alternative="greater")
  print(t)
  return(t)
}
test.in.vs <- function(core,r) {
  core <- as.logical(core)
  r.in <- r[core,core]
  x <- remove.diag(r.in)
  r.out <- r[core,!core]
  y <- as.vector(r.out)
  t <- t.test(x=x,y=y,alternative="greater")
  print(t)
  return(t)
}

ts.in.out <- apply(pao.cores,1,function(x) test.in.out(x,r))
p.vals.in.out <- vapply(ts.in.out,function(x) x$p.value,0)
print(sum(p.vals.in.out < 0.05))

ts.in.vs <- apply(pao.cores,1,function(x) test.in.vs(x,r))
p.vals.in.vs <- vapply(ts.in.vs,function(x) x$p.value,0)
print(sum(p.vals.in.vs < 0.05))

print(sum(p.vals.in.out < 0.05 & p.vals.in.vs < 0.05))

hist(as.vector(r))
  