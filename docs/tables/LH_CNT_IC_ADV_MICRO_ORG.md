# LH_CNT_IC_ADV_MICRO_ORG

> Child table of LH_CNT_IC_ADV_MICRO. Stores organisms found on a given microbiology culture, there can be multiple organisms per culture

**Description:** LH_CNT_IC_ADV_MICRO_ORG  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_IC_ADV_MICRO_ORG_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LH_CNT_IC_ADV_MICRO_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to LH_CNT_IC_ADV_MICRO table. |
| 5 | `LH_CNT_IC_ADV_MICRO_ORG_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `MDRO_CAT_NAME` | VARCHAR(150) |  |  | Stores the name assigned to the category. |
| 7 | `MDRO_IN_PLAN_IND` | DOUBLE | NOT NULL |  | Value can be 0 or 1. If 1, then it means that the organism is found in the MDRO plan for NHSN, else it will be 0. |
| 8 | `MICRO_SEQ_NBR` | DOUBLE |  |  | Used for uniqueness in cases where there are multiple micro records per clinical_event. |
| 9 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | A unique identifier for organism. |
| 10 | `ORGANISM_OCCURENCE_NBR` | DOUBLE |  |  | A unique number to identify parts of the same organism. |
| 11 | `PATHOGEN_NUMBER` | DOUBLE |  |  | Stores the pathogen number for the organism. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_ADV_MICRO_ID` | [LH_CNT_IC_ADV_MICRO](LH_CNT_IC_ADV_MICRO.md) | `LH_CNT_IC_ADV_MICRO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LH_CNT_IC_ADV_MICRO_ANTI](LH_CNT_IC_ADV_MICRO_ANTI.md) | `LH_CNT_IC_ADV_MICRO_ORG_ID` |

