# BR_OC_RAD_ROOM

> radiology orderable and service resource relationship

**Description:** BEDROCK OC RADIOLOGY ROOM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Unique identifier for the order catalog item. |
| 3 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The service resource associated to the order catalog item. |
| 4 | `START_VERSION_NBR` | DOUBLE |  |  | Identifies which version of start has been loaded |
| 5 | `STATUS` | DOUBLE | NOT NULL |  | The status of whether the data is committed to the HNAM database. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | date/time on which the record was added to the file |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

