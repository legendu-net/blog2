---
title: "Union RDDs in Spark"
created: 2017-06-03 23:49:38
date: 2020-11-03 23:49:38
authors:
  - bendu
label: union-RDDs-in-spark
license: CC-BY-4.0
tags:
  - programming
  - Scala
  - Spark
  - RDD
  - union
---


No deduplication is done (to be efficient) when unioning RDDs/DataFrames in Spark 2.1.0+.

1. Union 2 RDDs.

        df1.union(df2)
        // or for old-fashioned RDD
        rdd1.union(rdd_2)

2. Union multiple RDDs.

        df = spark.union([df1, df2, df3]) // spark is a SparkSession object
        // or for old-fashioned RDD
        rdd = sc.union([rdd1, rdd2, rdd3]) // sc is a SparkContext object

## References 

[Union DataFrames in Spark](http://www.legendu.net/misc/blog/spark-dataframe-union)

[Union DataFrames in Spark](http://www.legendu.net/en/blog/spark-dataframe-union)