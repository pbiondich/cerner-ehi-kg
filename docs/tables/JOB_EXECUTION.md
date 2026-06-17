# JOB_EXECUTION

> Stores execution details for various jobs in our system. ;

**Description:** Job Execution  
**Table type:** ACTIVITY  
**Primary key:** `JOB_EXECUTION_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETION_DT_TM` | DATETIME |  |  | The date and time this job last completed successfully. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was created. |
| 3 | `CREATE_ID` | DOUBLE |  | FK→ | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 4 | `JOB_EXECUTION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the JOB_EXECUTION table. |
| 5 | `JOB_GROUP_NAME` | VARCHAR(100) |  |  | Text identifier of the team that owns this job. |
| 6 | `JOB_NAME` | VARCHAR(50) |  |  | The name of the job being tracked. |
| 7 | `LAST_EXEC_DT_TM` | DATETIME |  |  | The last time this job began execution. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `PROCESS_TFLG` | VARCHAR(20) |  |  | The status of the job. |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MM_XFI_ASN_HEADER](MM_XFI_ASN_HEADER.md) | `JOB_EXECUTION_ID` |
| [MM_XFI_REQ_FILL](MM_XFI_REQ_FILL.md) | `JOB_EXECUTION_ID` |

