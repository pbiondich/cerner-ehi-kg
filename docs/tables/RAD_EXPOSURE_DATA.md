# RAD_EXPOSURE_DATA

> Rad Exposure Data

**Description:** This table contains the exposure fields assigned to a specific exam.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXPOSURE_FIELD_CD` | DOUBLE | NOT NULL |  | This field identifies which field the value corresponds with. |
| 2 | `EXP_VALUE_FREETEXT` | VARCHAR(255) |  |  | This column contains the free text response, if the field is of type free-text. |
| 3 | `EXP_VALUE_ID` | DOUBLE | NOT NULL | FK→ | This column contains the coded value if the field is a codified field. |
| 4 | `EXP_VALUE_NBR` | DOUBLE |  |  | This column contains the numeric entry if this field is of type number. |
| 5 | `RAD_EXPOSURE_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the Rad_Exposure table. It uniquely identifies the exposure related to a specific exam. |
| 6 | `SEQUENCE` | DOUBLE |  |  | The sequence field indicates which order the fields should be displayed in. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXP_VALUE_ID` | [RAD_EXPOSURE_VALUES](RAD_EXPOSURE_VALUES.md) | `EXPOSURE_VALUE_ID` |
| `RAD_EXPOSURE_ID` | [RAD_EXPOSURE](RAD_EXPOSURE.md) | `RAD_EXPOSURE_ID` |

