# ORD_CAT_SENT_R

> Table is used to store the relationships between order catalogs/synonyms and order sentences.

**Description:** ORDER CATALOG SENTENCE RELATIONSHIP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The code value of the orderable. |
| 3 | `DISPLAY_SEQ` | DOUBLE |  |  | contains user-defined sequencing for the display order of order sentences |
| 4 | `ORDER_CAT_SENT_R_ID` | DOUBLE | NOT NULL |  | The key to the table. |
| 5 | `ORDER_SENTENCE_DISP_LINE` | VARCHAR(255) |  |  | The display line of the order sentence. |
| 6 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL |  | The id of the order sentence |
| 7 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | The id of the order catalog synonym |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

