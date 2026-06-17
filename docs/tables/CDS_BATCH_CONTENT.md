# CDS_BATCH_CONTENT

> Contains information about the contents of each batch.

**Description:** Commissioning Data Set - Batch Content  
**Table type:** ACTIVITY  
**Primary key:** `CDS_BATCH_CONTENT_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Denotes the date the activity occurred. |
| 2 | `CDS_BATCH_CONTENT_ID` | DOUBLE | NOT NULL | PK | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `CDS_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Reflects the ID of the latest batch this in which this item appeared. |
| 4 | `CDS_ROW_ERROR_IND` | DOUBLE |  |  | Indicator to denote inability to add this item to a CDS (usually because we can't determine its trust.) |
| 5 | `CDS_TYPE_CD` | DOUBLE | NOT NULL |  | Code value that describes the type of CDS activity item. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the encounter related to this batch content. |
| 7 | `FS_PARENT_ENTITY_IDENT` | VARCHAR(36) |  |  | Contains the identifier of the table from the foreign system to which this CDS activity is related. |
| 8 | `FS_PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Contains the name of the table from the foreign system to which this CDS activity is related. |
| 9 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the organization related to this batch content. |
| 10 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the identifier of the table that from which the activity comes. |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Table Name related to the activity of this batch content. |
| 12 | `PERMANENT_DEL_IND` | DOUBLE | NOT NULL |  | Indicator to denote whether this CDS activity can ever be changed from a 'delete' (UPDATE_DEL_FLAG of 1) row to an 'update/insert' (UPDATE_DEL_FLAG of 9) row. The indicator being 1 denotes the activity should never be updated to an 'upate/insert' status. |
| 13 | `SUPPRESS_IND` | DOUBLE | NOT NULL |  | Indicator field to denote whether a row of CDS activity is currentyl suppressed from publication or not. |
| 14 | `TRANSACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The transaction type of the last transaction to occur against this CDS activity. |
| 15 | `UPDATE_DEL_FLAG` | DOUBLE |  |  | Denotes whether this is a CDS update or delete. 9 = Update; 1 = Delete |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDS_BATCH_ID` | [CDS_BATCH](CDS_BATCH.md) | `CDS_BATCH_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CDS_BATCH_CONTENT_ALIAS](CDS_BATCH_CONTENT_ALIAS.md) | `CDS_BATCH_CONTENT_ID` |
| [CDS_BATCH_CONTENT_HIST](CDS_BATCH_CONTENT_HIST.md) | `CDS_BATCH_CONTENT_ID` |

