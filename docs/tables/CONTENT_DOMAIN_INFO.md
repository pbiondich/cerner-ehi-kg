# CONTENT_DOMAIN_INFO

> Stores content domain information for the Content Manager solution.

**Description:** CONTENT DOMAIN INFO  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_DOMAIN_INFO_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `FIELD_NAME` | VARCHAR(100) | NOT NULL |  | Name of the Content DOMAIN attribute being stored in the FIELD_VALUE column. |
| 3 | `FIELD_VALUE` | DOUBLE |  |  | Numeric value for the attribute named in the FIELD_NAME column. |
| 4 | `FIELD_VALUE_STR` | VARCHAR(100) |  |  | String value for the attribute named in the FIELD_NAME column. |
| 5 | `PROPERTY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CONTENT_PROPERTY table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

