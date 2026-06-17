# FILTER_TYPE_DATA

> This table contains the filter types defined to be used for the filter entity relations that have filtered data.

**Description:** Filter Type Data  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_ENTITY1_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 2 | `FILTER_ENTITY1_NAME` | VARCHAR(30) | NOT NULL |  | filter_entity1_name |
| 3 | `FILTER_ENTITY2_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 4 | `FILTER_ENTITY2_NAME` | VARCHAR(30) |  |  | filter_entity2_name |
| 5 | `FILTER_ENTITY3_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 6 | `FILTER_ENTITY3_NAME` | VARCHAR(30) |  |  | filter_entity3_name |
| 7 | `FILTER_ENTITY4_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 8 | `FILTER_ENTITY4_NAME` | VARCHAR(30) |  |  | filter_entity4_name |
| 9 | `FILTER_ENTITY5_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which contains the filter data |
| 10 | `FILTER_ENTITY5_NAME` | VARCHAR(30) |  |  | filter_entity5_name |
| 11 | `FILTER_TYPE_CD` | DOUBLE | NOT NULL |  | Filter type code |
| 12 | `FILTER_TYPE_DATA_ID` | DOUBLE | NOT NULL |  | Filter type data identifier |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

