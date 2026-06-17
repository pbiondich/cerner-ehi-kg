# WORKLIST_REF_QC

> Defines the Quality Control accesssions to be included on a worklist and where and how many times they will apear on the worklist.

**Description:** Worklist Reference Quality Control  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL |  | A unique internal system assigned number that identifies a specific Quality Control accession number to be included on a worklist. Creates a relationship to the accession table. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEGIN_IND` | DOUBLE |  |  | Indicates whether the QC accession should be listed at the beginning of the worklist. A value of zero denotes the QC accession is not to be listed at the beginning of the worklist. A value of one denotes the QC accession is to be listed at the beginning of the worklist. |
| 7 | `END_IND` | DOUBLE |  |  | Indicates whether the QC accession should be listed at the end of the worklist. A value of zero denotes the QC accession is not to be listed at the ending of the worklist. A value of one denotes the QC accession is to be listed at the ending of the worklist. |
| 8 | `INTERVAL` | DOUBLE |  |  | Defines the number of patient accessions to list on the worklist before listing the QC accession again. |
| 9 | `INTERVAL_IND` | DOUBLE |  |  | Indicates whether the QC accession should be listed at intervals on the worklist. A value of zero denotes the QC accession is not to be listed at intervals on the worklist. A value of one denotes the QC accession is to be listed at intervals on the worklist. |
| 10 | `POS` | DOUBLE |  |  | Defines the position of the QC accession on the worklist relative to other QC accessions to print on the worklist. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `WORKLIST_REF_ID` | DOUBLE | NOT NULL |  | A unique internal system assigned number that identifies a specific worklist reference template. Creates a relationship to the worklist reference table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

