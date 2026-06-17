# BR_DRUG_GROUP

> Method to group drugs. Used in Multiple Drug Resistance Organisms Bedrock Wizard.

**Description:** Bedrock Drug Group  
**Table type:** REFERENCE  
**Primary key:** `BR_DRUG_GROUP_ID`  
**Columns:** 7  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DRUG_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BR_DRUG_GROUP table. |
| 2 | `DRUG_GROUP_NAME` | VARCHAR(150) | NOT NULL |  | The name assigned to the drug group. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BR_DRUG_GROUP_ANTIBIOTIC](BR_DRUG_GROUP_ANTIBIOTIC.md) | `BR_DRUG_GROUP_ID` |
| [BR_DRUG_GROUP_ORGANISM](BR_DRUG_GROUP_ORGANISM.md) | `BR_DRUG_GROUP_ID` |

