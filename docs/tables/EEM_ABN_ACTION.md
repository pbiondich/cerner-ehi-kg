# EEM_ABN_ACTION

> This table is used to track the actions performed on an ABN.

**Description:** EEM ABN Action  
**Table type:** ACTIVITY  
**Primary key:** `ABN_ACTION_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_ACTION_CD` | DOUBLE | NOT NULL | FK→ | The action taken on the ABN. For example: Check, Print, Signed, Not Signed, View, etc. |
| 2 | `ABN_ACTION_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. |
| 3 | `ABN_CHECK_ID` | DOUBLE | NOT NULL | FK→ | The ABN check associated with the ABN action. A foreign key to the EEM_ABN_CHECK table. |
| 4 | `ABN_FORM_ID` | DOUBLE | NOT NULL | FK→ | The ABN form associated to the ABN action. A foreign key to the EEM_ABN_CHECK table. |
| 5 | `ABN_STATE_CD` | DOUBLE | NOT NULL | FK→ | The state of the ABN. For example: Checked, Signed, Printed, Not Signed, etc. |
| 6 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | The date and time the action was performed. |
| 7 | `ACTION_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-char description corresponding to the Action Code. |
| 8 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the personnel that performed the action. |
| 9 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 10 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 11 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 12 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 13 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | The Application Number of the Application that the update was performed from. |
| 14 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 15 | `CONVERSATION_ID` | DOUBLE | NOT NULL |  | Scheduling Conversation Identifier. This identifier is used to track all the abn checks which happened in the same transaction. This field makes debugging much easier |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `FORM_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Form Action Identifier |
| 18 | `STATE_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-char description corresponding to the ABN State Code. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ABN_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ABN_CHECK_ID` | [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `ABN_CHECK_ID` |
| `ABN_FORM_ID` | [EEM_ABN_FORM](EEM_ABN_FORM.md) | `ABN_FORM_ID` |
| `ABN_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FORM_ACTION_ID` | [EEM_ACTION](EEM_ACTION.md) | `EEM_ACTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EEM_ABN_FORM](EEM_ABN_FORM.md) | `ABN_FORM_ID` |

