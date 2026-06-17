# CT_PRESCREEN_JOB

> Store the prescreening job data

**Description:** Power Trials Screening Job Data  
**Table type:** ACTIVITY  
**Primary key:** `CT_PRESCREEN_JOB_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CT_PRESCREEN_JOB_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 2 | `JOB_END_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this job ended. |
| 3 | `JOB_START_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this job started. |
| 4 | `JOB_STATUS_CD` | DOUBLE | NOT NULL |  | This field holds the status of the prescreening job. |
| 5 | `JOB_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field indicates what type of screening job this is: Prescreen Test POM(0), Prescreen Test(1) or Prescreen(2) |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the LONG_TEXT table. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prsnl table. It is the person that initiated the prescreening job. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CT_PROT_PRESCREEN_JOB_INFO](CT_PROT_PRESCREEN_JOB_INFO.md) | `CT_PRESCREEN_JOB_ID` |
| [PT_PROT_PRESCREEN](PT_PROT_PRESCREEN.md) | `CT_PRESCREEN_JOB_ID` |
| [PT_PROT_PRESCREEN_TEST](PT_PROT_PRESCREEN_TEST.md) | `CT_PRESCREEN_JOB_ID` |

