# AUTO_VERIFY

> Defines the parameters used to check whether a procedure result should be autoverified.

**Description:** Automatic Verification  
**Table type:** REFERENCE  
**Primary key:** `AV_REF_ID`  
**Columns:** 33  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AV_REF_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific autoverification reference row. |
| 3 | `AV_STATUS_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate the status of this service resource and assay combination. It indicates whether this is turned on or off from AVStatus.dll or whether it has been turned off because QC is out of control. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `CONSISTENT_MAP` | CHAR(50) |  |  | Field no longer used. |
| 6 | `CONS_NBR_HRS` | DOUBLE |  |  | Field no longer used. |
| 7 | `CRIT_RANGE_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check for critical result values to prevent autoverification. A value of 0 does not check for critical to prevent autoverification. A value of 1 does check for critical to prevent autoverification. |
| 8 | `DELTA_CHK_FLAG` | DOUBLE | NOT NULL |  | Defines whether the delta check flag on a specific result will be used in determining whether to autoverify the result. |
| 9 | `DELTA_CHK_IND` | DOUBLE | NOT NULL |  | Field no longer used. |
| 10 | `DEST_CODES` | VARCHAR(50) |  |  | Field no longer used. |
| 11 | `DUP_ASSAY_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check for a duplicate/equivalent assay to prevent autoverification. A value of 0 does not check for a duplicate/equivalent assay to prevent autoverification. A value of 1 does check for a duplicate/equivalent assay to prevent autoverification. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `FEAS_RANGE_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check for a feasibility limit to prevent autoverification. A value of 0 does not check for feasible limit to prevent autoverification. A value of 1 does check for a feasible limit to prevent autoverification. |
| 14 | `INSTR_ERROR_CODE_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check the posting of instrument error codes with the result to prevent autoverification. A value of 0 does not check for instrument error codes posted with the result. A value of 1 does check for instrument error codes posted with the result to prevent autoverification. |
| 15 | `LIN_RANGE_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check for a result exceeding a linear limit to prevent autoverification. A value of 0 does not check for exceeding linearity to prevent autoverification. A value of 1 does check for exceeding linearity to prevent autoverification. |
| 16 | `NOTIFY_RANGE_IND` | DOUBLE | NOT NULL |  | Indicates that auto verification will be restricted if the notify flag is applied to the result. |
| 17 | `PREV_RSLT_IND` | DOUBLE | NOT NULL |  | Field no longer used. |
| 18 | `PREV_VERF_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should prevent autoverification of associated discrete task assays. A value of 0 does not prevent autoverification of the associated assay. A value of 1 does prevent autoverification of the associated assay. |
| 19 | `QC_INSTR_ERROR_CODE_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check the posting of instrument error codes with the result to prevent autoverification for QC results. A value of 0 does not check for instrument error codes posted with the result. A value of 1 does check for instrument error codes posted with the result to prevent autoverification. |
| 20 | `REF_RANGE_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check for a result that exceeds a reference range to prevent autoverification. A value of 0 does not check for exceeding reference ranges to prevent autoverification. A value of 1 does check for a exceeding reference ranges to prevent autoverification. |
| 21 | `REPEAT_FLAG` | DOUBLE | NOT NULL |  | Field no longer used. |
| 22 | `REPEAT_MAP` | CHAR(50) |  |  | Defines how repeats should be performed when autoverification fails. |
| 23 | `REV_RANGE_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check for results exceeding a review limit to prevent autoverification. A value of 0 does not check for exceeding the review limit to prevent autoverification. A value of 1 does check for exceeding the review limit to prevent autoverification. |
| 24 | `SCRIPT` | CHAR(20) |  |  | Defines a user-created script that should be run to check autoverify parameters. (Currently not implemented) |
| 25 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies a specific service resource (i.e. instrument) for which autoverification parameters are defined. |
| 26 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies the specific discrete task assay for which autoverification parameters are defined. |
| 27 | `UNVERF_PREV_RSLT_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check for an unverified previous result to prevent autoverification. A value of 0 does not check for an unverified previous result to prevent autoverification. A value of 1 does check for an unverified previous result to prevent autoverification. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 33 | `VALIDATE_QC_SCHEDULE_IND` | DOUBLE | NOT NULL |  | Indicates whether the system should check whether to validate the QC schedule for this instrument/assay. A value of 0 does not validate the QC schedule for this instrument/assay. A value of 1 does validate the QC schedule for this instrument/assay. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AV_CONSISTENCY](AV_CONSISTENCY.md) | `AV_REF_ID` |

