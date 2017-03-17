# Notes about graph entropy

## The first entropy measures of graphs

Rashevsky and Trucco in 1995, defined an entropy measure to characterize the structural information content of graphs. His definition is based on the partitioning of the n vertices into k classes of equivalent vertices, according to their degree dependence. Then, assigned a probability to each partition obtained as the fraction of vertices in this partition divided by the total number of vertices. Thus, according to Rashevsky the entropy of a graph $G$ is:

$$ I(G) := - \sum_{i=1}^{k} \frac{|N_{i}|}{|V|} log \left( \frac{|N_{i}|}{|V|} \right) $$

According to Rashevsky, $|N_{i}| denotes the number of equivalent vertices in the ith class and k the number of classes (or different orbits).

Trucco applied this concept to the edge automorphism group introducing a similar entropy measure $_{E}I(G)$
