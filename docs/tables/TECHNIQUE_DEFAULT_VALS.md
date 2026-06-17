# TECHNIQUE_DEFAULT_VALS

> This table contains the default fields and values that are to be prompted for at exam completion time.

**Description:** Radiology Technique Default Values  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXPOSURE_FIELD_CD` | DOUBLE | NOT NULL |  | This column identifies the exposure field that the default value is being specified for. |
| 2 | `EXPOSURE_VALUE_ID` | DOUBLE |  | FK→ | This column is a foreign key to the rad_exposure_values table. It uniquely identifies the default value for the given exposure field. |
| 3 | `TECHNIQUE_DEFAULT_ID` | DOUBLE | NOT NULL | FK→ | This column is a foreign key to the technique_default table. It identifies the catalog_cd/department_cd/exam_room_cd that the default fields and values are assigned to. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE_NUMERIC` | DOUBLE |  |  | This column contains the default numeric value if the field is a numeric field. |
| 10 | `VALUE_TEXT` | VARCHAR(255) |  |  | This column contains the textual value for the exposure field. If it is a text type field. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPOSURE_VALUE_ID` | [RAD_EXPOSURE_VALUES](RAD_EXPOSURE_VALUES.md) | `EXPOSURE_VALUE_ID` |
| `TECHNIQUE_DEFAULT_ID` | [TECHNIQUE_DEFAULTS](TECHNIQUE_DEFAULTS.md) | `TECHNIQUE_DEFAULT_ID` |

