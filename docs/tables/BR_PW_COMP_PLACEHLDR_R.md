# BR_PW_COMP_PLACEHLDR_R

> Relates a placeholder to a pathway component so that the pathway component can be identified as a placeholder.

**Description:** Bedrock Pathway Component Placeholder Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_PW_COMP_PLACEHLDR_ID` | DOUBLE | NOT NULL | FK→ | The header row for the Placeholder. |
| 2 | `BR_PW_COMP_PLACEHLDR_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BR_PW_COMP_PLACEHLDR_R table. |
| 3 | `INCLUDE_IND` | DOUBLE | NOT NULL |  | Indicator that controls if the placeholder will be included in the pathway by default. |
| 4 | `PATHWAY_UUID` | VARCHAR(255) | NOT NULL |  | The pathway_comp unique universal identifier. This will relate to the component in any current and future versions of the powerplan in PATHWAY_COMP. |
| 5 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicator that defines the placeholder as being required. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_PW_COMP_PLACEHLDR_ID` | [BR_PW_COMP_PLACEHLDR](BR_PW_COMP_PLACEHLDR.md) | `BR_PW_COMP_PLACEHLDR_ID` |

