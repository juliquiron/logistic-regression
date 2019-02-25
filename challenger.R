data = read.csv('challenger-data.csv')

install.packages('plyr')
library(plyr)

failures = subset(data, data$Y == 1)
success = subset(data, data$Y == 0)
failures_freq = count(failures, 'X')
success_freq = count(success, 'X')
plot(success$X, integer(length(success$X)), ylim=c(-0.5, 3.5), col='blue', xlab='X: Temperature', ylab='Number of failures', pch=19)
points(failures_freq$X, failures_freq$freq, col='red', pch=19)

model = glm(data$Y ~ data$X, family=binomial(link='logit'), data=data)
summary(model)
