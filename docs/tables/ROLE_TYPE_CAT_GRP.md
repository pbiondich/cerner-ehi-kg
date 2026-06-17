# ROLE_TYPE_CAT_GRP

> role type category group

**Description:** role type category group  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LVL1_GROUP` | VARCHAR(40) |  |  | level one group |
| 2 | `LVL2_GROUP` | VARCHAR(40) |  |  | level two group |
| 3 | `LVL3_GROUP` | VARCHAR(40) |  |  | level three group |
| 4 | `LVL4_GROUP` | VARCHAR(40) |  |  | level four group |
| 5 | `LVL5_GROUP` | VARCHAR(40) |  |  | level five group |
| 6 | `ROLE_TYPE_CAT_GRP_ID` | DOUBLE | NOT NULL |  | role type category group identifier |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

