# MLTM_NDC_IMAGE

> Store Physical information for drug products (Shape, Color, Flavor, Inscriptions, etc.)

**Description:** MLTM NDC IMAGE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_DOSEFORM_ID` | DOUBLE | NOT NULL | FK→ | Value from MLTM_ADDITIONAL_DOSEFORM table |
| 2 | `COLOR_ID` | DOUBLE | NOT NULL | FK→ | Value from MLTM_COLOR table |
| 3 | `FLAVOR_ID` | DOUBLE | NOT NULL | FK→ | Value from MLTM_FLAVOR table |
| 4 | `IMAGE` | VARCHAR(50) |  |  | File Name of Image JPEG |
| 5 | `NDC_LEFT_9` | VARCHAR(9) | NOT NULL |  | First 9 digits of NDC_CODE. Primary Key for this table. |
| 6 | `SCORED_IND` | DOUBLE | NOT NULL |  | Scored Indicator. 1 = true, 0 = false. |
| 7 | `SHAPE_ID` | DOUBLE | NOT NULL | FK→ | Value comes from the MLTM_SHAPE table |
| 8 | `SIDE_1_MARKING` | VARCHAR(25) |  |  | Inscription on Side 1 |
| 9 | `SIDE_2_MARKING` | VARCHAR(25) |  |  | Inscription on Side 2 |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDITIONAL_DOSEFORM_ID` | [MLTM_ADDITIONAL_DOSEFORM](MLTM_ADDITIONAL_DOSEFORM.md) | `ADDITIONAL_DOSEFORM_ID` |
| `COLOR_ID` | [MLTM_COLOR](MLTM_COLOR.md) | `COLOR_ID` |
| `FLAVOR_ID` | [MLTM_FLAVOR](MLTM_FLAVOR.md) | `FLAVOR_ID` |
| `SHAPE_ID` | [MLTM_SHAPE](MLTM_SHAPE.md) | `SHAPE_ID` |

