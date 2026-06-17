# UCM_FAMILY_HISTORY_REVIEW

> This table will track when a provider reviews the Consumer entered family history data.

**Description:** Unified Case Management - Family History Review  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person for which the family history was reviewed. |
| 2 | `REVIEWER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the user for the provider who reviewed the family history data. |
| 3 | `REVIEW_DT_TM` | DATETIME | NOT NULL |  | The date and time the family history data was reviewed. |
| 4 | `REVIEW_TZ` | DOUBLE | NOT NULL |  | The time zone associated to the review data and time. |
| 5 | `UCM_FAMILY_HISTORY_REVIEW_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a family history record which has been reviewed by a provider. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REVIEWER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

