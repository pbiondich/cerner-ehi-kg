# RAD_OMF_MAMMO_FIND_DETAILS

> RadNet OMF Mammography Finding Details

**Description:** This table contains finding summary data for mammography PowerVision reports.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CERNER_MEANING_STR` | VARCHAR(25) |  |  | This column corresponds to the Cerner_meaning_str column on the rad_fol_up_field table. It uniquely identifies a field between ACR BI-RADS edtions. |
| 2 | `FIELD_DESCRIPTION` | VARCHAR(255) |  |  | This is the field description corresponding to the field description on the rad_fol_up_field table. |
| 3 | `FIND_ID` | DOUBLE | NOT NULL | FK→ | This is the foreign key to both the rad_omf_mammo_find table and the mammo_find table. |
| 4 | `FOLLOW_UP_FIELD_ID` | DOUBLE | NOT NULL | FK→ | This is the foreign key to the rad_fol_up_field table |
| 5 | `MAMMO_FIND_ID` | DOUBLE | NOT NULL |  | This it the primary key to the table. |
| 6 | `NUMERIC_VALUE` | DOUBLE | NOT NULL |  | This is the field that holds numeric summary data. |
| 7 | `PARENT1_MEANING_STR` | VARCHAR(25) |  |  | This is the parent meaning string for the Cerner meaning string on any given row. |
| 8 | `PARENT2_MEANING_STR` | VARCHAR(25) |  |  | This is the second parent meaning string for the Cerner meaning string on any given row. It is also the parent of parent 1 meaning string. |
| 9 | `PARENT3_MEANING_STR` | VARCHAR(25) |  |  | This is the third parent meaning string for the Cerner meaning string on any given row. It is also the parent of parent 2 meaning string. |
| 10 | `PARENT4_MEANING_STR` | VARCHAR(25) |  |  | This is the forth parent meaning string for the Cerner meaning string on any given row. It is also the parent of parent 3 meaning string. |
| 11 | `TEXT_VALUE` | VARCHAR(255) |  |  | This field holds string summary data. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VALUE_DT_TM` | DATETIME |  |  | This field holds date/time summary data. |
| 18 | `VALUE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIND_ID` | [MAMMO_FIND](MAMMO_FIND.md) | `FIND_ID` |
| `FOLLOW_UP_FIELD_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |

