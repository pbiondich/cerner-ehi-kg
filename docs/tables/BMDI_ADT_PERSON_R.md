# BMDI_ADT_PERSON_R

> BMDI Acquired Data Track Person Relationship. Extends BMDI_ACQUIRED_DATA_TRACK database table with details of the person associated with the bedside medical device. Multiple rows could exist in this table for a specific row in BMDI_ACQUIRED_DATA_TRACK

**Description:** BMDI Acquired Data Track Person Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSOCIATION_ID` | DOUBLE | NOT NULL | FK→ | Referring parent - Primary key in bmdi_acquired_data_track database table |
| 3 | `ASSOCIATION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Associating clinical personnel identifier - Equivalent to PERSON_ID in PRSNL database table |
| 4 | `BMDI_ADT_PERSON_R_ID` | DOUBLE | NOT NULL |  | Primary key |
| 5 | `DIS_ASSOCIATION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Disassociation Clinical Personnel Identifier. Equivalent to PERSON_ID in PRSNL table. |
| 6 | `ENCNTR_ALIAS` | VARCHAR(200) |  |  | Encounter alias value in Person Data Model - equivalent to ALIAS in ENCNTR_ALIAS database table |
| 7 | `ENCNTR_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter alias type code value in Person Data Model - equivalent to ENCOUNTER_ALIAS_TYPE_CD in ENCNTR_ALIAS database table, like, FIN, Encounter Number etc. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Primary key in ENCOUNTER database table |
| 9 | `HEIGHT_UNITS_CD` | DOUBLE | NOT NULL |  | Code value defining UNIT of PERSON_HEIGHT |
| 10 | `PERSON_ALIAS` | VARCHAR(200) |  |  | Person alias value in Person Data Model - equivalent to ALIAS in PERSON_ALIAS database table |
| 11 | `PERSON_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter alias type code value in Person Data Model - equivalent to ENCOUNTER_ALIAS_TYPE_CD in ENCNTR_ALIAS database table, like, FIN, Encounter Number etc. |
| 12 | `PERSON_BIRTH_DT_TM` | DATETIME |  |  | Equivalent to BIRTH_DT_TM in PERSON database table |
| 13 | `PERSON_GENDER_CD` | DOUBLE | NOT NULL |  | Code value defining gender |
| 14 | `PERSON_HEIGHT` | VARCHAR(255) |  |  | Result value in clinical event data model - equivalent to RESULT_VAL in CLINICAL_EVENT database table, corresponding value for EVENT_SET_CD_DISP_KEY of HEIGHT in V500_EVENT_SET_CODE database table |
| 15 | `PERSON_NAME` | VARCHAR(100) | NOT NULL |  | Person name value in Person Data Model - equivalent to NAME_FULL_FORMATTED in PERSON database table |
| 16 | `PERSON_WEIGHT` | VARCHAR(255) |  |  | Result value in clinical event data model - equivalent to RESULT_VAL in CLINICAL_EVENT database table, corresponding value for EVENT_SET_CD_DISP_KEY of WEIGHT in V500_EVENT_SET_CODE database table |
| 17 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Process Status Flag - Flag values to be documented... |
| 18 | `STATUS_MESSAGE` | VARCHAR(255) |  |  | A Status Message for the process |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `WEIGHT_UNITS_CD` | DOUBLE | NOT NULL |  | Code value defining UNIT of PERSON_WEIGHT |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSOCIATION_ID` | [BMDI_ACQUIRED_DATA_TRACK](BMDI_ACQUIRED_DATA_TRACK.md) | `ASSOCIATION_ID` |
| `ASSOCIATION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DIS_ASSOCIATION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

