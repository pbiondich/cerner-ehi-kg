# LH_CNT_READMIT_RISK

> This table will contain the reasons (risks) that a patient was added to the readmission worklist

**Description:** LH_CNT_READMIT_RISK  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LH_CNT_READMIT_RISK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_READMIT_RISK table. |
| 5 | `LH_CNT_READMIT_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | The ID of the parent row from the LH_CNT_READMIT_WORKLIST table. |
| 6 | `RISK_FACTOR_FLAG` | DOUBLE | NOT NULL |  | Value that represents what type of risk factor this risk is. (AMI, HF, PNEU) |
| 7 | `RISK_FACTOR_TXT` | VARCHAR(255) |  |  | Text representation of the risk factor. Needed to store it separate as the client can modify the text. |
| 8 | `RISK_FACTOR_VALUE` | DOUBLE | NOT NULL |  | Holds the numerical value representing the risk factor. |
| 9 | `RISK_VERSION_IDENT` | DOUBLE |  |  | Contains the Version ID for a Cloud Based risk score. This Version ID is used to tie the record back to a record in the Cloud Database. |
| 10 | `RISK_VERSION_TXT` | VARCHAR(100) |  |  | The unique value for each risk which allows the value stored to be tied back to the source. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_READMIT_WORKLIST_ID` | [LH_CNT_READMIT_WORKLIST](LH_CNT_READMIT_WORKLIST.md) | `LH_CNT_READMIT_WORKLIST_ID` |

