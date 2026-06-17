# LH_CNT_READMIT_RISK_HIST

> Holds the history of the risk associated to patients in the readmission worklist

**Description:** LH_CNT_READMIT_RISK_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LH_CNT_READMIT_RISK_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `LH_CNT_READMIT_RISK_ID` | DOUBLE | NOT NULL |  | ID original record in LH_CNT_READMIT_RISK table |
| 6 | `LH_CNT_READMIT_WORKLIST_ID` | DOUBLE | NOT NULL |  | ID of original row on the LH_CNT_READMIT_WORKLIST table |
| 7 | `RISK_FACTOR_FLAG` | DOUBLE | NOT NULL |  | The type of risk factor for the patient |
| 8 | `RISK_FACTOR_TXT` | VARCHAR(255) |  |  | The description of the risk factor |
| 9 | `RISK_FACTOR_VALUE` | DOUBLE | NOT NULL |  | The Risk Factor for the patient |
| 10 | `RISK_VERSION_IDENT` | DOUBLE |  |  | Contains the Version ID for a Cloud Based risk score. This Version ID is used to tie the record back to a record in the Cloud Database. |
| 11 | `RISK_VERSION_TXT` | VARCHAR(100) |  |  | The unique value for each risk which allows the value stored to be tied back to the source. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

