# BR_MDRO_CAT_ORGANISM

> Stores information about Multiple Drug Resistance Organisms and their Category information , used in Multiple Drug Resistance Organisms (MDRO) Bedrock Wizard.

**Description:** Bedrock Multiple Drug Resistance Organism Category Organism  
**Table type:** REFERENCE  
**Primary key:** `BR_MDRO_CAT_ORGANISM_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTICS_TXT` | VARCHAR(500) | NOT NULL |  | A string representation of the antibiotics that are used for this MDRO. |
| 2 | `BR_MDRO_CAT_ID` | DOUBLE | NOT NULL | FK→ | Stores Category ID of the Category this Organism is associated to. |
| 3 | `BR_MDRO_CAT_ORGANISM_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_MDRO_CAT_ORGANISM table. |
| 4 | `BR_MDRO_ID` | DOUBLE | NOT NULL | FK→ | A pointer to the name and other base information of the MDRO. |
| 5 | `GROUP_RESISTANT_CNT` | DOUBLE | NOT NULL |  | Stores the number of Drug Groups this organism must be resistant to before it is classified as drug-resistant. |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Indicates the MDRO category and organism combination is only valid for the given location code_value. |
| 7 | `LOOKBACK_TIME_SPAN_NBR` | DOUBLE | NOT NULL |  | Time period used for building a worklist. |
| 8 | `LOOKBACK_TIME_SPAN_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the lookback time span. |
| 9 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | The organism that is defined as multiple-drug resistant. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_MDRO_CAT_ID` | [BR_MDRO_CAT](BR_MDRO_CAT.md) | `BR_MDRO_CAT_ID` |
| `BR_MDRO_ID` | [BR_MDRO](BR_MDRO.md) | `BR_MDRO_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_DRUG_GROUP_ORGANISM](BR_DRUG_GROUP_ORGANISM.md) | `BR_MDRO_CAT_ORGANISM_ID` |

