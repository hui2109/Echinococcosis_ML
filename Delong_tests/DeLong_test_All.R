
library(pROC)
sink('./DeLong_test_All.txt')
lines = '################################################################################################'
computeDelong <- function(y_true, y_score1, y_score2){
  roc1 <- roc(y_true, y_score1)
  roc2 <- roc(y_true, y_score2)
  delong_res <- roc.test(roc1, roc2, method='delong')
  return(list(roc1 = roc1, roc2 = roc2, delong_res = delong_res))
}


################################################################################################
DL_val <- read.csv('./resources/results/DL/validation.csv')
ML_RF_val <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/random_val_results_mk.csv')
DL_val_VS_ML_RF_val = computeDelong(DL_val[, 'Label'], DL_val[, 'Score'], ML_RF_val[, 'Score'])
print(lines)
print('DL_val_VS_ML_RF_val')
DL_val_VS_ML_RF_val$delong_res$roc1
DL_val_VS_ML_RF_val$delong_res$roc2
DL_val_VS_ML_RF_val$delong_res
print(lines)
################################################################################################


################################################################################################
DL_val <- read.csv('./resources/results/DL/validation.csv')
ML_AE_val <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/random_val_results_mk.csv')
DL_val_VS_ML_AE_val = computeDelong(DL_val[, 'Label'], DL_val[, 'Score'], ML_AE_val[, 'Score'])
print(lines)
print('DL_val_VS_ML_AE_val')
DL_val_VS_ML_AE_val$delong_res$roc1
DL_val_VS_ML_AE_val$delong_res$roc2
DL_val_VS_ML_AE_val$delong_res
print(lines)
################################################################################################


################################################################################################
DL_test <- read.csv('./resources/results/DL/test.csv')
ML_RF_test <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/random_test_results_mk.csv')
DL_test_VS_ML_RF_test = computeDelong(DL_test[, 'Label'], DL_test[, 'Score'], ML_RF_test[, 'Score'])
print(lines)
print('DL_test_VS_ML_RF_test')
DL_test_VS_ML_RF_test$delong_res$roc1
DL_test_VS_ML_RF_test$delong_res$roc2
DL_test_VS_ML_RF_test$delong_res
print(lines)
################################################################################################


################################################################################################
DL_test <- read.csv('./resources/results/DL/test.csv')
ML_AE_test <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/random_test_results_mk.csv')
DL_test_VS_ML_AE_test = computeDelong(DL_test[, 'Label'], DL_test[, 'Score'], ML_AE_test[, 'Score'])
print(lines)
print('DL_test_VS_ML_AE_test')
DL_test_VS_ML_AE_test$delong_res$roc1
DL_test_VS_ML_AE_test$delong_res$roc2
DL_test_VS_ML_AE_test$delong_res
print(lines)
################################################################################################


################################################################################################
DL_inves <- read.csv('./resources/results/DL/inves_2022_mk.csv')
ML_RF_inves <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/inves_2023_mk.csv')
DL_inves_VS_ML_RF_inves = computeDelong(DL_inves[, 'Label'], DL_inves[, 'Score'], ML_RF_inves[, 'Score'])
print(lines)
print('DL_inves_VS_ML_RF_inves')
DL_inves_VS_ML_RF_inves$delong_res$roc1
DL_inves_VS_ML_RF_inves$delong_res$roc2
DL_inves_VS_ML_RF_inves$delong_res
print(lines)
################################################################################################


################################################################################################
DL_inves <- read.csv('./resources/results/DL/inves_2022_mk.csv')
ML_AE_inves <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/inves_2023_mk.csv')
DL_inves_VS_ML_AE_inves = computeDelong(DL_inves[, 'Label'], DL_inves[, 'Score'], ML_AE_inves[, 'Score'])
print(lines)
print('DL_inves_VS_ML_AE_inves')
DL_inves_VS_ML_AE_inves$delong_res$roc1
DL_inves_VS_ML_AE_inves$delong_res$roc2
DL_inves_VS_ML_AE_inves$delong_res
print(lines)
################################################################################################


