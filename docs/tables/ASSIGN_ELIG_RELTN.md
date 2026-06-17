# ASSIGN_ELIG_RELTN

> This table contains the relation between pt_elig_tracking and prot_cohort tables

**Description:** ASSIGN ELIGIBILITY RELATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGN_ELIG_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the assign_elig_reltn table. It is an internal system assigned number. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COHORT_ID` | DOUBLE | NOT NULL |  | A logical identifier in the prot_cohort table. No two rows in the prot_cohort table will have the same cohort_id when end_effective_dt_tm = 31-dec-2100 |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PT_ELIG_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pt_elig_tracking table. It is an internal system assigned number. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PT_ELIG_TRACKING_ID` | [PT_ELIG_TRACKING](PT_ELIG_TRACKING.md) | `PT_ELIG_TRACKING_ID` |

