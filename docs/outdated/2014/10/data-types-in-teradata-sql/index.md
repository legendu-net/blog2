---
title: Data Types in Teradata SQL
created: 2014-10-23 13:01:10
date: 2026-04-19 20:02:26.877425
authors:
  - bendu
label: data-types-in-teradata-sql
license: CC-BY-4.0
tags:
  - programming
  - Teradata SQL
  - data type
  - cast
  - date
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

1. It is important to be aware of type of columns in SQL.

1. You can use `cast` to convert between different data types in Teradata SQL.
   For example, `cast(n as bigint)` cast the column "n" into type of `bigint`.

1. In Teradata SQL,
   missing values (both numeric and character) are represented by `null`.
   You can use `v is (not) null` in the `where` and/or `on` clauses to select rows.
   When Teradata SQL Assistant displays query results,
   `null` values are indicated by question marks (`?`).

1. When unioning multiple tables containing constant columns,
   the type of constant columns are forced to be the same as the one in the first table.
   For example,
   the type of `str` column in the following query is char(1),
   which loses information.

```SQL
select '1' as str;
union
select '12' as str;
union 
select '123' as str;
```

To avoid this issue,
you can manually cast the type of the column in the first (or all) tables to a bigger one.

```SQL
select '1' (varchar(255)) as str;
union
select '12' as str;
union 
select '123' as str;
```

6. Arithematic calculation in SQL is similar to C/C++ and Java.
   For example, integer dividing by integer returns an integer
   which is different from R and Python.
   The return type of arithematic calculation is the largest type in the expression.

1. NUMBER is a new data type,
   introduced in Teradata 14.0,
   which is intended to emulate the Oracle number data type.
   It has an optional precision and scale of up to 38 decimal digits.\
   It can also represent exponential values.
   Its storage size varies from 0 to 18 bytes.

1. Operations/function on null return null
   except a few exception such as ...

1. In Teradata, the maximum row size is approx 64K bytes.
   So that you cannot define columns of size greater than 64K.
   For example,
   you cannot define a column of size 65K.

1. be careful about return type of string functions, some return too long strings,
   better to manually cast them to short strings

## Date Types

1. Dates can be represented by strings in the 'yyyy-mm-dd' format in Teradata SQL,
   and these strings will be converted to dates implicitly when necessarily.
   For example,
   the following code counts the number of transactions in a month.

   ```sql
   SELECT
       count(*) AS n
   FROM
       some_transaction_table
   WHERE
       tran_dt between '2014-03-01' and '2014-03-31'
   ;
   ```

1. Be careful when you work with date in SQL.
   A non-exist date can result in tricky errors.
   For example (note that `2016-09-31` does not exist)

   ```sql
   WHERE dt BETWEEN '2016-09-01' AND '2016-09-31'  
   ```

   in Teradata throws the error message "a character string failed to convert to a numeric value".
