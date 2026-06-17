# MAMMO_NOTIFICATION

> This table keeps track of historical notification associated with mammo follow-up.

**Description:** Mammography Notification  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FOLLOW_UP_DEFAULT_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of follow-up letter that was sent out. |
| 2 | `LETTER_ID` | DOUBLE | NOT NULL | FK→ | This is the letter id of the letter that last printed. |
| 3 | `NOTIFY_DT_TM` | DATETIME |  |  | The date and time that the letter was generated and sent. |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence that the letter(s) was sent for positive values. A negative number indicates letter type(s) that are suppressed. |
| 5 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | This identifies the study that the letters were sent out for. This is a foreign key to the Mammo_Study table. |
| 6 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This identifies the template that was used in generating the follow-up letter. This is a foreign key to the WP_Template table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LETTER_ID` | [MAMMO_LETTER](MAMMO_LETTER.md) | `LETTER_ID` |
| `STUDY_ID` | [MAMMO_STUDY](MAMMO_STUDY.md) | `STUDY_ID` |
| `TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

