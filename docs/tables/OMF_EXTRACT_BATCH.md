# OMF_EXTRACT_BATCH

> Contains records that are currently being updated or inserted into the Care Profiling data repository.

**Description:** OMF Extract Batch  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDL_PARENT_ENTITY_ID` | DOUBLE |  |  | Optional additional ID required to lookup data for repository insert/update |
| 3 | `ADDL_PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Optional additional item type that is referenced by ADDL_PARENT_ENTITY_ID (ORDER, ENCOUNTER, PERSON, CLINICAL_EVENT, CHARGE) |
| 4 | `EXTRACT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The extract that is referenced by this row |
| 5 | `OMF_EXTRACT_BATCH_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the OMF_EXTRACT_BATCH table. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | ID value for the item being updtated in the Care Profiling repository |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The item type that is referenced by PARENT_ENTITY_ID (ORDER, ENCOUNTER, CLINICAL_EVENT, CHARGE) |
| 8 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | Describes the processing status of the item referenced by PARENT_ENTITY_ID. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXTRACT_TYPE_CD` | [OMF_EXTRACT_TYPE](OMF_EXTRACT_TYPE.md) | `EXTRACT_TYPE_CD` |

