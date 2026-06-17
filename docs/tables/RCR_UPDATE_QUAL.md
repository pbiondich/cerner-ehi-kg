# RCR_UPDATE_QUAL

> This table contains all quailified IDs per each execution of a Revenue Cycle Analytics cleanup and or update script.

**Description:** Revenue Cycle - Update Qualified  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | Date and time the row was added. |
| 2 | `PROCESS_IND` | DOUBLE | NOT NULL |  | Indicates whether the particular ID is processed by the execution script or not. |
| 3 | `QUALIFIED_IDENT` | DOUBLE | NOT NULL |  | The identifier that qualified as a part of the qualification process. |
| 4 | `QUAL_BEGIN_DT_TM` | DATETIME |  |  | Stores the begin date from the input prompt. |
| 5 | `QUAL_END_DT_TM` | DATETIME |  |  | Stores the end date from the input prompt. |
| 6 | `RCR_UPDATE_QUAL_ID` | DOUBLE | NOT NULL |  | Unique generated umber that identifies a single row on the RCR_UPDATE_QUAL_ID. |
| 7 | `RCR_UPDATE_REGISTRY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related RCR_UPDATE_REGISTRY record. |
| 8 | `REQUALIFIED_IND` | DOUBLE | NOT NULL |  | Indicates whether the corresponing ID is requalified during the cleanup validation process. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCR_UPDATE_REGISTRY_ID` | [RCR_UPDATE_REGISTRY](RCR_UPDATE_REGISTRY.md) | `RCR_UPDATE_REGISTRY_ID` |

