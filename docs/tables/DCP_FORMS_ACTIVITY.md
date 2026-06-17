# DCP_FORMS_ACTIVITY

> Maintains record of all charting transactions performed via PowerForms

**Description:** Forms Activity Record  
**Table type:** ACTIVITY  
**Primary key:** `DCP_FORMS_ACTIVITY_ID`  
**Columns:** 21  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_ACTIVITY_DT_TM` | DATETIME |  |  | Date & Time form was first charted |
| 3 | `DCP_FORMS_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | Unique identifier for assessment |
| 4 | `DCP_FORMS_REF_ID` | DOUBLE | NOT NULL |  | Identifies form definition for activity |
| 5 | `DESCRIPTION` | VARCHAR(255) |  |  | This field is the display that will show up in the FormBrowser. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `FLAGS` | DOUBLE |  |  | //Completion Status 0 - Unknown 1 - Incomplete 2 - Complete |
| 8 | `FORM_DT_TM` | DATETIME |  |  | Date/Time that assessment was done |
| 9 | `FORM_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the results on the form |
| 10 | `FORM_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `LAST_ACTIVITY_DT_TM` | DATETIME |  |  | Last Date/Time form was modified |
| 12 | `LOCK_CREATE_DT_TM` | DATETIME |  |  | The time this row was locked for use. |
| 13 | `LOCK_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel who is currently in control of this row. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | Activity Task Id |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VERSION_DT_TM` | DATETIME |  |  | Date & time of the form definition that was documented. Used to retrieve the correct version of the form that was used to document the results. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CV_CASE](CV_CASE.md) | `FORM_ID` |
| [DCP_FORMS_ACTIVITY_COMP](DCP_FORMS_ACTIVITY_COMP.md) | `DCP_FORMS_ACTIVITY_ID` |
| [DCP_FORMS_ACTIVITY_PRSNL](DCP_FORMS_ACTIVITY_PRSNL.md) | `DCP_FORMS_ACTIVITY_ID` |

