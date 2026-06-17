# ESO_TRANSACTION_RECORD

> Contains details of events that are processed or filtered

**Description:** ESO TRANSACTION RECORDS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter ID from the ENCOUNTER table |
| 2 | `ESO_TRANSACTION_RECORD_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique identifier from the parent table referrenced in PARENT_ENTITIY_NAME column. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the parent table for the value referrenced in PARENT_ENTITY_ID |
| 5 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicate the status of parent_entity_id0 = Not Defined 10 = Processed 20 = Filtered 30 = Hold |
| 6 | `TRANSACTION_GROUP_IDENT` | DOUBLE | NOT NULL |  | The identifer used to group the events from the CQM_FSIESO_QE table. Typically a value from that table, but can be a value not yet written to that table. Therefore, no Foreign Key relationship exists. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

