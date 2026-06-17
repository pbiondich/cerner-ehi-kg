# AP_PREFIX_STATION_R

> This table establishes the relationship between an image station and the prefix report combination for which it is valid.

**Description:** ap_prefix_station_r  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field is used to identify the anatomic pathology report for which an image station can be used. |
| 2 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value for the anatomic pathology prefix for which the image station is valid. |
| 3 | `PUBLISH_FLAG` | DOUBLE | NOT NULL |  | This field establishes whether or not an image should default to "chartable" or not when an image is acquired at a given image station. |
| 4 | `STATION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique image station identifier from the ap_image_station table. |
| 5 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | This field contains the unique value of the default anatomic pathology report section that images should be associated to when they are acquired at a given imaging station. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |
| `STATION_ID` | [AP_IMAGE_STATION](AP_IMAGE_STATION.md) | `STATION_ID` |

