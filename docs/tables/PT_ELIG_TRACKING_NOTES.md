# PT_ELIG_TRACKING_NOTES

> This table stores notes attached to eligibility checklists filled out for patients.

**Description:** Checklist Notes  
**Table type:** ACTIVITY  
**Primary key:** `PT_ELIG_TRACKING_NOTES_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `NOTE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | references the long text for the checklist description. foreign key from the long text reference table. |
| 4 | `NOTE_TYPE_CD` | DOUBLE | NOT NULL |  | This indicates what type of note it is. |
| 5 | `PREV_PT_ELIG_TRACKING_NOTES_ID` | DOUBLE | NOT NULL | FK→ | The original value of the Pt_elig_tracking_notes_id used for grouping the related versons. Required for type 2 versioning methodology. |
| 6 | `PT_ELIG_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Identifies a unique row in the pt_elig_tracking table. This identifies the eligibility attempt to which the note is associated. |
| 7 | `PT_ELIG_TRACKING_NOTES_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PREV_PT_ELIG_TRACKING_NOTES_ID` | [PT_ELIG_TRACKING_NOTES](PT_ELIG_TRACKING_NOTES.md) | `PT_ELIG_TRACKING_NOTES_ID` |
| `PT_ELIG_TRACKING_ID` | [PT_ELIG_TRACKING](PT_ELIG_TRACKING.md) | `PT_ELIG_TRACKING_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PT_ELIG_TRACKING_NOTES](PT_ELIG_TRACKING_NOTES.md) | `PREV_PT_ELIG_TRACKING_NOTES_ID` |

