# CDS_BATCH_CONTENT_HIST

> Maintains audit information about each CDS batch content activity item.

**Description:** Commissioning Data Set - Batch Content History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Denotes the date that the activity occurred. |
| 2 | `CDS_BATCH_CNT_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely Identifies each history batch content for each CDS item. This is the unique CDS id reported to the NHS. |
| 3 | `CDS_BATCH_CONTENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the batch content record related to this historical record. |
| 4 | `CDS_BATCH_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the CDS Batch related to the Batch Content. |
| 5 | `CDS_ROW_ERROR_IND` | DOUBLE |  |  | Indicator to denote inability to add this item to a CDS (usually because we can't determine its trust) |
| 6 | `CDS_TYPE_CD` | DOUBLE | NOT NULL |  | Denotes the type of CDS activity item. |
| 7 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the encounter related to this specific batch content. |
| 8 | `FS_PARENT_ENTITY_IDENT` | VARCHAR(36) |  |  | Contains the identifier of the table from the foreign system to which this CDS activity is related. |
| 9 | `FS_PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Contains the name of the table from the foreign system to which this CDS activity is related. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the organization related to this specific batch_content. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the identifier of the table from which the activity comes. |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the name of the table from which the activity comes. |
| 13 | `PERMANENT_DEL_IND` | DOUBLE | NOT NULL |  | Indicator to denote whether this CDS activity can ever be changed from a 'delete' (UPDATE_DEL_FLAG of 1) row to an 'update/insert' (UPDATE_DEL_FLAG of 9) row. The indicator being 1 denotes the activity should never be updated to an 'upate/insert' status. |
| 14 | `SUPPRESS_IND` | DOUBLE | NOT NULL |  | Indicator field to denote whether a row of CDS activity is currentyl suppressed from publication or not. |
| 15 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | The date this row was added to history. |
| 16 | `TRANSACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The transaction type of the last transaction to occur against this CDS activity. |
| 17 | `UPDATE_DEL_FLAG` | DOUBLE |  |  | Denotes whether this is a CDS update or delete. 9 = Update; 1 = Delete |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDS_BATCH_CONTENT_ID` | [CDS_BATCH_CONTENT](CDS_BATCH_CONTENT.md) | `CDS_BATCH_CONTENT_ID` |

