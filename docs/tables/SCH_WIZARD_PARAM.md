# SCH_WIZARD_PARAM

> Scheduling Wizard Parameters

**Description:** Scheduling Wizard Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `CDF_MEANING` | VARCHAR(12) |  |  | The actual string value for the cdf meaning. |
| 8 | `CODE_SET` | DOUBLE | NOT NULL |  | Code Set |
| 9 | `DATA_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling date type. |
| 10 | `DATA_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling data type. |
| 11 | `DOUBLE_VALUE` | DOUBLE |  |  | Numeric Value |
| 12 | `DT_TM_VALUE` | DATETIME |  |  | Date and Time Value |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVAL_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the evaluation type. |
| 15 | `EVAL_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the evaluation type. |
| 16 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 17 | `STRING_VALUE` | VARCHAR(255) |  |  | Alphanumeric Value. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 24 | `WIZ_OPTION_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the wizard option. |
| 25 | `WIZ_OPTION_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the wizard option. |
| 26 | `WIZ_PARAM_NAME` | VARCHAR(30) | NOT NULL |  | A free textname used to identify scheduling wizard parameters. |
| 27 | `WIZ_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the scheduling wizard type. |
| 28 | `WIZ_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling wizard type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATA_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `EVAL_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WIZ_OPTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WIZ_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

