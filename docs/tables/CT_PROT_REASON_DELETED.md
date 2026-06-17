# CT_PROT_REASON_DELETED

> Stores the information on why protocol information has been logically deleted from the PROT_MASTER table.

**Description:** Clinical Trials - Protocol Reason Deleted  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CT_PROT_REASON_DELETED_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `DELETION_DT_TM` | DATETIME | NOT NULL |  | The date and time the deletion occurred. |
| 3 | `DELETION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person who performed the deletion. |
| 4 | `DELETION_REASON_TXT` | VARCHAR(2000) |  |  | The reason why the deletion was done. Free Form text |
| 5 | `PARENT_PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Parent prot_master id From table prot_master. This is the foreign key for prot_master_id present in prot_master table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DELETION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PARENT_PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

