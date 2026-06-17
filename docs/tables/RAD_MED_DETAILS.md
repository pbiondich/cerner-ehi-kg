# RAD_MED_DETAILS

> This table contains detail information about medications that were administered as a part of a radiological procedure.

**Description:** Rad Med Details  
**Table type:** ACTIVITY  
**Primary key:** `RAD_MED_DETAIL_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RAD_MED_DETAIL_ID` | DOUBLE | NOT NULL | PK | This column contains a meaningless number that serves as a unique identifier for the row. |
| 2 | `RAD_MED_FIELD_ID` | DOUBLE | NOT NULL | FK→ | This column is a foreign key to the rad_med_fields table. It identifies the field that is being documented. |
| 3 | `RAD_MED_ID` | DOUBLE | NOT NULL | FK→ | This column is a foreign key to the rad_meds table. It identifies the recorded medication that the details belong to. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE_DT_TM` | DATETIME |  |  | Value date/time |
| 10 | `VALUE_NBR` | DOUBLE |  |  | Value number |
| 11 | `VALUE_TXT` | VARCHAR(255) |  |  | The value assigned to this level. The lower value within a range of values. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_MED_FIELD_ID` | [RAD_MED_FIELDS](RAD_MED_FIELDS.md) | `RAD_MED_FIELD_ID` |
| `RAD_MED_ID` | [RAD_MEDS](RAD_MEDS.md) | `RAD_MED_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_MED_DETAILS_HIST](RAD_MED_DETAILS_HIST.md) | `RAD_MED_DETAIL_ID` |

