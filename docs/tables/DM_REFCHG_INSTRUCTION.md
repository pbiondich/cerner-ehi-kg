# DM_REFCHG_INSTRUCTION

> This table will store instructions to aid in the RDDS process

**Description:** Database Management Reference Change Instruction  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHORIZED_IND` | DOUBLE | NOT NULL |  | Indicates if the instruction was reviewed/tested by Cerner |
| 2 | `DESCRIPTION` | VARCHAR(500) | NOT NULL |  | Holds the description of what instruction does |
| 3 | `DM_REFCHG_INSTRUCTION_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 4 | `INSTRUCTION_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Points to the LONG_TEXT_ID holding the instruction |
| 5 | `INS_MEANING` | VARCHAR(50) | NOT NULL |  | Name of instruction, and alternate key |
| 6 | `RUN_ORDER` | DOUBLE |  |  | Indicates the order in which instructions should run within a given run time. |
| 7 | `RUN_TIME_FLAG` | DOUBLE | NOT NULL |  | Indicates when the instruction runs |
| 8 | `TABLE_NAME` | VARCHAR(30) |  |  | Holds what table name is affected by instruction. Can be blank |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INSTRUCTION_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

