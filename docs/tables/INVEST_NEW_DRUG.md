# INVEST_NEW_DRUG

> Contains information about investigation new drug

**Description:** INVEST NEW DRUG  
**Table type:** REFERENCE  
**Primary key:** `INVEST_NEW_DRUG_DEV_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGENT_DEV_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the drug |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Identifies the drug |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `INVEST_DRUG_NAME` | VARCHAR(255) | NOT NULL |  | Textual investigational drug name. |
| 6 | `INVEST_DRUG_NBR_TXT` | VARCHAR(12) | NOT NULL |  | Textual investigational drug number. |
| 7 | `INVEST_NEW_DRUG_DEV_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the IND/IDE |
| 8 | `NEW_DRUG_ID` | DOUBLE | NOT NULL | FK→ | A unique key for the Investigation Drug on a protocol. No two active rows can have the same new_drug_id. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AGENT_DEV_ID` | [INVEST_AGENT_DEV](INVEST_AGENT_DEV.md) | `INVEST_AGENT_DEV_ID` |
| `NEW_DRUG_ID` | [INVEST_NEW_DRUG](INVEST_NEW_DRUG.md) | `INVEST_NEW_DRUG_DEV_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INVEST_NEW_DRUG](INVEST_NEW_DRUG.md) | `NEW_DRUG_ID` |

