library(pROC)
sink('./DeLong_test_BetweenVal.txt')
lines = '################################################################################################'
computeDelong <- function(y_true, y_score1, y_score2){
  roc1 <- roc(y_true, y_score1)
  roc2 <- roc(y_true, y_score2)
  delong_res <- roc.test(roc1, roc2, method='delong')
  return(list(roc1 = roc1, roc2 = roc2, delong_res = delong_res))
}


################################################################################################
External_junior_E <- read.csv('./resources/results/External/junior_E/mk_2022_inves.csv')
External_junior_NE <- read.csv('./resources/results/External/junior_NE/mk_2022_inves.csv')
External_junior_E_VS_External_junior_NE = computeDelong(External_junior_E[, 'Label'], External_junior_E[, 'Score'], External_junior_NE[, 'Score'])
print(lines)
print('External_junior_E_VS_External_junior_NE')
External_junior_E_VS_External_junior_NE$delong_res$roc1
External_junior_E_VS_External_junior_NE$delong_res$roc2
External_junior_E_VS_External_junior_NE$delong_res
print(lines)
################################################################################################


################################################################################################
External_middle_E <- read.csv('./resources/results/External/middle_E/mk_2022_inves.csv')
External_middle_NE <- read.csv('./resources/results/External/middle_NE/mk_2022_inves.csv')
External_middle_E_VS_External_middle_NE = computeDelong(External_middle_E[, 'Label'], External_middle_E[, 'Score'], External_middle_NE[, 'Score'])
print(lines)
print('External_middle_E_VS_External_middle_NE')
External_middle_E_VS_External_middle_NE$delong_res$roc1
External_middle_E_VS_External_middle_NE$delong_res$roc2
External_middle_E_VS_External_middle_NE$delong_res
print(lines)
################################################################################################


################################################################################################
External_senior_E <- read.csv('./resources/results/External/senior_E/mk_2022_inves.csv')
External_senior_NE <- read.csv('./resources/results/External/senior_NE/mk_2022_inves.csv')
External_senior_E_VS_External_senior_NE = computeDelong(External_senior_E[, 'Label'], External_senior_E[, 'Score'], External_senior_NE[, 'Score'])
print(lines)
print('External_senior_E_VS_External_senior_NE')
External_senior_E_VS_External_senior_NE$delong_res$roc1
External_senior_E_VS_External_senior_NE$delong_res$roc2
External_senior_E_VS_External_senior_NE$delong_res
print(lines)
################################################################################################


################################################################################################
External_E <- read.csv('./resources/results/External/Mean_E/mk_2022_inves.csv')
External_NE <- read.csv('./resources/results/External/Mean_NE/mk_2022_inves.csv')
External_E_VS_External_NE = computeDelong(External_E[, 'Label'], External_E[, 'Score'], External_NE[, 'Score'])
print(lines)
print('External_E_VS_External_NE')
External_E_VS_External_NE$delong_res$roc1
External_E_VS_External_NE$delong_res$roc2
External_E_VS_External_NE$delong_res
print(lines)
################################################################################################

