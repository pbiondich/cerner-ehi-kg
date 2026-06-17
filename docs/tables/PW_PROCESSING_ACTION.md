# PW_PROCESSING_ACTION

> pathway processing action

**Description:** This table is used to track pathways that are being processed by the pw server  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 2 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL |  | Pathway catalog id of the pathway that is being processed.Column |
| 3 | `PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway that is being created or updated.Column |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `PROCESSING_START_DT_TM` | DATETIME |  |  | Date and time that processing started on the pathway.Column |
| 6 | `PROCESSING_UPDT_CNT` | DOUBLE | NOT NULL |  | The value of the update count on the pathway table after the processing is complete. |
| 7 | `PW_GROUP_NBR` | DOUBLE |  |  | Unique id from pathway table used to group multiple phases as a group to form a multi-phase pathway. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `WORKFLOW_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The LONG_BLOB_ID for all workflows on the phase and are signed (from the LONG_BLOB table). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `WORKFLOW_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

