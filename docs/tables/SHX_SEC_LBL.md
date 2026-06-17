# SHX_SEC_LBL

> The table defines the confidentiality(4702082) associated with social-history data.

**Description:** Social history security label  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PRSNL_ID` | DOUBLE |  | FK→ | The ID of the personnel who has taken an action (modified-deleted-etc) on this label. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CREATED_BY_PRSNL_ID` | DOUBLE |  | FK→ | The ID of the personnel who associated this label with the data entity. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `SENSITIVITY_REASON_CD` | DOUBLE |  |  | The code value indicating why the tagged data is considered sensitive. Values should be taken from the SENSITIVITY_REASON codeset (4702082). |
| 7 | `SHX_ACTIVITY_ID` | DOUBLE |  | FK→ | Primary Key value from a row in the SHX_ACTIVITY table. |
| 8 | `SHX_SEC_LBL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `TASK_ASSAY_CD` | DOUBLE |  | FK→ | task assay code from DISCRETE_TASK_ASSAY table - Code set 14003. This value should align with value in SHX_RESPONSE.TASK_ACTIVITY_CD |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SHX_ACTIVITY_ID` | [SHX_ACTIVITY](SHX_ACTIVITY.md) | `SHX_ACTIVITY_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

