# AP_SYS_CORR

> This reference table includes the parameters established for system selected correlation events. Each entry describes a set of circumstances under which the system will initiate diagnostic correlation events to be correlated.

**Description:** System Selected Correlation  
**Table type:** REFERENCE  
**Primary key:** `SYS_CORR_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSIGN_TO_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification of the personnel group to which a correlation study is to be assigned. This field can be used to join to the PRSNL_GROUP table. |
| 3 | `ASSIGN_TO_GROUP_IND` | DOUBLE | NOT NULL |  | This indicator field is used to determine whether the initiated study is to be assigned to a group or will be defaulted to group assignment. |
| 4 | `ASSIGN_TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification of the person to which a correlation study is to be assigned. This field can be used to join to the PRSNL table. |
| 5 | `ASSIGN_TO_VERIFYING_IND` | DOUBLE |  |  | This indicator fields is used to determine whether the correlation event should be assigned to the person verifying the Pathology report. |
| 6 | `CASE_PERCENTAGE` | DOUBLE | NOT NULL |  | This field contains the percentage of times a system initiated correlation event will be triggered upon parameter qualification. |
| 7 | `EXECUTE_ON_RESCREEN_IND` | DOUBLE | NOT NULL |  | This indicator field is used to determine whether all attempts to verify a cytology report should be evaluated against a system correlation trigger. |
| 8 | `LOOKBACK_ALL_CASES_IND` | DOUBLE | NOT NULL |  | This indicator field is used to determine whether all cases or only the most recent case should qualify for a system correlation trigger. |
| 9 | `LOOKBACK_CASE_TYPE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the type of cases to look back for. |
| 10 | `LOOKBACK_MONTHS` | DOUBLE | NOT NULL |  | This field indicates the number of months to look back for qualifying cases. |
| 11 | `NOTIFY_USER_ONLINE_IND` | DOUBLE | NOT NULL |  | This indicator field is used to determine whether the user should be notified online when the system initiates a correlation study. |
| 12 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the correlation study to be initiated upon qualification. |
| 13 | `STUDY_SEQUENCE` | DOUBLE | NOT NULL |  | This field in used in conjunction with the STUDY_ID column in order to identify a single correlation parameter set. |
| 14 | `SYS_CORR_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies the 'system correlation' and its associated parameters. This value is used to join to the AP_SYS_CORR_DETAIL and AP_SYS_CORR_COUNTS tables. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGN_TO_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ASSIGN_TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOOKBACK_CASE_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `STUDY_ID` | [AP_DC_STUDY](AP_DC_STUDY.md) | `STUDY_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [AP_DC_EVENT](AP_DC_EVENT.md) | `SYS_CORR_ID` |
| [AP_SYS_CORR_COUNTS](AP_SYS_CORR_COUNTS.md) | `SYS_CORR_ID` |
| [AP_SYS_CORR_DETAIL](AP_SYS_CORR_DETAIL.md) | `SYS_CORR_ID` |

