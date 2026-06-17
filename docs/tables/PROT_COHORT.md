# PROT_COHORT

> This table contains information about the cohorts of a stratum

**Description:** PROT COHORT  
**Table type:** REFERENCE  
**Primary key:** `PROT_COHORT_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `COHORT_ID` | DOUBLE | NOT NULL |  | Logical identifier into the prot_cohort table. No two active rows (End_effective_dt_tm = 31-dec-2100) will have the same cohort_id |
| 3 | `COHORT_LABEL` | VARCHAR(30) | NOT NULL |  | Display label for the cohort (Has to be less than 30 character in length) |
| 4 | `COHORT_STATUS_CD` | DOUBLE | NOT NULL |  | A code value indicating the status of the cohort. It can be Open, Closed or Suspended |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PARENT_COHORT_ID` | DOUBLE | NOT NULL | FK→ | The link back to the cohort_id that this cohort originated or was copied from. |
| 7 | `PROT_COHORT_DESCRIPTION` | VARCHAR(2000) |  |  | Description of the cohort |
| 8 | `PROT_COHORT_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the prot_cohort table. It is an internal system assigned number. |
| 9 | `PT_ACCRUAL` | DOUBLE |  |  | Number of patients to be accrued on the cohort |
| 10 | `STATUS_CHG_REASON_CD` | DOUBLE | NOT NULL |  | A code value indicating the reason for change in the status of cohort |
| 11 | `STRATUM_ID` | DOUBLE | NOT NULL |  | Identifies a row in the prot_stratum table. It identifies the stratum to which this cohort belongs. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | The date on which the cohort becomes valid |
| 18 | `VALID_TO_DT_TM` | DATETIME | NOT NULL |  | The date till which the cohort is valid. It can't accrue patients after this date. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_COHORT_ID` | [PROT_COHORT](PROT_COHORT.md) | `PROT_COHORT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PROT_COHORT](PROT_COHORT.md) | `PARENT_COHORT_ID` |

