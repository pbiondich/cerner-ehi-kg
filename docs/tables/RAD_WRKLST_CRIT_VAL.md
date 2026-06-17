# RAD_WRKLST_CRIT_VAL

> This table models the criteria element values of a radiologists reading worklist.

**Description:** Radiology Worklist Criteria Value  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `END_OFFSET_QTY` | DOUBLE |  |  | The end offset for a range type value |
| 6 | `END_OFFSET_UNIT_CD` | DOUBLE | NOT NULL |  | The end offset unit identifier for a range type value |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the parent table row associated to the criteria value. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This is the name of the parent table where the value in parent_entity_id originates. |
| 9 | `RAD_WRKLST_CRIT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the criteria the value is associated with. |
| 10 | `RAD_WRKLST_CRIT_VAL_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RAD_WRKLST_CRIT_VAL table. |
| 11 | `START_OFFSET_QTY` | DOUBLE |  |  | The start offset for a range type value |
| 12 | `START_OFFSET_UNIT_CD` | DOUBLE | NOT NULL |  | The start offset unit identifier for a range type value |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_WRKLST_CRIT_ID` | [RAD_WRKLST_CRIT](RAD_WRKLST_CRIT.md) | `RAD_WRKLST_CRIT_ID` |

