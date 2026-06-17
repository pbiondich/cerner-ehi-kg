# BR_PW_COMP_PLACEHLDR

> Defines a placeholder for a pathway component. A placeholder can be linked to a pathway component so that it can later be replaced with a different pathway component.

**Description:** Bedrock Pathway Component Placeholder  
**Table type:** REFERENCE  
**Primary key:** `BR_PW_COMP_PLACEHLDR_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_PW_COMP_PLACEHLDR_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_PW_COMP_PLACEHLDR table. |
| 2 | `COMP_TYPE_FLAG` | DOUBLE | NOT NULL |  | Component type flag that represents the intended use of the placeholder. |
| 3 | `PLACEHLDR_NAME` | VARCHAR(100) | NOT NULL |  | Name of placeholder. |
| 4 | `PLACEHLDR_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Name of placeholder in all uppercase. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_PW_COMP_PLACEHLDR_R](BR_PW_COMP_PLACEHLDR_R.md) | `BR_PW_COMP_PLACEHLDR_ID` |

