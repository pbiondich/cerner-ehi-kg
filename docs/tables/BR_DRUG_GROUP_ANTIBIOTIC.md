# BR_DRUG_GROUP_ANTIBIOTIC

> Used in Multiple Drug Resistance Organisms Bedrock Wizard. Contains the antibiotics grouped together in a drug_group.

**Description:** Bedrock Drug Group Antibiotic  
**Table type:** REFERENCE  
**Primary key:** `BR_DRUG_GROUP_ANTIBIOTIC_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | The antibiotic that is a part of this drug group. |
| 2 | `BR_DRUG_GROUP_ANTIBIOTIC_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_DRUG_GROUP_ANTIBIOTIC table. |
| 3 | `BR_DRUG_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The drug group that this antibiotic is a part of. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DRUG_GROUP_ID` | [BR_DRUG_GROUP](BR_DRUG_GROUP.md) | `BR_DRUG_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_ORGANISM_DRUG_RESULT](BR_ORGANISM_DRUG_RESULT.md) | `BR_DRUG_GROUP_ANTIBIOTIC_ID` |

