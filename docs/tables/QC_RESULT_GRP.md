# QC_RESULT_GRP

> Creates a grouping table for all qc results performed at the same time.

**Description:** Quality Control Group  
**Table type:** ACTIVITY  
**Primary key:** `QC_GROUP_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL |  | A unique internal system assigned number that identifies the quality control accession number associated with the QC result grouping. Creates a relationship to the accession table. |
| 2 | `GROUP_DT_TM` | DATETIME |  |  | The date and time the group of qc results were created by the system. |
| 3 | `QC_GROUP_ID` | DOUBLE | NOT NULL | PK | A unique internal system assigned number that identifies a specific grouping of several quality control results. |
| 4 | `STATUS_FLAG` | DOUBLE |  |  | Defines the status of the group of quality control results. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [QC_RESULT](QC_RESULT.md) | `QC_GROUP_ID` |

