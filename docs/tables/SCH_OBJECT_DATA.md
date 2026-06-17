# SCH_OBJECT_DATA

> Scheduling Object Data Sources

**Description:** Scheduling Object Data Sources  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ASSOC_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier of the scheduling association type. This is used to denote the type of association between the objects. |
| 6 | `ASSOC_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling association type code. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `DATA_SOURCE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling data source. |
| 10 | `DATA_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling data source. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 13 | `OBJECT_SUB_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the generic scheduling object sub type. |
| 14 | `OBJECT_SUB_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the generic scheduling object sub type code. |
| 15 | `SCRIPT_NAME` | VARCHAR(30) |  |  | The CCL name of the program to execute. |
| 16 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSOC_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATA_SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OBJECT_SUB_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

