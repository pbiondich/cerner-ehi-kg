# DRG_EXTENSION

> Stores fields such as MDC, DRG weight...

**Description:** DRG Extension table hold additional DRG info now stored on the nomenclature  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AMLOS` | DOUBLE |  |  | This stores the Arithmetic mean length of stay assigned for this DRG |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DRG_CATEGORY` | VARCHAR(10) |  |  | The category that the Diagnostic Related Group is associated with in accordance with the Major Diagnostic Groups. |
| 8 | `DRG_WEIGHT` | DOUBLE |  |  | The weight of the diagnostic related group determines the amount of reimbursement entitled to the organization. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `GMLOS` | DOUBLE |  |  | A way to figure the length of stay geometrically |
| 11 | `MDC_CD` | DOUBLE |  |  | Major Diagnostic Category Code |
| 12 | `SEVERITY_OF_ILLNESS_CD` | DOUBLE | NOT NULL |  | This is the code value for severity of illness. |
| 13 | `SOURCE_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | The code or key from the source vocabulary that contributed the string to the nomenclature |
| 14 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | The external vocabulary or lexicon that contributed the string, example ICD-9, SNOMED etc. |
| 15 | `TRANSFER_RULE_IND` | DOUBLE | NOT NULL |  | This field indicates where the DRG is subject to the Transfer Rule |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

