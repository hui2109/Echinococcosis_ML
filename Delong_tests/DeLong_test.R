library(pROC)
computeDelong <- function(y_true, y_score1, y_score2){
  roc1 <- roc(y_true, y_score1)
  roc2 <- roc(y_true, y_score2)
  delong_res <- roc.test(roc1, roc2, method="delong")
  return(list(roc1, roc2, delong_res))
}

############################################1
val_ML_RF <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/random_val_results_mk.csv')
val_DL <- read.csv('./resources/results/DL/validation.csv')
res_val_ML_RF = computeDelong(val_ML_RF[, "Label"], val_ML_RF[, "Pred"], val_DL[, "probs_1"])

val_ML_AE <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/random_val_results_mk.csv')
val_DL <- read.csv('./resources/results/DL/validation.csv')
res_val_ML_AE = computeDelong(val_ML_AE[, "Label"], val_ML_AE[, "Pred"], val_DL[, "probs_1"])
############################################1


############################################2
test_ML_RF <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/random_test_results_mk.csv')
test_DL <- read.csv('./resources/results/DL/test.csv')
res_test_ML_RF = computeDelong(test_ML_RF[, "Label"], test_ML_RF[, "Pred"], test_DL[, "probs_1"])

test_ML_AE <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/random_test_results_mk.csv')
test_DL <- read.csv('./resources/results/DL/test.csv')
res_test_ML_AE = computeDelong(test_ML_AE[, "Label"], test_ML_AE[, "Pred"], test_DL[, "probs_1"])
############################################2


############################################3
test_ML_RF <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/random_test_results_mk.csv')
test_DL <- read.csv('./resources/results/DL/test.csv')
res_test_ML_RF = computeDelong(test_ML_RF[, "Label"], test_ML_RF[, "Pred"], test_DL[, "probs_1"])

test_ML_AE <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/random_test_results_mk.csv')
test_DL <- read.csv('./resources/results/DL/test.csv')
res_test_ML_AE = computeDelong(test_ML_AE[, "Label"], test_ML_AE[, "Pred"], test_DL[, "probs_1"])
############################################3