################################################################################################
DL_inves <- read.csv('./resources/results/DL/inves_2022_mk.csv')
External_junior_E <- read.csv('./resources/results/External/junior_E/mk_2022_inves.csv')
DL_inves_VS_External_junior_E = computeDelong(DL_inves[, 'Label'], DL_inves[, 'Score'], External_junior_E[, 'Score'])
print(lines)
print('DL_inves_VS_External_junior_E')
DL_inves_VS_External_junior_E$delong_res$roc1
DL_inves_VS_External_junior_E$delong_res$roc2
DL_inves_VS_External_junior_E$delong_res
print(lines)
################################################################################################


################################################################################################
DL_inves <- read.csv('./resources/results/DL/inves_2022_mk.csv')
External_junior_NE <- read.csv('./resources/results/External/junior_NE/mk_2022_inves.csv')
DL_inves_VS_External_junior_NE = computeDelong(DL_inves[, 'Label'], DL_inves[, 'Score'], External_junior_NE[, 'Score'])
print(lines)
print('DL_inves_VS_External_junior_NE')
DL_inves_VS_External_junior_NE$delong_res$roc1
DL_inves_VS_External_junior_NE$delong_res$roc2
DL_inves_VS_External_junior_NE$delong_res
print(lines)
################################################################################################


################################################################################################
DL_inves <- read.csv('./resources/results/DL/inves_2022_mk.csv')
External_middle_E <- read.csv('./resources/results/External/middle_E/mk_2022_inves.csv')
DL_inves_VS_External_middle_E = computeDelong(DL_inves[, 'Label'], DL_inves[, 'Score'], External_middle_E[, 'Score'])
print(lines)
print('DL_inves_VS_External_middle_E')
DL_inves_VS_External_middle_E$delong_res$roc1
DL_inves_VS_External_middle_E$delong_res$roc2
DL_inves_VS_External_middle_E$delong_res
print(lines)
################################################################################################


################################################################################################
DL_inves <- read.csv('./resources/results/DL/inves_2022_mk.csv')
External_middle_NE <- read.csv('./resources/results/External/middle_NE/mk_2022_inves.csv')
DL_inves_VS_External_middle_NE = computeDelong(DL_inves[, 'Label'], DL_inves[, 'Score'], External_middle_NE[, 'Score'])
print(lines)
print('DL_inves_VS_External_middle_NE')
DL_inves_VS_External_middle_NE$delong_res$roc1
DL_inves_VS_External_middle_NE$delong_res$roc2
DL_inves_VS_External_middle_NE$delong_res
print(lines)
################################################################################################


################################################################################################
DL_inves <- read.csv('./resources/results/DL/inves_2022_mk.csv')
External_senior_E <- read.csv('./resources/results/External/senior_E/mk_2022_inves.csv')
DL_inves_VS_External_senior_E = computeDelong(DL_inves[, 'Label'], DL_inves[, 'Score'], External_senior_E[, 'Score'])
print(lines)
print('DL_inves_VS_External_senior_E')
DL_inves_VS_External_senior_E$delong_res$roc1
DL_inves_VS_External_senior_E$delong_res$roc2
DL_inves_VS_External_senior_E$delong_res
print(lines)
################################################################################################


################################################################################################
DL_inves <- read.csv('./resources/results/DL/inves_2022_mk.csv')
External_senior_NE <- read.csv('./resources/results/External/senior_NE/mk_2022_inves.csv')
DL_inves_VS_External_senior_NE = computeDelong(DL_inves[, 'Label'], DL_inves[, 'Score'], External_senior_NE[, 'Score'])
print(lines)
print('DL_inves_VS_External_senior_NE')
DL_inves_VS_External_senior_NE$delong_res$roc1
DL_inves_VS_External_senior_NE$delong_res$roc2
DL_inves_VS_External_senior_NE$delong_res
print(lines)
################################################################################################


