# BR_PRSNL_ITEM_RELTN

> solutions & steps for each user

**Description:** BEDROCK PERSONNEL ITEM RELATIONSHIP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `BR_PRSNL_ID` | DOUBLE | NOT NULL |  | identifier of the user from br_prsnl table |
| 3 | `BR_PRSNL_ITEM_RELTN_ID` | DOUBLE | NOT NULL |  | BEDROCK PRSNL ITEM RELATION IDENTIFIER value |
| 4 | `ITEM_DISPLAY` | VARCHAR(255) | NOT NULL |  | display value of ""STEP"" or ""SOLUTION"" |
| 5 | `ITEM_LEAD_IND` | DOUBLE | NOT NULL |  | set to 1 if user is considered a ""leader"" (team lead, owner, etc.) for the item |
| 6 | `ITEM_MEAN` | VARCHAR(255) | NOT NULL |  | meaning of ""STEP"" or ""SOLUTION"" |
| 7 | `ITEM_TYPE` | VARCHAR(255) | NOT NULL |  | item type value |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

