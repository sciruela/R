require(ggplot2); 
require(igraph); 



data<-read.csv("D:/sn-examples/myfriends.csv")

g<-graph.data.frame(data)

V(g)$label<-V(g)$name

png("D:/sn-examples/myfriendsinterests.png")
plot(g)
dev.off()