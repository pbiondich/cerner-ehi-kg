# BR_RLI_SUPPLIER

> reference lab supplier data

**Description:** BEDROCK RLI SUPPLIER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `CONTENT_LOADED_IND` | DOUBLE |  |  | Defines whether the RLI supplier's autobuild content has been loaded |
| 3 | `DEFAULT_SELECTED_IND` | DOUBLE |  |  | Defines whether the RLI supplier is used for a specified client |
| 4 | `START_VERSION_NBR` | DOUBLE | NOT NULL |  | Identifies which version of start has been loaded |
| 5 | `SUPPLIER_FLAG` | DOUBLE | NOT NULL |  | Unique identifier for an RLI supplier |
| 6 | `SUPPLIER_MEANING` | VARCHAR(100) |  |  | String value uniquely identifying the RLI supplier |
| 7 | `SUPPLIER_NAME` | VARCHAR(100) |  |  | Describes the name of the RLI supplier |
| 8 | `SUPPLIER_PREFIX` | VARCHAR(100) |  |  | A value concatenated to the order mnemonics to identify the orders as being from the RLI supplier |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

