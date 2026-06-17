# NC_CHARTED_VIEW

> Used to maintain activity details of a charting view.

**Description:** Nursing Charting - Charted View  
**Table type:** ACTIVITY  
**Primary key:** `NC_CHARTED_VIEW_ID`  
**Columns:** 31  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CE_DRAFT_ID` | DOUBLE |  | FK→ | The identifier of the clinical event draft for the charted view. |
| 6 | `CHARTED_VIEW_CLOB` | LONGTEXT |  |  | A JSON formatted string containing the representation of the charted view activity. |
| 7 | `CHARTING_VIEW_DISP` | VARCHAR(255) |  |  | Stores the label of the charting view, if a label is defined. Otherwise, stores the name of the charting view. This is either pulled from NC_CHARTING_VIEW (Quick Chart solution) or an external cloud database (Integrated Charting). |
| 8 | `CLINICAL_DT_TM` | DATETIME |  |  | The clinically relevent date of the charted view. |
| 9 | `CLOUD_CHARTING_VIEW_IDENT` | VARCHAR(255) | NOT NULL |  | Represents the cloud reference identifier for the charting view. |
| 10 | `CREATE_DT_TM` | DATETIME |  |  | Thd date and time this row was created. |
| 11 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the person who created the row in the table |
| 12 | `DRAFT_STATUS_TFLG` | VARCHAR(15) |  |  | The status text of the draft for the charted view.; Values: NOT_STARTED, IN_PROGRESS; |
| 13 | `DRAFT_UPDT_DT_TM` | DATETIME |  |  | The date and time the draft for the charted view was updated. |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the patient's encounter associated to the charted view. |
| 15 | `INACTIVE_NOTIFICATION_DT_TM` | DATETIME |  |  | The date time an inactive notification was sent for the charted view. |
| 16 | `LAST_UPDT_DT_TM` | DATETIME |  |  | Last date and time this row was updated. |
| 17 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that last updated the data on this row. |
| 18 | `NC_CHARTED_VIEW_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the NC_CHARTED_VIEW table. |
| 19 | `NC_CHARTING_VIEW_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the charting view reference data. |
| 20 | `NOTE_EVENT_ID` | DOUBLE |  |  | The identifier of the note event for the charted view. |
| 21 | `NOTE_STATUS_CD` | DOUBLE |  |  | The status code of the note for the charted view. |
| 22 | `NOTE_TYPE_CD` | DOUBLE |  |  | The type code of the note for the charted view. |
| 23 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | The patient associated to the view. |
| 24 | `SCRATCHPAD_DRAFT_ID` | DOUBLE |  | FK→ | The identifier of the scratchpad draft for the charted view.; |
| 25 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the charted view |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `VERSION_NBR` | DOUBLE |  |  | The version of the charted view schema. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_DRAFT_ID` | [CE_DRAFT](CE_DRAFT.md) | `CE_DRAFT_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `NC_CHARTING_VIEW_ID` | [NC_CHARTING_VIEW](NC_CHARTING_VIEW.md) | `NC_CHARTING_VIEW_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SCRATCHPAD_DRAFT_ID` | [NURSING_ENCNTR_SCRATCHPAD](NURSING_ENCNTR_SCRATCHPAD.md) | `NURSING_ENCNTR_SCRATCHPAD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [NC_CHARTED_SECTION](NC_CHARTED_SECTION.md) | `NC_CHARTED_VIEW_ID` |

