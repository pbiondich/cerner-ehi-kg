# LOG_GROUP_TYPE

> Stores Exception Type data for groups which are created. Link to LOGICAL_GROUPING table by log_grouping_cd field. T

**Description:** Logical Grouping Type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXCEPTION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates which database this exception relates to. CodeSet: 6015 |
| 2 | `LOG_GROUPING_CD` | DOUBLE | NOT NULL | FK→ | This row contains the identifier of the logical group that this row is an entry for on the logical grouping table. |
| 3 | `LOG_GROUP_TYPE_ID` | DOUBLE | NOT NULL |  | Primary key |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOG_GROUPING_CD` | [LOGICAL_GROUPING](LOGICAL_GROUPING.md) | `LOG_GROUPING_CD` |

