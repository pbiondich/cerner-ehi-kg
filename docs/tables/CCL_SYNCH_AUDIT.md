# CCL_SYNCH_AUDIT

> Audits export and import activity for CCL dictionary objects within the RDDS/synchronization process

**Description:** CCL Synchronize Audit  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_TM` | DATETIME | NOT NULL |  | The Begin date and time of the operation |
| 2 | `CCL_SYNCH_AUDIT_ID` | DOUBLE | NOT NULL |  | Primary Key - Unique row identifier |
| 3 | `END_DT_TM` | DATETIME | NOT NULL |  | The End date and time of the operation |
| 4 | `NODE_NAME` | VARCHAR(20) | NOT NULL |  | UNIX/VMS node name |
| 5 | `OBJECT_NAME` | VARCHAR(30) | NOT NULL |  | Discern Explorer Object Name |
| 6 | `OPERATION` | VARCHAR(10) | NOT NULL |  | The name of the merge operation (IMPORT/EXPORT/etc.) |
| 7 | `OP_MODE` | VARCHAR(1) | NOT NULL |  | The mode passed to the import/export operation |
| 8 | `STATUS` | VARCHAR(10) | NOT NULL |  | The status of the import/export operation |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

