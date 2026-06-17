# DCP_FLEX_RTG

> Flex routing

**Description:** Flex routing  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DCP_FLEX_RTG_ID` | DOUBLE | NOT NULL |  | flex routing is |
| 2 | `DCP_OUTPUT_ROUTE_ID` | DOUBLE | NOT NULL |  | output routing |
| 3 | `FLEX_DEST_IND` | DOUBLE |  |  | flexing destination ind |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE1_CD` | DOUBLE | NOT NULL |  |  |
| 10 | `VALUE2_CD` | DOUBLE | NOT NULL |  |  |
| 11 | `VALUE3_CD` | DOUBLE | NOT NULL |  |  |
| 12 | `VALUE4_CD` | DOUBLE | NOT NULL |  |  |
| 13 | `VALUE5_CD` | DOUBLE | NOT NULL |  |  |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

