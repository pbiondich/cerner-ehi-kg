# DSI_FEEDBACK

> This table contains decision support intervention information with user feedback.

**Description:** Decision Support Intervention Feedback  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Flag for the action taken. 0 - Other, 1 - Viewed, 2 - Canceled, 3 - Continued, 4 - Modified. |
| 2 | `ACTION_TXT` | VARCHAR(255) |  |  | Action text for other (0) Action Flag. |
| 3 | `DSI_DT_TM` | DATETIME |  |  | Date and time of the intervention. |
| 4 | `DSI_FEEDBACK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DSI_FEEDBACK table. Populated by Oracle sequence DSI_SEQ. |
| 5 | `DSI_NAME` | VARCHAR(255) |  |  | Name of the intervention the feedback is for.. |
| 6 | `ENCNTR_ID` | DOUBLE |  | FK→ | The Encounter Id associated to the intervention. |
| 7 | `FEEDBACK_TXT` | LONGBLOB |  |  | The user feedback for the intervention. |
| 8 | `LOCATION_TXT` | VARCHAR(255) |  |  | The location of the intervention. |
| 9 | `PRSNL_ID` | DOUBLE |  | FK→ | Identifier of the Personnel creating the feedback. Foreign key to the PRSNL table. |
| 10 | `RATING_NBR` | DOUBLE |  |  | The user's rating for the alert. Rating range 1-5. |
| 11 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

