# Load ggplot2 + dplyr
library(ggplot2)
library(dplyr)

# Load Iris 
data(iris)


head(iris)
summary(iris)



ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point() +
  labs(x = "Sepal Length", y = "Sepal Width", title = "Sepal Length vs Sepal Width")


ggplot(iris, aes(x = Species, y = Petal.Length, fill = Species)) +
  geom_boxplot() +
  labs(x = "Species", y = "Petal Length", title = "Petal Length by Species")


mean_petal_length <- iris %>%
  group_by(Species) %>%
  summarise(mean_petal_length = mean(Petal.Length))


print(mean_petal_length)

#Print  message
cat("Data analysis and visualization has been completed.\n")
