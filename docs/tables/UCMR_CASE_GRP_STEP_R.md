# UCMR_CASE_GRP_STEP_R

> Contains the case group step relationship information.

**Description:** Unified Case Manager Reference - Case Group Step Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PREV_UCMR_CASE_GRP_STEP_R_ID` | DOUBLE | NOT NULL |  | Used to track versions of the case group information. This field will always point back to the initial value created. This may be used to find the correct version when combined with the begin and end effective dates and times. |
| 6 | `REPEAT_CAT_CD` | DOUBLE | NOT NULL |  | Orderable to be repeated. |
| 7 | `UCMR_CASE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the case group related to this record. |
| 8 | `UCMR_CASE_GRP_STEP_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a case group step relationship. |
| 9 | `UCMR_CASE_STEP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the case step related to this record. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_CASE_GROUP_ID` | [UCMR_CASE_GROUP](UCMR_CASE_GROUP.md) | `UCMR_CASE_GROUP_ID` |
| `UCMR_CASE_STEP_ID` | [UCMR_CASE_STEP](UCMR_CASE_STEP.md) | `UCMR_CASE_STEP_ID` |

