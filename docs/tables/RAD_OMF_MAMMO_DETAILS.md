# RAD_OMF_MAMMO_DETAILS

> Radnet OMF Mammography Details

**Description:** Summary table that stores the general information related to mammo PV.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CERNER_MEANING_STR` | VARCHAR(25) |  |  | This field corresponds to the Cerner_meaning_str on the rad_fol_up_field table. It is a unique identifier for each field. |
| 2 | `FIELD_DESCRIPTION` | VARCHAR(255) |  |  | This field corresponds to the field_description column on the rad_fol_up_field table. It contains the description of the follow up field. |
| 3 | `FOLLOW_UP_FIELD_ID` | DOUBLE | NOT NULL | FK→ | This field is a foreign key to the rad_fol_up_field table. |
| 4 | `MAMMO_DETAIL_ID` | DOUBLE | NOT NULL |  | This field is the primary key. |
| 5 | `NUMERIC_VALUE` | DOUBLE | NOT NULL |  | This field holds numeric summary data. |
| 6 | `PARENT1_MEANING_STR` | VARCHAR(25) |  |  | This is the first parent meaning str of the Cerner meaning str for any given row. |
| 7 | `PARENT2_MEANING_STR` | VARCHAR(25) |  |  | This is the second parent meaning str of the Cerner meaning str for any given row. It is also the parent of the parent 1 meaning str. |
| 8 | `PARENT3_MEANING_STR` | VARCHAR(25) |  |  | This is the third parent meaning str of the Cerner meaning str for any given row. It is also the parent of the parent 2 meaning str. |
| 9 | `PARENT4_MEANING_STR` | VARCHAR(25) |  |  | This is the forth parent meaning str of the Cerner meaning str for any given row. It is also the parent of the parent 3 meaning str. |
| 10 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to the mammo_study table. |
| 11 | `TEXT_VALUE` | VARCHAR(255) |  |  | This field holds summary values of string type. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VALUE_DT_TM` | DATETIME |  |  | This field holds date/time summary values. |
| 18 | `VALUE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FOLLOW_UP_FIELD_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `STUDY_ID` | [MAMMO_STUDY](MAMMO_STUDY.md) | `STUDY_ID` |

