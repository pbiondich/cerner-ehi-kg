# PT_PROT_PRESCREEN_TEST

> Store the test screening matches temporarily for each protocol and the corresponding job.

**Description:** PowerTrials Test Screening Matches  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CT_PRESCREEN_JOB_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a job in ct_prescreen_job table. |
| 2 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table for the person who is a potential trial candidate. it is an internal system assigned number. |
| 3 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_master table. |
| 4 | `PT_PROT_PRESCREEN_TEST_ID` | DOUBLE | NOT NULL |  | Primary key |
| 5 | `SCREENED_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time on which the pre-screening was run and the potential trial candidate was found. |
| 6 | `SCREENER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the prsnl table for the person ran the pre-screening. it is an internal system assigned number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_PRESCREEN_JOB_ID` | [CT_PRESCREEN_JOB](CT_PRESCREEN_JOB.md) | `CT_PRESCREEN_JOB_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |
| `SCREENER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

