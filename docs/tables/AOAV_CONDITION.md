# AOAV_CONDITION

> Activity table to store the conditions that attributed to a patient's outcomes

**Description:** AOAV_CONDITION  
**Table type:** ACTIVITY  
**Primary key:** `AOAV_CONDITION_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AOAV_COMP_CD` | DOUBLE | NOT NULL |  | Code value that identifies an AOAV Component. Code Set 400806 |
| 6 | `AOAV_CONDITION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `AOAV_PERSON_ENCNTR_ID` | DOUBLE | NOT NULL |  | #OBSOLETE in DBARCHDTL-22877 -; Unique identifier of an AOAV_PERSON_ENCNTR |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CALCULATED_FLAG` | DOUBLE | NOT NULL |  | The calculated flag giving the state of the event.0-Needs to be calculated; 1- calculation in progress; 2-calculation done |
| 10 | `ENCNTR_ID` | DOUBLE |  | FK→ | Unique Identifier of the encounter; |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `ERROR_STATUS_FLAG` | DOUBLE | NOT NULL |  | The error status flag (0 = no error, 1 = in error, 2 = invalid) |
| 13 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value from the NOMENCLATURE table |
| 14 | `PERSON_ID` | DOUBLE |  | FK→ | Unique Identifier of the person; |
| 15 | `SOURCE_ENTITY_COLUMN` | VARCHAR(30) |  |  | Column name of the SOURCE_ENTITY_ID E.g. DIAGNOSIS_GROUP, PROBLEM_ID, PROCEDURE_ID |
| 16 | `SOURCE_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier of source condition from the SOURCE_ENTITY_NAME. |
| 17 | `SOURCE_ENTITY_NAME` | VARCHAR(30) |  |  | Name of the table of SOURCE_ENTITY_ID , SOURCE_ENTITY_COLUMN ( I.e. DIAGNOSIS, PROBLEM, PROCEDURE) |
| 18 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Status flag to represent the Active(0), Inactive (1), Canceled (2), Resolved(3) status of the condition. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AOAV_OUTCOME_COMP_COND_R](AOAV_OUTCOME_COMP_COND_R.md) | `AOAV_CONDITION_ID` |

