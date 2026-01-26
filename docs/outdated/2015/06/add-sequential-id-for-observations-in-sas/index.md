---
title: "Add Sequential ID for Observations in SAS"
date: 2015-06-20 23:25:05
modified: 2015-06-20 23:25:05
authors:
  - bendu
label: add-sequential-id-for-observations-in-sas
license: CC-BY-4.0
tags:
  - programming
  - SAS
  - SQL
  - sequential
  - ID
  - observation
---

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**

**
Things under legendu.net/outdated are outdated technologies 
that the author does not plan to update any more. 
Please look for better alternatives.
**

data s1;
    set s;
    obs_id = _n_;
run;

proc sql;
    create table s1 as
    select 
        monotonic() as obs_id,
        *
    from
        s
    ;
run;

1. The `monotonic` function runs before `sort` and `group by`.
So even if it gives distinct observation ID,
it guarantees no specific order of observations.
It is suggested that you use the data step approach 
rather than the `nonotonic` way in SQL
if you want the generated observation IDs to preserve some kind of order of observations.

