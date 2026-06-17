# BR_AUTO_RLI_SYNONYM

> stores additional synonyms for each reference lab orderable item

**Description:** Bedrock Auto RLI Synonym  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `RLI_ORDER_ID` | DOUBLE | NOT NULL |  | stores the id of the related parent row on the br_auto_rli_order table |
| 3 | `SUPPLIER_FLAG` | DOUBLE | NOT NULL |  | stores the value identifying the reference lab interface |
| 4 | `SYNONYM_NAME` | VARCHAR(100) |  |  | Name of the synonym |
| 5 | `SYNONYM_SEQ` | DOUBLE | NOT NULL |  | a sequence number used to make the row unique |
| 6 | `SYNONYM_TYPE_FLAG` | DOUBLE |  |  | stores a flag value identifying the synonym type |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