################################################################################################
ML_RF_inves <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/inves_2023_mk.csv')
External_junior_E <- read.csv('./resources/results/External/junior_E/mk_2022_inves.csv')
ML_RF_inves_VS_External_junior_E = computeDelong(ML_RF_inves[, 'Label'], ML_RF_inves[, 'Score'], External_junior_E[, 'Score'])
print(lines)
print('ML_RF_inves_VS_External_junior_E')
ML_RF_inves_VS_External_junior_E$delong_res$roc1
ML_RF_inves_VS_External_junior_E$delong_res$roc2
ML_RF_inves_VS_External_junior_E$delong_res
print(lines)
################################################################################################


################################################################################################
ML_RF_inves <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/inves_2023_mk.csv')
External_junior_NE <- read.csv('./resources/results/External/junior_NE/mk_2022_inves.csv')
ML_RF_inves_VS_External_junior_NE = computeDelong(ML_RF_inves[, 'Label'], ML_RF_inves[, 'Score'], External_junior_NE[, 'Score'])
print(lines)
print('ML_RF_inves_VS_External_junior_NE')
ML_RF_inves_VS_External_junior_NE$delong_res$roc1
ML_RF_inves_VS_External_junior_NE$delong_res$roc2
ML_RF_inves_VS_External_junior_NE$delong_res
print(lines)
################################################################################################


################################################################################################
ML_RF_inves <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/inves_2023_mk.csv')
External_middle_E <- read.csv('./resources/results/External/middle_E/mk_2022_inves.csv')
ML_RF_inves_VS_External_middle_E = computeDelong(ML_RF_inves[, 'Label'], ML_RF_inves[, 'Score'], External_middle_E[, 'Score'])
print(lines)
print('ML_RF_inves_VS_External_middle_E')
ML_RF_inves_VS_External_middle_E$delong_res$roc1
ML_RF_inves_VS_External_middle_E$delong_res$roc2
ML_RF_inves_VS_External_middle_E$delong_res
print(lines)
################################################################################################


################################################################################################
ML_RF_inves <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/inves_2023_mk.csv')
External_middle_NE <- read.csv('./resources/results/External/middle_NE/mk_2022_inves.csv')
ML_RF_inves_VS_External_middle_NE = computeDelong(ML_RF_inves[, 'Label'], ML_RF_inves[, 'Score'], External_middle_NE[, 'Score'])
print(lines)
print('ML_RF_inves_VS_External_middle_NE')
ML_RF_inves_VS_External_middle_NE$delong_res$roc1
ML_RF_inves_VS_External_middle_NE$delong_res$roc2
ML_RF_inves_VS_External_middle_NE$delong_res
print(lines)
################################################################################################


################################################################################################
ML_RF_inves <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/inves_2023_mk.csv')
External_senior_E <- read.csv('./resources/results/External/senior_E/mk_2022_inves.csv')
ML_RF_inves_VS_External_senior_E = computeDelong(ML_RF_inves[, 'Label'], ML_RF_inves[, 'Score'], External_senior_E[, 'Score'])
print(lines)
print('ML_RF_inves_VS_External_senior_E')
ML_RF_inves_VS_External_senior_E$delong_res$roc1
ML_RF_inves_VS_External_senior_E$delong_res$roc2
ML_RF_inves_VS_External_senior_E$delong_res
print(lines)
################################################################################################


################################################################################################
ML_RF_inves <- read.csv('./resources/results/ML/Mean_PCC_KW_24_RF/inves_2023_mk.csv')
External_senior_NE <- read.csv('./resources/results/External/senior_NE/mk_2022_inves.csv')
ML_RF_inves_VS_External_senior_NE = computeDelong(ML_RF_inves[, 'Label'], ML_RF_inves[, 'Score'], External_senior_NE[, 'Score'])
print(lines)
print('ML_RF_inves_VS_External_senior_NE')
ML_RF_inves_VS_External_senior_NE$delong_res$roc1
ML_RF_inves_VS_External_senior_NE$delong_res$roc2
ML_RF_inves_VS_External_senior_NE$delong_res
print(lines)
################################################################################################


