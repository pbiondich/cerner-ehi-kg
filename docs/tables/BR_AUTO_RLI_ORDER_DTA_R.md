# BR_AUTO_RLI_ORDER_DTA_R

> This table stores the relationship between a reference lab's orderable items and discrete task assays. This is an autobuild content table used in the Bedrock Reference Lab Interface Wizard.

**Description:** Bedrock Auto RLI Order DTA Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 3 | `RLI_DTA_ID` | DOUBLE | NOT NULL |  | Unique identifier for the reference lab discrete task assay. |
| 4 | `RLI_ORDER_ID` | DOUBLE | NOT NULL |  | Unique identifier for the reference lab orderable item. |
| 5 | `SUPPLIER_FLAG` | DOUBLE | NOT NULL |  | Flag value used to identify the reference lab. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

