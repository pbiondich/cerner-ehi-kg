# ASSIGN_REG_RELTN

> This is a relationship table between pt_prot_reg and prot_cohort tables

**Description:** This table contains the relationship between pt_prot_reg and prot_cohort tables.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGN_REG_RELTN_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the assign_reg_reltn table. It is an internal system assigned number. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COHORT_ID` | DOUBLE | NOT NULL |  | This is a logical identifier in the prot_cohort table. It uniquely identifies an active row in the prot_cohort table. No two rows with an end_effective_dt_tm of max_date (dec-31-2100) can have the same cohort_id. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `REG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the registration |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REG_ID` | [PT_PROT_REG](PT_PROT_REG.md) | `PT_PROT_REG_ID` |

