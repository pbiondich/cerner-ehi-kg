# MAMMO_LETTER

> This table contains all of the Notification letters that can print out of Mammo

**Description:** Mammography Letter  
**Table type:** REFERENCE  
**Primary key:** `LETTER_ID`  
**Columns:** 11  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | This field determines whether or not the letter is the default letter for the specified recommendation. There should only be one letter with the default set to 1 for each recommendation. |
| 3 | `DESCRIPTION` | VARCHAR(100) |  |  | This is the Description of the Letter. |
| 4 | `LETTER_ID` | DOUBLE | NOT NULL | PK | This is a unique meaningless number to represent each letter. |
| 5 | `LETTER_TYPE_FLAG` | DOUBLE | NOT NULL |  | This determines whether the letter is a Notification, Warning, etc. |
| 6 | `RECOMMENDATION_ID` | DOUBLE | NOT NULL | FK→ | This is the Recommendation that a letter is associated with. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RECOMMENDATION_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [MAMMO_LETTER_DETAIL](MAMMO_LETTER_DETAIL.md) | `LETTER_ID` |
| [MAMMO_NOTIFICATION](MAMMO_NOTIFICATION.md) | `LETTER_ID` |
| [MAMMO_NOTIFICATION_HIST](MAMMO_NOTIFICATION_HIST.md) | `LETTER_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `LETTER_ID` |
| [RAD_MAMMO_LETTER_MGMT_R](RAD_MAMMO_LETTER_MGMT_R.md) | `LETTER_ID` |

