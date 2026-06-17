# MLLD_NDC_IMAGE

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_NDC_IMAGE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_DOSEFORM_ID` | DOUBLE | NOT NULL |  | Value from MLTM_ADDITIONAL_DOSEFORM table |
| 2 | `COLOR_ID` | DOUBLE | NOT NULL |  | Value from MLTM_COLOR table |
| 3 | `FLAVOR_ID` | DOUBLE | NOT NULL |  | Value from MLTM_FLAVOR table |
| 4 | `IMAGE` | VARCHAR(50) |  |  | File Name of Image JPEG |
| 5 | `NDC_LEFT_9` | VARCHAR(9) | NOT NULL |  | First 9 digits of NDC_CODE. Primary Key for this table. |
| 6 | `SCORED` | DOUBLE |  |  | ** obsolete column - replaced by SCORED_IND. Scored Indicator. 1 = true, 0 = false. |
| 7 | `SCORED_IND` | DOUBLE | NOT NULL |  | Scored Indicator. 1 = true, 0 = false. |
| 8 | `SHAPE_ID` | DOUBLE | NOT NULL |  | Value comes from the MLTM_SHAPE table |
| 9 | `SIDE_1_MARKING` | VARCHAR(25) |  |  | Inscription on Side 1 |
| 10 | `SIDE_2_MARKING` | VARCHAR(25) |  |  | Inscription on Side 2 |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

