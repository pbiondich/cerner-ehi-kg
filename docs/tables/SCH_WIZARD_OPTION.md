# SCH_WIZARD_OPTION

> Scheduling Wizard Options

**Description:** Scheduling Wizard Options  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

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
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 9 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 16 | `WIZ_DISPLAY_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the wizard display. |
| 17 | `WIZ_DISPLAY_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the wizard display. |
| 18 | `WIZ_OPTION_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the wizard option. |
| 19 | `WIZ_OPTION_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the wizard option. |
| 20 | `WIZ_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the scheduling wizard type. |
| 21 | `WIZ_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling wizard type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WIZ_DISPLAY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WIZ_OPTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WIZ_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

