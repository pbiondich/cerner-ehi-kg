# RAD_MED_DETAILS_HIST

> This table contains a history of changes that have been made to the rad_meds and rad_med_details tables

**Description:** Radiology medication detail history  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_DT_TM` | DATETIME |  |  | This column will contain the administration Date/time of the med |
| 2 | `MODIFIED_DT_TM` | DATETIME | NOT NULL |  | This column is the date that the data was modified on. |
| 3 | `MODIFIED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the personnel that modified the data |
| 4 | `RAD_MED_DETAILS_HIST_ID` | DOUBLE | NOT NULL |  | This column contains a meaningless number that serves the purpose of uniquely identifying a row |
| 5 | `RAD_MED_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | This column is a foreign key to the rad_med_details table. |
| 6 | `RAD_MED_FIELD_ID` | DOUBLE | NOT NULL |  | This column is a foreign key to the rad_med_fields table |
| 7 | `RAD_MED_ID` | DOUBLE | NOT NULL |  | This column is a foreign key to the rad_meds table |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_DT_TM` | DATETIME |  |  | This column will contain a date/time for those fields that are of type date/time. |
| 14 | `VALUE_NBR` | DOUBLE |  |  | This column will contain a numeric value for those fields that are of type numeric. |
| 15 | `VALUE_TXT` | VARCHAR(255) |  |  | This column will contain a string of text for those fields that are of type text. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFIED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_MED_DETAIL_ID` | [RAD_MED_DETAILS](RAD_MED_DETAILS.md) | `RAD_MED_DETAIL_ID` |