################################################################################################
ML_AE_inves <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/inves_2023_mk.csv')
External_junior_E <- read.csv('./resources/results/External/junior_E/mk_2022_inves.csv')
ML_AE_inves_VS_External_junior_E = computeDelong(ML_AE_inves[, 'Label'], ML_AE_inves[, 'Score'], External_junior_E[, 'Score'])
print(lines)
print('ML_AE_inves_VS_External_junior_E')
ML_AE_inves_VS_External_junior_E$delong_res$roc1
ML_AE_inves_VS_External_junior_E$delong_res$roc2
ML_AE_inves_VS_External_junior_E$delong_res
print(lines)
################################################################################################


################################################################################################
ML_AE_inves <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/inves_2023_mk.csv')
External_junior_NE <- read.csv('./resources/results/External/junior_NE/mk_2022_inves.csv')
ML_AE_inves_VS_External_junior_NE = computeDelong(ML_AE_inves[, 'Label'], ML_AE_inves[, 'Score'], External_junior_NE[, 'Score'])
print(lines)
print('ML_AE_inves_VS_External_junior_NE')
ML_AE_inves_VS_External_junior_NE$delong_res$roc1
ML_AE_inves_VS_External_junior_NE$delong_res$roc2
ML_AE_inves_VS_External_junior_NE$delong_res
print(lines)
################################################################################################


################################################################################################
ML_AE_inves <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/inves_2023_mk.csv')
External_middle_E <- read.csv('./resources/results/External/middle_E/mk_2022_inves.csv')
ML_AE_inves_VS_External_middle_E = computeDelong(ML_AE_inves[, 'Label'], ML_AE_inves[, 'Score'], External_middle_E[, 'Score'])
print(lines)
print('ML_AE_inves_VS_External_middle_E')
ML_AE_inves_VS_External_middle_E$delong_res$roc1
ML_AE_inves_VS_External_middle_E$delong_res$roc2
ML_AE_inves_VS_External_middle_E$delong_res
print(lines)
################################################################################################


################################################################################################
ML_AE_inves <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/inves_2023_mk.csv')
External_middle_NE <- read.csv('./resources/results/External/middle_NE/mk_2022_inves.csv')
ML_AE_inves_VS_External_middle_NE = computeDelong(ML_AE_inves[, 'Label'], ML_AE_inves[, 'Score'], External_middle_NE[, 'Score'])
print(lines)
print('ML_AE_inves_VS_External_middle_NE')
ML_AE_inves_VS_External_middle_NE$delong_res$roc1
ML_AE_inves_VS_External_middle_NE$delong_res$roc2
ML_AE_inves_VS_External_middle_NE$delong_res
print(lines)
################################################################################################


################################################################################################
ML_AE_inves <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/inves_2023_mk.csv')
External_senior_E <- read.csv('./resources/results/External/senior_E/mk_2022_inves.csv')
ML_AE_inves_VS_External_senior_E = computeDelong(ML_AE_inves[, 'Label'], ML_AE_inves[, 'Score'], External_senior_E[, 'Score'])
print(lines)
print('ML_AE_inves_VS_External_senior_E')
ML_AE_inves_VS_External_senior_E$delong_res$roc1
ML_AE_inves_VS_External_senior_E$delong_res$roc2
ML_AE_inves_VS_External_senior_E$delong_res
print(lines)
################################################################################################


################################################################################################
ML_AE_inves <- read.csv('./resources/results/ML/Zscore_PCC_KW_29_AE/inves_2023_mk.csv')
External_senior_NE <- read.csv('./resources/results/External/senior_NE/mk_2022_inves.csv')
ML_AE_inves_VS_External_senior_NE = computeDelong(ML_AE_inves[, 'Label'], ML_AE_inves[, 'Score'], External_senior_NE[, 'Score'])
print(lines)
print('ML_AE_inves_VS_External_senior_NE')
ML_AE_inves_VS_External_senior_NE$delong_res$roc1
ML_AE_inves_VS_External_senior_NE$delong_res$roc2
ML_AE_inves_VS_External_senior_NE$delong_res
print(lines)
################################################################################################


