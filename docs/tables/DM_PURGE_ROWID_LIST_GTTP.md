# DM_PURGE_ROWID_LIST_GTTP

> Global Temporary Table used for Purge process to track table purges. Temp data will be preserved until session terminates.

**Description:** Global Temp Table for PURGE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PURGE_TABLE_ROWID` | VARCHAR(10) |  |  | A ROWID value of a table that is purged by the purge process |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

