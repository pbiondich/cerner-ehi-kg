# BR_OC_SYNONYM

> legacy orderable synonyms

**Description:** BEDROCK OC SYNONYM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `FACILITY` | VARCHAR(50) |  |  | Used to identify individual facility data. |
| 3 | `HIDE_FLAG` | DOUBLE |  |  | The hide indicator for the order catalog item. |
| 4 | `MNEMONIC` | VARCHAR(100) |  |  | The mnemonic for the order catalog. |
| 5 | `MNEMONIC_TYPE_CD` | DOUBLE | NOT NULL |  | The mnemonic type associated to the order catalog. |
| 6 | `OC_ID` | DOUBLE | NOT NULL |  | The order catalog item unique identifier |
| 7 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VIRTUAL_VIEWS` | VARCHAR(15) |  |  | The virtual views for the order catalog item. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

