# RAD_EXPOSURE_VALUES

> This field stores the user defined values for radiology exposure fields.

**Description:** Radiology Exposure Values  
**Table type:** REFERENCE  
**Primary key:** `EXPOSURE_VALUE_ID`  
**Columns:** 10  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESCRIPTION` | VARCHAR(255) |  |  | This is the description of the exposure value. |
| 3 | `EXPOSURE_FIELD_CD` | DOUBLE | NOT NULL |  | This column identifies the exposure field that this value is related to. |
| 4 | `EXPOSURE_VALUE_ID` | DOUBLE | NOT NULL | PK | The Exposure Value Id serves as a unique identifier for a given row. |
| 5 | `SEQUENCE` | DOUBLE |  |  | The Sequence field determines which order the values should appear when listed. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RAD_EXPOSURE_DATA](RAD_EXPOSURE_DATA.md) | `EXP_VALUE_ID` |
| [SERVICE_DIRECTORY](SERVICE_DIRECTORY.md) | `RAD_ORGAN_ID` |
| [TECHNIQUE_DEFAULT_VALS](TECHNIQUE_DEFAULT_VALS.md) | `EXPOSURE_VALUE_ID` |

