# PT_PROT_PRESCREEN

> This table holds all the patients that have been pre-screened against specific protocols and their status.

**Description:** Potential Trial Candidate table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDED_VIA_FLAG` | DOUBLE | NOT NULL |  | Defines if patient was added manually or through prescreening. 0- prescreened, 1- manually added |
| 2 | `COMMENT_TEXT` | VARCHAR(4000) |  |  | Comment Text. Will be null if not used. |
| 3 | `CT_PRESCREEN_JOB_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a job in ct_prescreen_job table. |
| 4 | `MODE_IND` | DOUBLE | NOT NULL |  | This field indicates whether the potential trial candidate was found in test mode or normal mode. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table for the person who is a potential trial candidate. It is an internal system assigned number. |
| 6 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row in Prot_Master table. This field identifies the protocol on which the patient is a potential trial candidate. |
| 7 | `PT_PROT_PRESCREEN_ID` | DOUBLE | NOT NULL |  | Primary key of the pt_prot_prescreen table. It is a system assigned number ( protocol_def_seq) |
| 8 | `REASON_TEXT` | VARCHAR(2000) |  |  | Reason Comment |
| 9 | `REFERRED_DT_TM` | DATETIME |  |  | This field contains the date and time on which the potential trial candidate was referred. |
| 10 | `REFERRED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table for the person who referred the potential trial candidate. It is an internal system assigned number. |
| 11 | `SCREENED_DT_TM` | DATETIME |  |  | This field contains the date and time on which the pre-screening was run and the potential trial candidate was found. |
| 12 | `SCREENER_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table for the person ran the pre-screening. It is an internal system assigned number. |
| 13 | `SCREENING_STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the code identifying the pre-screening status of the potential trial candidate for the protocol. (17901) |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_PRESCREEN_JOB_ID` | [CT_PRESCREEN_JOB](CT_PRESCREEN_JOB.md) | `CT_PRESCREEN_JOB_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |
| `REFERRED_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCREENER_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

