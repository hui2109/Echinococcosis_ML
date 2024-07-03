
library(pROC)
sink('./DeLong_test_CUltra.txt')
lines = '################################################################################################'
computeDelong <- function(y_true, y_score1, y_score2){
  roc1 <- roc(y_true, y_score1)
  roc2 <- roc(y_true, y_score2)
  delong_res <- roc.test(roc1, roc2, method='delong')
  return(list(roc1 = roc1, roc2 = roc2, delong_res = delong_res))
}


################################################################################################
RFTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_38\\RF\\cv_val_prediction.csv')
SVMTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\MinMax\\PCA\\RFE_37\\SVM\\cv_val_prediction.csv')
RFTrain_VS_SVMTrain = computeDelong(RFTrain[, 'Label'], RFTrain[, 'Pred'], SVMTrain[, 'Pred'])
print(lines)
print('RFTrain_VS_SVMTrain')
RFTrain_VS_SVMTrain$delong_res$roc1
RFTrain_VS_SVMTrain$delong_res$roc2
RFTrain_VS_SVMTrain$delong_res
print(lines)
################################################################################################


################################################################################################
RFTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_38\\RF\\cv_val_prediction.csv')
AETrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_27\\AE\\cv_val_prediction.csv')
RFTrain_VS_AETrain = computeDelong(RFTrain[, 'Label'], RFTrain[, 'Pred'], AETrain[, 'Pred'])
print(lines)
print('RFTrain_VS_AETrain')
RFTrain_VS_AETrain$delong_res$roc1
RFTrain_VS_AETrain$delong_res$roc2
RFTrain_VS_AETrain$delong_res
print(lines)
################################################################################################


################################################################################################
RFTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_38\\RF\\cv_val_prediction.csv')
LDATrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCA\\RFE_39\\LDA\\cv_val_prediction.csv')
RFTrain_VS_LDATrain = computeDelong(RFTrain[, 'Label'], RFTrain[, 'Pred'], LDATrain[, 'Pred'])
print(lines)
print('RFTrain_VS_LDATrain')
RFTrain_VS_LDATrain$delong_res$roc1
RFTrain_VS_LDATrain$delong_res$roc2
RFTrain_VS_LDATrain$delong_res
print(lines)
################################################################################################


################################################################################################
RFTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_38\\RF\\cv_val_prediction.csv')
LRTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\MinMax\\PCA\\RFE_32\\LR\\cv_val_prediction.csv')
RFTrain_VS_LRTrain = computeDelong(RFTrain[, 'Label'], RFTrain[, 'Pred'], LRTrain[, 'Pred'])
print(lines)
print('RFTrain_VS_LRTrain')
RFTrain_VS_LRTrain$delong_res$roc1
RFTrain_VS_LRTrain$delong_res$roc2
RFTrain_VS_LRTrain$delong_res
print(lines)
################################################################################################


################################################################################################
RFTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_38\\RF\\cv_val_prediction.csv')
ABTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\RFE_33\\AB\\cv_val_prediction.csv')
RFTrain_VS_ABTrain = computeDelong(RFTrain[, 'Label'], RFTrain[, 'Pred'], ABTrain[, 'Pred'])
print(lines)
print('RFTrain_VS_ABTrain')
RFTrain_VS_ABTrain$delong_res$roc1
RFTrain_VS_ABTrain$delong_res$roc2
RFTrain_VS_ABTrain$delong_res
print(lines)
################################################################################################


################################################################################################
RFTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_38\\RF\\cv_val_prediction.csv')
DTTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\MinMax\\PCC\\RFE_30\\DT\\cv_val_prediction.csv')
RFTrain_VS_DTTrain = computeDelong(RFTrain[, 'Label'], RFTrain[, 'Pred'], DTTrain[, 'Pred'])
print(lines)
print('RFTrain_VS_DTTrain')
RFTrain_VS_DTTrain$delong_res$roc1
RFTrain_VS_DTTrain$delong_res$roc2
RFTrain_VS_DTTrain$delong_res
print(lines)
################################################################################################


