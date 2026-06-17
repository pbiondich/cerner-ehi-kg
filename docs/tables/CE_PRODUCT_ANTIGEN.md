# CE_PRODUCT_ANTIGEN

> ce product antigen

**Description:** ce product antigen  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIGEN_CD` | DOUBLE | NOT NULL |  | Code to describe the antigen |
| 2 | `ATTRIBUTE_IND` | DOUBLE |  |  | 1 indicates an attribute and 0 indicates an antigen |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the clinical event table. |
| 4 | `PROD_ANT_SEQ_NBR` | DOUBLE | NOT NULL |  | Sequence number to make the primary key unique when there is more than one antigen for a single product. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when this row is valid. |
| 11 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the End Point of when this row is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

