# LH_CNT_READMIT_WORKLIST

> This table will contain a list of patients to be displayed in the Readmission Worklist Mpage

**Description:** LH_CNT_READMIT_WORKLIST  
**Table type:** ACTIVITY  
**Primary key:** `LH_CNT_READMIT_WORKLIST_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDED_DT_TM` | DATETIME | NOT NULL |  | Date and Time the row was added to the table. |
| 3 | `ADDED_REASON_CD` | DOUBLE | NOT NULL |  | Reason for manually adding a patient to the worklist. |
| 4 | `ADDED_UPDT_ID` | DOUBLE | NOT NULL |  | User who manually added the patient to the worklist. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter_ID for the patient qualified for Readmission Risk. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LH_CNT_READMIT_WORKLIST_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CNT_READMIT_WORKLIST table. |
| 9 | `MANUALLY_ADDED_IND` | DOUBLE | NOT NULL |  | Indicates that this row was manually added to the worklist. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | PERSON_ID for the patient qualified for Readmission Risk. |
| 11 | `RATING_DT_TM` | DATETIME | NOT NULL |  | Date/Time the rating was updated. |
| 12 | `RATING_REASON_CD` | DOUBLE | NOT NULL |  | Represents the reason the individual increased or decreased the rating for this person. |
| 13 | `RATING_UPDT_ID` | DOUBLE | NOT NULL |  | Individual that updated the rating. |
| 14 | `RATING_VALUE` | DOUBLE | NOT NULL |  | Represents the persons rating on the worklist. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [LH_CNT_READMIT_RISK](LH_CNT_READMIT_RISK.md) | `LH_CNT_READMIT_WORKLIST_ID` |
| [LH_CNT_READMIT_STATUS](LH_CNT_READMIT_STATUS.md) | `LH_CNT_READMIT_WORKLIST_ID` |
| [LH_CNT_WL_RATING](LH_CNT_WL_RATING.md) | `LH_CNT_READMIT_WORKLIST_ID` |

