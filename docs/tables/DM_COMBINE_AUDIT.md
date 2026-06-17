# DM_COMBINE_AUDIT

> Stores a history of all combine types for auditing purposes

**Description:** Database Management Combine Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_FLAG` | DOUBLE |  |  | Tells which type of application sends the transaction. |
| 2 | `CALLING_SCRIPT` | VARCHAR(30) |  |  | The script that was initially called for the combine event listed. |
| 3 | `CHILD_ENTITY_COL` | VARCHAR(32) |  |  | Name of foreign key attribute of child table |
| 4 | `CHILD_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table to which this combine row is related. |
| 5 | `CHILD_ENTITY_SCRIPT_NAME` | VARCHAR(50) |  |  | Name of the custom script to be executed for the child table |
| 6 | `COMBINE_ERROR_ID` | DOUBLE | NOT NULL |  | A unique identifier for a row in the dm_combine_error table. |
| 7 | `COMBINE_GROUP_ID` | DOUBLE | NOT NULL |  | This is a group identifier which will be unique per combine event. |
| 8 | `COMBINE_MODE` | VARCHAR(20) |  |  | Mode that the combine was run in. |
| 9 | `DM_COMBINE_AUDIT_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 10 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. |
| 11 | `END_DT_TM` | DATETIME |  |  | The end date/time of the combine event listed. |
| 12 | `FROM_ENTITY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier from the PARENT_ENTITY table of the 'from' parent entity that was combined. |
| 13 | `INST_ID` | DOUBLE | NOT NULL |  | Instance identifier |
| 14 | `LOG_LEVEL` | DOUBLE | NOT NULL |  | The level of logging associated with the combine event. (1=per combine event, 2=per table) |
| 15 | `OPERATION_TYPE` | VARCHAR(20) | NOT NULL |  | The operation being performed for the combine event listed. (Combine, Uncombine) |
| 16 | `OSUSER` | VARCHAR(30) | NOT NULL |  | Operating system client user name |
| 17 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the parent_entity¿s combine table. |
| 18 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Parent entity for the combine/uncombine (i.e. person, encounter). |
| 19 | `PROCESS_IDENT` | VARCHAR(12) |  |  | Operating system client process ID |
| 20 | `PROGRAM_NAME` | VARCHAR(48) |  |  | Operating system program name |
| 21 | `REVERSE_CMB_IND` | DOUBLE |  |  | Indicates whether or not reverse combines were used in this particular combine event. |
| 22 | `SESSION_ID` | DOUBLE | NOT NULL |  | Session identifier |
| 23 | `START_DT_TM` | DATETIME |  |  | The start date/time of the combine event listed. |
| 24 | `TO_ENTITY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier from the PARENT_ENTITY table of the 'to' parent entity that was combined into. |
| 25 | `TRANSACTION_TYPE` | VARCHAR(8) |  |  | The type of transaction that triggers the combine. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

