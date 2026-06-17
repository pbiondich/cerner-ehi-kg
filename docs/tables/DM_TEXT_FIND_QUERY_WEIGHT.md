# DM_TEXT_FIND_QUERY_WEIGHT

> This table will store the relative weighting for specific queries on the query group level.

**Description:** Database Management Text Find Query Weighting  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CRITERIA` | VARCHAR(2000) | NOT NULL |  | The criteria that will determine what value |
| 3 | `CRITERIA_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates what type of data is contained in the Criteria column (an exact value, a range, a regular expression, a custom rule, etc.) |
| 4 | `DM_TEXT_FIND_QUERY_WEIGHT_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 5 | `QUERY_GROUP_NAME` | VARCHAR(40) | NOT NULL |  | Indicates which group of queries to this weighting applies to. Value comes from the DM_TEXT_FIND_QUERY table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `WEIGHT` | DOUBLE | NOT NULL |  | The weight to assign to this QUERY_GROUP_NAME and QUERY_VALUE combination. 100 will be the default weight assigned to values not contained in this table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

