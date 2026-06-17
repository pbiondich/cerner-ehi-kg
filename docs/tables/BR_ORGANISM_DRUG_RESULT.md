# BR_ORGANISM_DRUG_RESULT

> The possible results from the use of an antibiotic for an MDRO.

**Description:** Bedrock Organism Drug Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DRUG_GROUP_ANTIBIOTIC_ID` | DOUBLE | NOT NULL | FK→ | The antibiotic that applies this result to this organism. |
| 2 | `BR_DRUG_GROUP_ORGANISM_ID` | DOUBLE | NOT NULL | FK→ | The organism that this antibiotic is used for. |
| 3 | `BR_ORGANISM_DRUG_RESULT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the br_organism_drug_result table. |
| 4 | `RESULT_CD` | DOUBLE | NOT NULL |  | The code value of an interpretation result associated with the drug and the organism. Possible code sets are 64, 10025, and 10027 |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DRUG_GROUP_ANTIBIOTIC_ID` | [BR_DRUG_GROUP_ANTIBIOTIC](BR_DRUG_GROUP_ANTIBIOTIC.md) | `BR_DRUG_GROUP_ANTIBIOTIC_ID` |
| `BR_DRUG_GROUP_ORGANISM_ID` | [BR_DRUG_GROUP_ORGANISM](BR_DRUG_GROUP_ORGANISM.md) | `BR_DRUG_GROUP_ORGANISM_ID` |

