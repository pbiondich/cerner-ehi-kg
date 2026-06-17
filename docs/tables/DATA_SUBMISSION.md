# DATA_SUBMISSION

> This table is used to store the organizations to which data must be sent

**Description:** DATA SUBMISSION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_SUBMISSION_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 2 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | Primary key of the prot_amendment table. Identifies the protocol amendment whose data must be sent. |
| 3 | `REPORTING_CLASS_CD` | DOUBLE | NOT NULL |  | The type of data that needs to be reported |
| 4 | `SUBMITTED_TO_CD` | DOUBLE | NOT NULL |  | The org to which the data is to be sent |
| 5 | `SUBMITTED_TO_DESC` | VARCHAR(255) |  |  | Written name of the organization to which the data is to be sent |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

