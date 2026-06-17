# BR_CKI_CLIENT_INFO

> Stores data type information for each client using the CKI Mapping wizard

**Description:** Bedrock CKI Client Info  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `CLIENT_ID` | DOUBLE | NOT NULL |  | Unique id for the client |
| 3 | `CLIENT_INFO_ID` | DOUBLE | NOT NULL |  | Unique id for the BR_CKI_client_info |
| 4 | `DATA_TYPE_ID` | DOUBLE | NOT NULL |  | Unique id for the BR_CKI data type |
| 5 | `EXPORT_IND` | DOUBLE |  |  | Indicates if mapping was done and an extract was created |
| 6 | `LOAD_DT_TM` | DATETIME |  |  | Date that the data set was loaded for mapping |
| 7 | `LOCK_IND` | DOUBLE |  |  | Indicates if mapping is currently being performed for a client/data type |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

