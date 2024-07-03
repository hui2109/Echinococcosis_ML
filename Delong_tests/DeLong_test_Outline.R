library(pROC)
sink('./DeLong_test_Outline.txt')
lines = '################################################################################################'
computeDelong <- function(y_true, y_score1, y_score2){
  roc1 <- roc(y_true, y_score1)
  roc2 <- roc(y_true, y_score2)
  delong_res <- roc.test(roc1, roc2, method='delong')
  return(list(roc1 = roc1, roc2 = roc2, delong_res = delong_res))
}


################################################################################################
outline_SVM_p1 <- read.csv('./resources/results/outlines/SVM/val/p1.csv')
outline_SVM_p2 <- read.csv('./resources/results/outlines/SVM/val/p2.csv')
outline_SVM_p1_VS_outline_SVM_p2 = computeDelong(outline_SVM_p1[, 'Label'], outline_SVM_p1[, 'Score'], outline_SVM_p2[, 'Score'])
print(lines)
print('outline_SVM_p1_VS_outline_SVM_p2')
outline_SVM_p1_VS_outline_SVM_p2$delong_res$roc1
outline_SVM_p1_VS_outline_SVM_p2$delong_res$roc2
outline_SVM_p1_VS_outline_SVM_p2$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p1 <- read.csv('./resources/results/outlines/SVM/val/p1.csv')
outline_SVM_p3 <- read.csv('./resources/results/outlines/SVM/val/p3.csv')
outline_SVM_p1_VS_outline_SVM_p3 = computeDelong(outline_SVM_p1[, 'Label'], outline_SVM_p1[, 'Score'], outline_SVM_p3[, 'Score'])
print(lines)
print('outline_SVM_p1_VS_outline_SVM_p3')
outline_SVM_p1_VS_outline_SVM_p3$delong_res$roc1
outline_SVM_p1_VS_outline_SVM_p3$delong_res$roc2
outline_SVM_p1_VS_outline_SVM_p3$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p1 <- read.csv('./resources/results/outlines/SVM/val/p1.csv')
outline_SVM_p4 <- read.csv('./resources/results/outlines/SVM/val/p4.csv')
outline_SVM_p1_VS_outline_SVM_p4 = computeDelong(outline_SVM_p1[, 'Label'], outline_SVM_p1[, 'Score'], outline_SVM_p4[, 'Score'])
print(lines)
print('outline_SVM_p1_VS_outline_SVM_p4')
outline_SVM_p1_VS_outline_SVM_p4$delong_res$roc1
outline_SVM_p1_VS_outline_SVM_p4$delong_res$roc2
outline_SVM_p1_VS_outline_SVM_p4$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p1 <- read.csv('./resources/results/outlines/SVM/val/p1.csv')
outline_SVM_p5 <- read.csv('./resources/results/outlines/SVM/val/p5.csv')
outline_SVM_p1_VS_outline_SVM_p5 = computeDelong(outline_SVM_p1[, 'Label'], outline_SVM_p1[, 'Score'], outline_SVM_p5[, 'Score'])
print(lines)
print('outline_SVM_p1_VS_outline_SVM_p5')
outline_SVM_p1_VS_outline_SVM_p5$delong_res$roc1
outline_SVM_p1_VS_outline_SVM_p5$delong_res$roc2
outline_SVM_p1_VS_outline_SVM_p5$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p1 <- read.csv('./resources/results/outlines/SVM/val/p1.csv')
outline_SVM_p6 <- read.csv('./resources/results/outlines/SVM/val/p6.csv')
outline_SVM_p1_VS_outline_SVM_p6 = computeDelong(outline_SVM_p1[, 'Label'], outline_SVM_p1[, 'Score'], outline_SVM_p6[, 'Score'])
print(lines)
print('outline_SVM_p1_VS_outline_SVM_p6')
outline_SVM_p1_VS_outline_SVM_p6$delong_res$roc1
outline_SVM_p1_VS_outline_SVM_p6$delong_res$roc2
outline_SVM_p1_VS_outline_SVM_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p2 <- read.csv('./resources/results/outlines/SVM/val/p2.csv')
outline_SVM_p3 <- read.csv('./resources/results/outlines/SVM/val/p3.csv')
outline_SVM_p2_VS_outline_SVM_p3 = computeDelong(outline_SVM_p2[, 'Label'], outline_SVM_p2[, 'Score'], outline_SVM_p3[, 'Score'])
print(lines)
print('outline_SVM_p2_VS_outline_SVM_p3')
outline_SVM_p2_VS_outline_SVM_p3$delong_res$roc1
outline_SVM_p2_VS_outline_SVM_p3$delong_res$roc2
outline_SVM_p2_VS_outline_SVM_p3$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p2 <- read.csv('./resources/results/outlines/SVM/val/p2.csv')
outline_SVM_p4 <- read.csv('./resources/results/outlines/SVM/val/p4.csv')
outline_SVM_p2_VS_outline_SVM_p4 = computeDelong(outline_SVM_p2[, 'Label'], outline_SVM_p2[, 'Score'], outline_SVM_p4[, 'Score'])
print(lines)
print('outline_SVM_p2_VS_outline_SVM_p4')
outline_SVM_p2_VS_outline_SVM_p4$delong_res$roc1
outline_SVM_p2_VS_outline_SVM_p4$delong_res$roc2
outline_SVM_p2_VS_outline_SVM_p4$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p2 <- read.csv('./resources/results/outlines/SVM/val/p2.csv')
outline_SVM_p5 <- read.csv('./resources/results/outlines/SVM/val/p5.csv')
outline_SVM_p2_VS_outline_SVM_p5 = computeDelong(outline_SVM_p2[, 'Label'], outline_SVM_p2[, 'Score'], outline_SVM_p5[, 'Score'])
print(lines)
print('outline_SVM_p2_VS_outline_SVM_p5')
outline_SVM_p2_VS_outline_SVM_p5$delong_res$roc1
outline_SVM_p2_VS_outline_SVM_p5$delong_res$roc2
outline_SVM_p2_VS_outline_SVM_p5$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p2 <- read.csv('./resources/results/outlines/SVM/val/p2.csv')
outline_SVM_p6 <- read.csv('./resources/results/outlines/SVM/val/p6.csv')
outline_SVM_p2_VS_outline_SVM_p6 = computeDelong(outline_SVM_p2[, 'Label'], outline_SVM_p2[, 'Score'], outline_SVM_p6[, 'Score'])
print(lines)
print('outline_SVM_p2_VS_outline_SVM_p6')
outline_SVM_p2_VS_outline_SVM_p6$delong_res$roc1
outline_SVM_p2_VS_outline_SVM_p6$delong_res$roc2
outline_SVM_p2_VS_outline_SVM_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p3 <- read.csv('./resources/results/outlines/SVM/val/p3.csv')
outline_SVM_p4 <- read.csv('./resources/results/outlines/SVM/val/p4.csv')
outline_SVM_p3_VS_outline_SVM_p4 = computeDelong(outline_SVM_p3[, 'Label'], outline_SVM_p3[, 'Score'], outline_SVM_p4[, 'Score'])
print(lines)
print('outline_SVM_p3_VS_outline_SVM_p4')
outline_SVM_p3_VS_outline_SVM_p4$delong_res$roc1
outline_SVM_p3_VS_outline_SVM_p4$delong_res$roc2
outline_SVM_p3_VS_outline_SVM_p4$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p3 <- read.csv('./resources/results/outlines/SVM/val/p3.csv')
outline_SVM_p5 <- read.csv('./resources/results/outlines/SVM/val/p5.csv')
outline_SVM_p3_VS_outline_SVM_p5 = computeDelong(outline_SVM_p3[, 'Label'], outline_SVM_p3[, 'Score'], outline_SVM_p5[, 'Score'])
print(lines)
print('outline_SVM_p3_VS_outline_SVM_p5')
outline_SVM_p3_VS_outline_SVM_p5$delong_res$roc1
outline_SVM_p3_VS_outline_SVM_p5$delong_res$roc2
outline_SVM_p3_VS_outline_SVM_p5$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p3 <- read.csv('./resources/results/outlines/SVM/val/p3.csv')
outline_SVM_p6 <- read.csv('./resources/results/outlines/SVM/val/p6.csv')
outline_SVM_p3_VS_outline_SVM_p6 = computeDelong(outline_SVM_p3[, 'Label'], outline_SVM_p3[, 'Score'], outline_SVM_p6[, 'Score'])
print(lines)
print('outline_SVM_p3_VS_outline_SVM_p6')
outline_SVM_p3_VS_outline_SVM_p6$delong_res$roc1
outline_SVM_p3_VS_outline_SVM_p6$delong_res$roc2
outline_SVM_p3_VS_outline_SVM_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p4 <- read.csv('./resources/results/outlines/SVM/val/p4.csv')
outline_SVM_p5 <- read.csv('./resources/results/outlines/SVM/val/p5.csv')
outline_SVM_p4_VS_outline_SVM_p5 = computeDelong(outline_SVM_p4[, 'Label'], outline_SVM_p4[, 'Score'], outline_SVM_p5[, 'Score'])
print(lines)
print('outline_SVM_p4_VS_outline_SVM_p5')
outline_SVM_p4_VS_outline_SVM_p5$delong_res$roc1
outline_SVM_p4_VS_outline_SVM_p5$delong_res$roc2
outline_SVM_p4_VS_outline_SVM_p5$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p4 <- read.csv('./resources/results/outlines/SVM/val/p4.csv')
outline_SVM_p6 <- read.csv('./resources/results/outlines/SVM/val/p6.csv')
outline_SVM_p4_VS_outline_SVM_p6 = computeDelong(outline_SVM_p4[, 'Label'], outline_SVM_p4[, 'Score'], outline_SVM_p6[, 'Score'])
print(lines)
print('outline_SVM_p4_VS_outline_SVM_p6')
outline_SVM_p4_VS_outline_SVM_p6$delong_res$roc1
outline_SVM_p4_VS_outline_SVM_p6$delong_res$roc2
outline_SVM_p4_VS_outline_SVM_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_SVM_p5 <- read.csv('./resources/results/outlines/SVM/val/p5.csv')
outline_SVM_p6 <- read.csv('./resources/results/outlines/SVM/val/p6.csv')
outline_SVM_p5_VS_outline_SVM_p6 = computeDelong(outline_SVM_p5[, 'Label'], outline_SVM_p5[, 'Score'], outline_SVM_p6[, 'Score'])
print(lines)
print('outline_SVM_p5_VS_outline_SVM_p6')
outline_SVM_p5_VS_outline_SVM_p6$delong_res$roc1
outline_SVM_p5_VS_outline_SVM_p6$delong_res$roc2
outline_SVM_p5_VS_outline_SVM_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p1 <- read.csv('./resources/results/outlines/ResNet/val/p1.csv')
outline_ResNet_p2 <- read.csv('./resources/results/outlines/ResNet/val/p2.csv')
outline_ResNet_p1_VS_outline_ResNet_p2 = computeDelong(outline_ResNet_p1[, 'Label'], outline_ResNet_p1[, 'Score'], outline_ResNet_p2[, 'Score'])
print(lines)
print('outline_ResNet_p1_VS_outline_ResNet_p2')
outline_ResNet_p1_VS_outline_ResNet_p2$delong_res$roc1
outline_ResNet_p1_VS_outline_ResNet_p2$delong_res$roc2
outline_ResNet_p1_VS_outline_ResNet_p2$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p1 <- read.csv('./resources/results/outlines/ResNet/val/p1.csv')
outline_ResNet_p3 <- read.csv('./resources/results/outlines/ResNet/val/p3.csv')
outline_ResNet_p1_VS_outline_ResNet_p3 = computeDelong(outline_ResNet_p1[, 'Label'], outline_ResNet_p1[, 'Score'], outline_ResNet_p3[, 'Score'])
print(lines)
print('outline_ResNet_p1_VS_outline_ResNet_p3')
outline_ResNet_p1_VS_outline_ResNet_p3$delong_res$roc1
outline_ResNet_p1_VS_outline_ResNet_p3$delong_res$roc2
outline_ResNet_p1_VS_outline_ResNet_p3$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p1 <- read.csv('./resources/results/outlines/ResNet/val/p1.csv')
outline_ResNet_p4 <- read.csv('./resources/results/outlines/ResNet/val/p4.csv')
outline_ResNet_p1_VS_outline_ResNet_p4 = computeDelong(outline_ResNet_p1[, 'Label'], outline_ResNet_p1[, 'Score'], outline_ResNet_p4[, 'Score'])
print(lines)
print('outline_ResNet_p1_VS_outline_ResNet_p4')
outline_ResNet_p1_VS_outline_ResNet_p4$delong_res$roc1
outline_ResNet_p1_VS_outline_ResNet_p4$delong_res$roc2
outline_ResNet_p1_VS_outline_ResNet_p4$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p1 <- read.csv('./resources/results/outlines/ResNet/val/p1.csv')
outline_ResNet_p5 <- read.csv('./resources/results/outlines/ResNet/val/p5.csv')
outline_ResNet_p1_VS_outline_ResNet_p5 = computeDelong(outline_ResNet_p1[, 'Label'], outline_ResNet_p1[, 'Score'], outline_ResNet_p5[, 'Score'])
print(lines)
print('outline_ResNet_p1_VS_outline_ResNet_p5')
outline_ResNet_p1_VS_outline_ResNet_p5$delong_res$roc1
outline_ResNet_p1_VS_outline_ResNet_p5$delong_res$roc2
outline_ResNet_p1_VS_outline_ResNet_p5$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p1 <- read.csv('./resources/results/outlines/ResNet/val/p1.csv')
outline_ResNet_p6 <- read.csv('./resources/results/outlines/ResNet/val/p6.csv')
outline_ResNet_p1_VS_outline_ResNet_p6 = computeDelong(outline_ResNet_p1[, 'Label'], outline_ResNet_p1[, 'Score'], outline_ResNet_p6[, 'Score'])
print(lines)
print('outline_ResNet_p1_VS_outline_ResNet_p6')
outline_ResNet_p1_VS_outline_ResNet_p6$delong_res$roc1
outline_ResNet_p1_VS_outline_ResNet_p6$delong_res$roc2
outline_ResNet_p1_VS_outline_ResNet_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p2 <- read.csv('./resources/results/outlines/ResNet/val/p2.csv')
outline_ResNet_p3 <- read.csv('./resources/results/outlines/ResNet/val/p3.csv')
outline_ResNet_p2_VS_outline_ResNet_p3 = computeDelong(outline_ResNet_p2[, 'Label'], outline_ResNet_p2[, 'Score'], outline_ResNet_p3[, 'Score'])
print(lines)
print('outline_ResNet_p2_VS_outline_ResNet_p3')
outline_ResNet_p2_VS_outline_ResNet_p3$delong_res$roc1
outline_ResNet_p2_VS_outline_ResNet_p3$delong_res$roc2
outline_ResNet_p2_VS_outline_ResNet_p3$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p2 <- read.csv('./resources/results/outlines/ResNet/val/p2.csv')
outline_ResNet_p4 <- read.csv('./resources/results/outlines/ResNet/val/p4.csv')
outline_ResNet_p2_VS_outline_ResNet_p4 = computeDelong(outline_ResNet_p2[, 'Label'], outline_ResNet_p2[, 'Score'], outline_ResNet_p4[, 'Score'])
print(lines)
print('outline_ResNet_p2_VS_outline_ResNet_p4')
outline_ResNet_p2_VS_outline_ResNet_p4$delong_res$roc1
outline_ResNet_p2_VS_outline_ResNet_p4$delong_res$roc2
outline_ResNet_p2_VS_outline_ResNet_p4$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p2 <- read.csv('./resources/results/outlines/ResNet/val/p2.csv')
outline_ResNet_p5 <- read.csv('./resources/results/outlines/ResNet/val/p5.csv')
outline_ResNet_p2_VS_outline_ResNet_p5 = computeDelong(outline_ResNet_p2[, 'Label'], outline_ResNet_p2[, 'Score'], outline_ResNet_p5[, 'Score'])
print(lines)
print('outline_ResNet_p2_VS_outline_ResNet_p5')
outline_ResNet_p2_VS_outline_ResNet_p5$delong_res$roc1
outline_ResNet_p2_VS_outline_ResNet_p5$delong_res$roc2
outline_ResNet_p2_VS_outline_ResNet_p5$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p2 <- read.csv('./resources/results/outlines/ResNet/val/p2.csv')
outline_ResNet_p6 <- read.csv('./resources/results/outlines/ResNet/val/p6.csv')
outline_ResNet_p2_VS_outline_ResNet_p6 = computeDelong(outline_ResNet_p2[, 'Label'], outline_ResNet_p2[, 'Score'], outline_ResNet_p6[, 'Score'])
print(lines)
print('outline_ResNet_p2_VS_outline_ResNet_p6')
outline_ResNet_p2_VS_outline_ResNet_p6$delong_res$roc1
outline_ResNet_p2_VS_outline_ResNet_p6$delong_res$roc2
outline_ResNet_p2_VS_outline_ResNet_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p3 <- read.csv('./resources/results/outlines/ResNet/val/p3.csv')
outline_ResNet_p4 <- read.csv('./resources/results/outlines/ResNet/val/p4.csv')
outline_ResNet_p3_VS_outline_ResNet_p4 = computeDelong(outline_ResNet_p3[, 'Label'], outline_ResNet_p3[, 'Score'], outline_ResNet_p4[, 'Score'])
print(lines)
print('outline_ResNet_p3_VS_outline_ResNet_p4')
outline_ResNet_p3_VS_outline_ResNet_p4$delong_res$roc1
outline_ResNet_p3_VS_outline_ResNet_p4$delong_res$roc2
outline_ResNet_p3_VS_outline_ResNet_p4$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p3 <- read.csv('./resources/results/outlines/ResNet/val/p3.csv')
outline_ResNet_p5 <- read.csv('./resources/results/outlines/ResNet/val/p5.csv')
outline_ResNet_p3_VS_outline_ResNet_p5 = computeDelong(outline_ResNet_p3[, 'Label'], outline_ResNet_p3[, 'Score'], outline_ResNet_p5[, 'Score'])
print(lines)
print('outline_ResNet_p3_VS_outline_ResNet_p5')
outline_ResNet_p3_VS_outline_ResNet_p5$delong_res$roc1
outline_ResNet_p3_VS_outline_ResNet_p5$delong_res$roc2
outline_ResNet_p3_VS_outline_ResNet_p5$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p3 <- read.csv('./resources/results/outlines/ResNet/val/p3.csv')
outline_ResNet_p6 <- read.csv('./resources/results/outlines/ResNet/val/p6.csv')
outline_ResNet_p3_VS_outline_ResNet_p6 = computeDelong(outline_ResNet_p3[, 'Label'], outline_ResNet_p3[, 'Score'], outline_ResNet_p6[, 'Score'])
print(lines)
print('outline_ResNet_p3_VS_outline_ResNet_p6')
outline_ResNet_p3_VS_outline_ResNet_p6$delong_res$roc1
outline_ResNet_p3_VS_outline_ResNet_p6$delong_res$roc2
outline_ResNet_p3_VS_outline_ResNet_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p4 <- read.csv('./resources/results/outlines/ResNet/val/p4.csv')
outline_ResNet_p5 <- read.csv('./resources/results/outlines/ResNet/val/p5.csv')
outline_ResNet_p4_VS_outline_ResNet_p5 = computeDelong(outline_ResNet_p4[, 'Label'], outline_ResNet_p4[, 'Score'], outline_ResNet_p5[, 'Score'])
print(lines)
print('outline_ResNet_p4_VS_outline_ResNet_p5')
outline_ResNet_p4_VS_outline_ResNet_p5$delong_res$roc1
outline_ResNet_p4_VS_outline_ResNet_p5$delong_res$roc2
outline_ResNet_p4_VS_outline_ResNet_p5$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p4 <- read.csv('./resources/results/outlines/ResNet/val/p4.csv')
outline_ResNet_p6 <- read.csv('./resources/results/outlines/ResNet/val/p6.csv')
outline_ResNet_p4_VS_outline_ResNet_p6 = computeDelong(outline_ResNet_p4[, 'Label'], outline_ResNet_p4[, 'Score'], outline_ResNet_p6[, 'Score'])
print(lines)
print('outline_ResNet_p4_VS_outline_ResNet_p6')
outline_ResNet_p4_VS_outline_ResNet_p6$delong_res$roc1
outline_ResNet_p4_VS_outline_ResNet_p6$delong_res$roc2
outline_ResNet_p4_VS_outline_ResNet_p6$delong_res
print(lines)
################################################################################################


################################################################################################
outline_ResNet_p5 <- read.csv('./resources/results/outlines/ResNet/val/p5.csv')
outline_ResNet_p6 <- read.csv('./resources/results/outlines/ResNet/val/p6.csv')
outline_ResNet_p5_VS_outline_ResNet_p6 = computeDelong(outline_ResNet_p5[, 'Label'], outline_ResNet_p5[, 'Score'], outline_ResNet_p6[, 'Score'])
print(lines)
print('outline_ResNet_p5_VS_outline_ResNet_p6')
outline_ResNet_p5_VS_outline_ResNet_p6$delong_res$roc1
outline_ResNet_p5_VS_outline_ResNet_p6$delong_res$roc2
outline_ResNet_p5_VS_outline_ResNet_p6$delong_res
print(lines)
################################################################################################

