# HLA_SERA_QUERY

> Defines a unique description and time for a query. Queries are comprised of a list of sera brought back from a serum search.

**Description:** HLA Sera Query.  
**Table type:** ACTIVITY  
**Primary key:** `SERA_QUERY_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `QUERY_DESCRIPTION` | VARCHAR(255) |  |  | The description of the query. Unique identifier the user gives the query. |
| 2 | `QUERY_DT_TM` | DATETIME |  |  | Date and time assigned to the record. |
| 3 | `SERA_QUERY_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a Query Sera record. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HLA_SERA_QUERY_QUERIES](HLA_SERA_QUERY_QUERIES.md) | `SERA_QUERY_ID` |
| [HLA_SERA_QUERY_SERUM](HLA_SERA_QUERY_SERUM.md) | `SERA_QUERY_ID` |

