# BR_ALIAS_POOL_INFO

> Alias pool data

**Description:** BEDROCK ALIAS POOL INFO  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | alias pool code set |
| 4 | `ALIAS_POOL_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the type of the alias pool |
| 5 | `ALPHA_CHAR_IND` | DOUBLE |  |  | Defines whether alpha characters are allowed in the aliases in this pool |
| 6 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 7 | `FORMAT_IND` | DOUBLE |  |  | Defined whether the aliases in this pool are subject to a format mask |
| 8 | `FSI_ID` | DOUBLE | NOT NULL |  | The id for the row on the BR_FSI table related to this alias pool |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

