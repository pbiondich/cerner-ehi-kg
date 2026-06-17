# BR_MDRO_CAT

> Stores MDRO Category information, used in Multiple Drug Resistance Organisms (MDRO) Bedrock Wizard

**Description:** Bedrock Multiple Drug Resistance Organism Category  
**Table type:** REFERENCE  
**Primary key:** `BR_MDRO_CAT_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_MDRO_CAT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_MDRO_CAT table. |
| 2 | `CAT_TYPE_FLAG` | DOUBLE | NOT NULL |  | "This field indicates whether the category is Organism - Specific or NHSN Type. 0 - NHSN , 1 - Organism - Specific." |
| 3 | `MDRO_CAT_NAME` | VARCHAR(150) | NOT NULL |  | Stores the name assigned to the category. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BR_MDRO_CAT_EVENT](BR_MDRO_CAT_EVENT.md) | `BR_MDRO_CAT_ID` |
| [BR_MDRO_CAT_ORGANISM](BR_MDRO_CAT_ORGANISM.md) | `BR_MDRO_CAT_ID` |
| [LH_CNT_IC_MICRO_EVENT](LH_CNT_IC_MICRO_EVENT.md) | `MDRO_CAT_ID` |

