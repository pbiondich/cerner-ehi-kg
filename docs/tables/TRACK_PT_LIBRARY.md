# TRACK_PT_LIBRARY

> The Track_Pt_Library table is a child of the service resource table and contains information specific to a tracking point or library.

**Description:** Tracking Point Library  
**Table type:** REFERENCE  
**Primary key:** `SERVICE_RESOURCE_CD`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILING_METHOD_CD` | DOUBLE | NOT NULL |  | The Filing_Method_Cd identifies the filing method used within the specified library. |
| 2 | `FILING_NUMBER_LENGTH` | DOUBLE |  |  | Number of characters specified as the terminal filing number |
| 3 | `LIB_IND` | DOUBLE | NOT NULL |  | The Lib_Ind indicates if this row is a library or a tracking point. |
| 4 | `PULL_LIST_BY_SECT_IND` | DOUBLE |  |  | The Pull_List_By_Sect_Ind indicates if pull lists generated within this library should be sorted by section. |
| 5 | `PURGE_LIB_IND` | DOUBLE |  |  | The Purge_Lib_Ind indicates if this library was set up as a purge library. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The Service_Resource_Cd is a foreign key to the Service_Resource table. It uniquely identifies the library/tracking point. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [FILING_NUMBER_POSITION](FILING_NUMBER_POSITION.md) | `SERVICE_RESOURCE_CD` |
| [PULL_TRANS_REQ](PULL_TRANS_REQ.md) | `FROM_LIB_CD` |
| [PULL_TRANS_REQ](PULL_TRANS_REQ.md) | `TO_LIB_CD` |

