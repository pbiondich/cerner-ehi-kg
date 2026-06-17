# CT_RN_PROT_RUN

> This table stores the research network run data for protocols.

**Description:** Research Network Protocol Run  
**Table type:** ACTIVITY  
**Primary key:** `CT_RN_PROT_RUN_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETED_FLAG` | DOUBLE | NOT NULL |  | This field contains the current status for the research network run. 0=Incomplete 1=Completed Successfully 2=Forced Completion |
| 2 | `CT_RN_PROT_RUN_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 3 | `NEXT_RUN_DT_TM` | DATETIME |  |  | the eligible date/time the protocol should be run through the research network. |
| 4 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | this field uniquely identifies a row in the prot_master table. |
| 5 | `PT_SENT_NBR` | DOUBLE | NOT NULL |  | This field contains the number of patient sent from the research network. |
| 6 | `RUN_GROUP_ID` | DOUBLE | NOT NULL |  | this field uniquely identifies a research network run.This value is pulled from the sequence and used as a grouper for several rows. The value has no relation to a PK ID value from any particular row. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CT_RN_RUN_ACTIVITY](CT_RN_RUN_ACTIVITY.md) | `CT_RN_PROT_RUN_ID` |

