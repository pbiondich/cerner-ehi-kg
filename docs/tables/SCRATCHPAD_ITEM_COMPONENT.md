# SCRATCHPAD_ITEM_COMPONENT

> Contains the component data elements associated to a scratchpad item.

**Description:** Scratchpad Item Component  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DATA_BLOB` | LONGBLOB |  |  | The raw data stored to the scratchpad item component. |
| 3 | `DATA_BLOB_SIZE` | DOUBLE |  |  | Used to store the size of the blob column. |
| 4 | `DATA_CONCEPT_NAME` | VARCHAR(100) | NOT NULL |  | The concept used to identify the data that is stored within the data_blob. |
| 5 | `DELETE_IND` | DOUBLE | NOT NULL |  | Indicates if the scratchpad item component has been deleted. |
| 6 | `ITEM_SEQ` | DOUBLE | NOT NULL |  | The scratchpad item sequence. Identifies the order in which components were added to this table. |
| 7 | `SCRATCHPAD_ITEM_COMPONENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the scratchpad_item_component table. |
| 8 | `SCRATCHPAD_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The scratchpad item identifier to which this component is associated. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCRATCHPAD_ITEM_ID` | [SCRATCHPAD_ITEM](SCRATCHPAD_ITEM.md) | `SCRATCHPAD_ITEM_ID` |

