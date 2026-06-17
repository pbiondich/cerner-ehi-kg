# BB_QC_RESULT_TROUBLESHOOTING_R

> This table contains the selected troubleshooting steps selected when a Blood Bank QC result is abnormal

**Description:** Blood Bank Quality Control Result Troubleshooting  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `QC_RESULT_ID` | DOUBLE | NOT NULL | FK→ | This field links the troubleshooting step with the specific QC result. (BB_QC_RESULT) |
| 2 | `RESULT_TROUBLESHOOTING_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies the troubleshooting row. |
| 3 | `TROUBLESHOOTING_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the selected troubleshooting step. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QC_RESULT_ID` | [BB_QC_RESULT](BB_QC_RESULT.md) | `QC_RESULT_ID` |
| `TROUBLESHOOTING_ID` | [BB_QC_TROUBLESHOOTING](BB_QC_TROUBLESHOOTING.md) | `TROUBLESHOOTING_ID` |

