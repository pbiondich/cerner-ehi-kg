# CE_MICROBIOLOGY

> ce microbiology

**Description:** CE MICROBIOLOGY  
**Table type:** ACTIVITY  
**Primary key:** `EVENT_ID`, `MICRO_SEQ_NBR`, `VALID_UNTIL_DT_TM`  
**Columns:** 16  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIOTYPE` | VARCHAR(20) |  |  | The biotype number of a microorganism |
| 2 | `EVENT_ID` | DOUBLE | NOT NULL | PK | Foreign key to the Event Table. |
| 3 | `MICRO_SEQ_NBR` | DOUBLE | NOT NULL | PK | Used for uniqueness in cases where there are multiple micro records per clinical_event |
| 4 | `OBSERVATION_PRSNL_ID` | DOUBLE | NOT NULL |  | Name of the clinician who made the observation. |
| 5 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | A unique identifier for organism. Foreign key to the Organism Table. |
| 6 | `ORGANISM_OCCURRENCE_NBR` | DOUBLE | NOT NULL |  | A unique number to identify parts of the same organism. |
| 7 | `ORGANISM_TYPE_CD` | DOUBLE | NOT NULL |  | The type of organism. |
| 8 | `POSITIVE_IND` | DOUBLE | NOT NULL |  | Indicates whether the organism was expected to be found in the culture. |
| 9 | `PROBABILITY` | DOUBLE |  |  | ** OBSOLTE** THIS COLUMN NO LONGER USED as of 3/18/05** Percent probability for this microorganism. This will be a floating point number with a value between 0 and 1. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 16 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL | PK | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CE_SUSCEPTIBILITY](CE_SUSCEPTIBILITY.md) | `EVENT_ID` |
| [CE_SUSCEPTIBILITY](CE_SUSCEPTIBILITY.md) | `MICRO_SEQ_NBR` |
| [CE_SUSCEPTIBILITY](CE_SUSCEPTIBILITY.md) | `VALID_UNTIL_DT_TM` |

