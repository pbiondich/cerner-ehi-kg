# SUMMARY_SECTION

> The Summary Section table defines the subject area of the section within the Summary Sheet.

**Description:** Summary Section  
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
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMMENT_TEXT` | VARCHAR(255) |  |  | Not Used. |
| 7 | `DISPLAY` | VARCHAR(40) |  |  | The user-defined name for the section. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `MAX_QUAL` | DOUBLE |  |  | Not Used. |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL |  | The unique personnel identifier of the person that the section is assigned to. |
| 11 | `SCRIPT` | VARCHAR(50) |  |  | Not Used. |
| 12 | `SECTION_ID` | DOUBLE | NOT NULL |  | Unique identifier for the summary section table. |
| 13 | `SECTION_TYPE_CD` | DOUBLE | NOT NULL |  | Defines what the section format is, e.g. header or body. |
| 14 | `SORTABLE_IND` | DOUBLE |  |  | Indicates whether the section can be sorted. |
| 15 | `SUBJECT_AREA_CD` | DOUBLE | NOT NULL | FK→ | Defines the domain of the data within the section. |
| 16 | `TMPL_SECTION_ID` | DOUBLE | NOT NULL |  | The original section_id that was used to create this section. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SUBJECT_AREA_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

