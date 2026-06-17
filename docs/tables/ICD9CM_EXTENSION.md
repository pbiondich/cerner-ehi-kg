# ICD9CM_EXTENSION

> Contains ICD-9-CM vocabulary specific data.

**Description:** ICD-9-CM Extension  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGE_FLAG_DESC` | CHAR(1) |  |  | Indicates Age specific edits for the code. A-adult (15 yo+) M-maternity (12-55 yo woman) P-pediatric (0-17 yo) N-newborn (0 yo) |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | Contributor Source Code |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `ICD9CM_EXTENSION_ID` | DOUBLE | NOT NULL |  | Identifies the row as unique in the table. |
| 7 | `SEX_FLAG_DESC` | CHAR(1) |  |  | Indicates Sex edits for the code. M-male F-female |
| 8 | `SOURCE_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | The ICD-9-CM code. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VALID_FLAG_DESC` | CHAR(1) |  |  | Indicates whether a code is billable. Y-billable N-not billable |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

