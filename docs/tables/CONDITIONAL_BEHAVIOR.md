# CONDITIONAL_BEHAVIOR

> Conditional behavior definitions for formbuilder forms.

**Description:** CONDITIONAL BEHAVIOR  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEHAVIOR_FLAG` | DOUBLE |  |  | Defines the behavior of the condition. |
| 7 | `CONDITION_CONTROL_CD` | DOUBLE | NOT NULL |  | The control which value defines the behavior. |
| 8 | `CONDITION_FLAG` | DOUBLE |  |  | The test to apply to the value of the control. |
| 9 | `CONDITION_ID` | DOUBLE | NOT NULL |  | Unique identifier of the condition. |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 11 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 12 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 13 | `EFFECTED_CONTROL_CD` | DOUBLE | NOT NULL |  | The control that has the behavior applied to it. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `INPUT_FORM_CD` | DOUBLE | NOT NULL | FK→ | The form that contains the two fields. |
| 16 | `INPUT_FORM_VERSION_NBR` | DOUBLE |  | FK→ | The version of the form that contains the two fields. |
| 17 | `RANGE_VALUE_1` | VARCHAR(255) |  |  | First value to test the condition against. |
| 18 | `RANGE_VALUE_2` | VARCHAR(255) |  |  | Second value to test the condition against. |
| 19 | `UPDT_APP` | DOUBLE |  |  | Update application. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_REQ` | DOUBLE |  |  | Update request. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INPUT_FORM_CD` | [INPUT_FORM_REFERENCE](INPUT_FORM_REFERENCE.md) | `INPUT_FORM_CD` |
| `INPUT_FORM_VERSION_NBR` | [INPUT_FORM_REFERENCE](INPUT_FORM_REFERENCE.md) | `INPUT_FORM_VERSION_NBR` |

