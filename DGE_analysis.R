library(edgeR)

# Read in expression values
setwd("~/Documents/School/Search_Pattern/frontal_lobe_mrna_db/data")
expr_values <- read.csv('merged_values.txt', row.names = 1, header = TRUE)

# Remove rows with NA values
expr_values <- na.omit(expr_values)

# Create DGEList object
dge <- DGEList(expr_values)

# Calculate normalization factors
dge <- calcNormFactors(dge)

coldata <- factor(c(rep("adult", 76),  rep("dev", 21) ))

# Multidimensional scaling plot
plotMDS(dge, col=as.numeric(coldata))


# Voom transformation
model_m <- model.matrix(~0 + coldata)

x <- voom(dge, model_m, plot = T)

# fit expression values to linear model

fit <- lmFit(x, model_m)

contr <- makeContrasts(coldatadev - coldataadult, levels = colnames(coef(fit)))

tmp <- contrasts.fit(fit, contr)

tmp <- eBayes(tmp)