################################################################################################
RFTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_38\\RF\\cv_val_prediction.csv')
NBTrain <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\MinMax\\PCA\\RFE_31\\NB\\cv_val_prediction.csv')
RFTrain_VS_NBTrain = computeDelong(RFTrain[, 'Label'], RFTrain[, 'Pred'], NBTrain[, 'Pred'])
print(lines)
print('RFTrain_VS_NBTrain')
RFTrain_VS_NBTrain$delong_res$roc1
RFTrain_VS_NBTrain$delong_res$roc2
RFTrain_VS_NBTrain$delong_res
print(lines)
################################################################################################


################################################################################################
RFTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\Relief_32\\RF\\test_prediction.csv')
SVMTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\MinMax\\PCA\\RFE_37\\SVM\\test_prediction.csv')
RFTest_VS_SVMTest = computeDelong(RFTest[, 'Label'], RFTest[, 'Pred'], SVMTest[, 'Pred'])
print(lines)
print('RFTest_VS_SVMTest')
RFTest_VS_SVMTest$delong_res$roc1
RFTest_VS_SVMTest$delong_res$roc2
RFTest_VS_SVMTest$delong_res
print(lines)
################################################################################################


################################################################################################
RFTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\Relief_32\\RF\\test_prediction.csv')
AETest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Zscore\\PCC\\RFE_27\\AE\\test_prediction.csv')
RFTest_VS_AETest = computeDelong(RFTest[, 'Label'], RFTest[, 'Pred'], AETest[, 'Pred'])
print(lines)
print('RFTest_VS_AETest')
RFTest_VS_AETest$delong_res$roc1
RFTest_VS_AETest$delong_res$roc2
RFTest_VS_AETest$delong_res
print(lines)
################################################################################################


################################################################################################
RFTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\Relief_32\\RF\\test_prediction.csv')
LDATest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCA\\RFE_39\\LDA\\test_prediction.csv')
RFTest_VS_LDATest = computeDelong(RFTest[, 'Label'], RFTest[, 'Pred'], LDATest[, 'Pred'])
print(lines)
print('RFTest_VS_LDATest')
RFTest_VS_LDATest$delong_res$roc1
RFTest_VS_LDATest$delong_res$roc2
RFTest_VS_LDATest$delong_res
print(lines)
################################################################################################


################################################################################################
RFTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\Relief_32\\RF\\test_prediction.csv')
LRTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\MinMax\\PCA\\RFE_32\\LR\\test_prediction.csv')
RFTest_VS_LRTest = computeDelong(RFTest[, 'Label'], RFTest[, 'Pred'], LRTest[, 'Pred'])
print(lines)
print('RFTest_VS_LRTest')
RFTest_VS_LRTest$delong_res$roc1
RFTest_VS_LRTest$delong_res$roc2
RFTest_VS_LRTest$delong_res
print(lines)
################################################################################################


################################################################################################
RFTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\Relief_32\\RF\\test_prediction.csv')
ABTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\RFE_33\\AB\\test_prediction.csv')
RFTest_VS_ABTest = computeDelong(RFTest[, 'Label'], RFTest[, 'Pred'], ABTest[, 'Pred'])
print(lines)
print('RFTest_VS_ABTest')
RFTest_VS_ABTest$delong_res$roc1
RFTest_VS_ABTest$delong_res$roc2
RFTest_VS_ABTest$delong_res
print(lines)
################################################################################################


################################################################################################
RFTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\Relief_32\\RF\\test_prediction.csv')
DTTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\MinMax\\PCC\\RFE_30\\DT\\test_prediction.csv')
RFTest_VS_DTTest = computeDelong(RFTest[, 'Label'], RFTest[, 'Pred'], DTTest[, 'Pred'])
print(lines)
print('RFTest_VS_DTTest')
RFTest_VS_DTTest$delong_res$roc1
RFTest_VS_DTTest$delong_res$roc2
RFTest_VS_DTTest$delong_res
print(lines)
################################################################################################


################################################################################################
RFTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\Mean\\PCC\\Relief_32\\RF\\test_prediction.csv')
NBTest <- read.csv('F:\\数据\\FAE\\huis_data\\results\\results2_合并\\MinMax\\PCA\\RFE_31\\NB\\test_prediction.csv')
RFTest_VS_NBTest = computeDelong(RFTest[, 'Label'], RFTest[, 'Pred'], NBTest[, 'Pred'])
print(lines)
print('RFTest_VS_NBTest')
RFTest_VS_NBTest$delong_res$roc1
RFTest_VS_NBTest$delong_res$roc2
RFTest_VS_NBTest$delong_res
print(lines)
################################################################################################

