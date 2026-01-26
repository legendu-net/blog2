---
title: "Use Spark With the BeakerX Scala Kernel"
date: 2021-04-23 17:23:46
modified: 2020-03-23 17:23:46
authors:
  - bendu
label: use-spark-with-the-beakerx-scala-kernel
license: CC-BY-4.0
tags:
  - Computer Science
  - Spark
  - Scala
  - BeakerX
  - JupyterLab
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. Open a JupyterLab notebook with the BeakerX Scala kernel from the launcher.

2. Download Spark (say, 2.3.1) dependencies. 

        :::scala
        %%classpath add mvn
        org.apache.spark spark-core_2.11 2.3.1
        org.apache.spark spark-sql_2.11 2.3.1

3. Create a SparkSession object.

        :::scala
        import org.apache.spark.sql.SparkSession
        import org.apache.spark.sql.functions._

        val spark = SparkSession.builder()
            .master("local[2]")
            .appName("Spark Example")
            .config("spark.some.config.option", "some-value")
            .getOrCreate()

        import spark.implicits._

4. Use Spark as usual. 

        :::scala
        val df = Range(0, 10).toDF
        df.show
