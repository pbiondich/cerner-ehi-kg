# LH_CNT_QM_MEAS_STATE

> This table will contain the statuses of core measures used by the Quality Measures MPage

**Description:** LH_CNT_QM_MEAS_STATE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Encounter id for specific person of this measure. |
| 2 | `LH_CNT_QM_MEAS_STATE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_QM_MEAS_STATE table. |
| 3 | `MEASURE_TXT` | VARCHAR(100) | NOT NULL |  | Textual display of the measure. |
| 4 | `STATE_FLAG` | DOUBLE | NOT NULL |  | Measure state of this measure. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

