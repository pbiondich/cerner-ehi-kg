# CP_PATHWAY_ACTIVITY

> Contain activity data related to a Pathway for a patient. Will indicate if a pathway has been suggested or activated for a patient.

**Description:** Care Planning Pathway Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_ADDED_IND` | DOUBLE | NOT NULL |  | Indicated if system suggested this pathway. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CLINICAL_TRIAL_IND` | DOUBLE | NOT NULL |  | Indicates if user has noted that patient is currerntly on a Clinical Trial |
| 4 | `COMMENT_TXT` | VARCHAR(1000) | NOT NULL |  | If pathway is system added the reason for suggesting. |
| 5 | `CP_PATHWAY_ACTIVITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `CP_PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Pathway this activity occurred for |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter Identifier - FK from ENCOUNTER table |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `OFF_PATHWAY_IND` | DOUBLE | NOT NULL |  | Indicates if Patient treatment is currently off Pathway |
| 10 | `PATHWAY_ACTIVITY_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the pathway activity. Active, Deleted, InError, Etc. |
| 11 | `PATHWAY_INSTANCE_ID` | DOUBLE | NOT NULL |  | Used to group rows of activity for the same instance of a pathway. The value will be pulled from a sequence (this is not a FK field). Relates to same column in CP_PATHWAY_ACTION |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person Identifier - FK from the PERSON table |
| 13 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel Identifier of User taking action |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_PATHWAY_ID` | [CP_PATHWAY](CP_PATHWAY.md) | `CP_PATHWAY_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

