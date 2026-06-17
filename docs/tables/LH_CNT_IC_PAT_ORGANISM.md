# LH_CNT_IC_PAT_ORGANISM

> This table will contain a list of organisms corresponding to each lab entry in LH_CNT_IC_PATIENT_LAB.

**Description:** Lighthouse Content Infection control Patient Organisms  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event id associated with the microbiology result. |
| 2 | `LH_CNT_IC_PAT_ORGANISM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_PAT_LAB_ORGANISM table. |
| 3 | `MICRO_SEQ_NBR` | DOUBLE | NOT NULL |  | Defines uniqueness in cases with multiple micro records per clinical event. |
| 4 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | Code value of the organism. |
| 5 | `ORGANISM_DESCRIPTION` | VARCHAR(80) | NOT NULL |  | The description of the organism including occurrence number, causing infection. |
| 6 | `ORGANISM_OCCURRENCE_NBR` | DOUBLE | NOT NULL |  | A unique number to identify parts of the same organism. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id row from the Parent Entity table. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the Parent Entity Table |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | The date time until which the ce_microbiology result is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

