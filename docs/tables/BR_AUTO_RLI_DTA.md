# BR_AUTO_RLI_DTA

> This table stored the discrete task assays from a reference lab. This is a Bedrock autobuild content table.

**Description:** Bedrock Auto RLI data  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALIAS_NAME` | VARCHAR(100) |  |  | Reference Lab's supplied alias value for the discrete task assay. |
| 3 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 4 | `DESCRIPTION` | VARCHAR(100) |  |  | Long description of the discrete task assay. |
| 5 | `MNEMONIC` | VARCHAR(100) |  |  | Mnemonic for the discrete task assay. |
| 6 | `PERFORMING_LOC` | VARCHAR(100) |  |  | String defining where the order is performed. |
| 7 | `RLI_DTA_ID` | DOUBLE | NOT NULL |  | Unique identifier of the reference lab's discrete task assay. |
| 8 | `SUPPLIER_FLAG` | DOUBLE | NOT NULL |  | Flag value used to identify the reference lab. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

