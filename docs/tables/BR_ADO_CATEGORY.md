# BR_ADO_CATEGORY

> Stores the Category Names under which the Synonyms can be grouped. Category can come from Content/Read me or User Entered from Advisor Orders Wizard.

**Description:** Bedrock Advisor Orders Category  
**Table type:** REFERENCE  
**Primary key:** `BR_ADO_CATEGORY_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_ADO_CATEGORY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_ADO_CATEGORY table. |
| 2 | `CATEGORY_MEAN` | VARCHAR(50) |  |  | Uniquely identifies the Category that is being inserted from Readme/Content. |
| 3 | `CATEGORY_NAME` | VARCHAR(100) | NOT NULL |  | Name for the Category |
| 4 | `CATEGORY_NAME_KEY` | VARCHAR(100) | NOT NULL |  | The Key version of the Category |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BR_ADO_DETAIL](BR_ADO_DETAIL.md) | `BR_ADO_CATEGORY_ID` |
| [BR_ADO_PROPOSED_DETAIL](BR_ADO_PROPOSED_DETAIL.md) | `BR_ADO_CATEGORY_ID` |