################################################################################################
VGG_val <- read.csv('./resources/results/DL/validation.csv')
Efficient_val <- read.csv('./resources/results/DL/efficientnetb0_rmsprop/validation.csv')
VGG_val_VS_Efficient_val = computeDelong(VGG_val[, 'Label'], VGG_val[, 'Score'], Efficient_val[, 'Score'])
print(lines)
print('VGG_val_VS_Efficient_val')
VGG_val_VS_Efficient_val$delong_res$roc1
VGG_val_VS_Efficient_val$delong_res$roc2
VGG_val_VS_Efficient_val$delong_res
print(lines)
################################################################################################


################################################################################################
VGG_val <- read.csv('./resources/results/DL/validation.csv')
Inception_val <- read.csv('./resources/results/DL/inceptionv3_rmsprop/validation.csv')
VGG_val_VS_Inception_val = computeDelong(VGG_val[, 'Label'], VGG_val[, 'Score'], Inception_val[, 'Score'])
print(lines)
print('VGG_val_VS_Inception_val')
VGG_val_VS_Inception_val$delong_res$roc1
VGG_val_VS_Inception_val$delong_res$roc2
VGG_val_VS_Inception_val$delong_res
print(lines)
################################################################################################


################################################################################################
VGG_val <- read.csv('./resources/results/DL/validation.csv')
ResNet_val <- read.csv('./resources/results/DL/resnet50_adam/validation.csv')
VGG_val_VS_ResNet_val = computeDelong(VGG_val[, 'Label'], VGG_val[, 'Score'], ResNet_val[, 'Score'])
print(lines)
print('VGG_val_VS_ResNet_val')
VGG_val_VS_ResNet_val$delong_res$roc1
VGG_val_VS_ResNet_val$delong_res$roc2
VGG_val_VS_ResNet_val$delong_res
print(lines)
################################################################################################


################################################################################################
VGG_test <- read.csv('./resources/results/DL/test.csv')
Efficient_test <- read.csv('./resources/results/DL/efficientnetb0_rmsprop/test.csv')
VGG_test_VS_Efficient_test = computeDelong(VGG_test[, 'Label'], VGG_test[, 'Score'], Efficient_test[, 'Score'])
print(lines)
print('VGG_test_VS_Efficient_test')
VGG_test_VS_Efficient_test$delong_res$roc1
VGG_test_VS_Efficient_test$delong_res$roc2
VGG_test_VS_Efficient_test$delong_res
print(lines)
################################################################################################


################################################################################################
VGG_test <- read.csv('./resources/results/DL/test.csv')
Inception_test <- read.csv('./resources/results/DL/inceptionv3_rmsprop/test.csv')
VGG_test_VS_Inception_test = computeDelong(VGG_test[, 'Label'], VGG_test[, 'Score'], Inception_test[, 'Score'])
print(lines)
print('VGG_test_VS_Inception_test')
VGG_test_VS_Inception_test$delong_res$roc1
VGG_test_VS_Inception_test$delong_res$roc2
VGG_test_VS_Inception_test$delong_res
print(lines)
################################################################################################


################################################################################################
VGG_test <- read.csv('./resources/results/DL/test.csv')
ResNet_test <- read.csv('./resources/results/DL/resnet50_adam/test.csv')
VGG_test_VS_ResNet_test = computeDelong(VGG_test[, 'Label'], VGG_test[, 'Score'], ResNet_test[, 'Score'])
print(lines)
print('VGG_test_VS_ResNet_test')
VGG_test_VS_ResNet_test$delong_res$roc1
VGG_test_VS_ResNet_test$delong_res$roc2
VGG_test_VS_ResNet_test$delong_res
print(lines)
################################################################################################



























