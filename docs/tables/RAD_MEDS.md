# RAD_MEDS

> This table contains those medications that were administered while performing a radiological procedure.

**Description:** Rad Meds  
**Table type:** ACTIVITY  
**Primary key:** `RAD_MED_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_DT_NBR` | DOUBLE |  |  | A conversion of the admin_dt_tm to an integer. |
| 6 | `ADMIN_DT_TM` | DATETIME |  |  | The date and time the med was administered. For the MAR, it is considered the time that the administration was completed, since all meds added through RadNet are completed meds. |
| 7 | `ADMIN_MIN_NBR` | DOUBLE |  |  | Admin minute number. |
| 8 | `ADMIN_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifier to the Medication Documentation created for the MAR. |
| 10 | `MODIFIED_DT_TM` | DATETIME | NOT NULL |  | This column is the date that the data was last changed by a user. |
| 11 | `MODIFIED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This column identifies the personnel that modified the med. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 13 | `RAD_MED_ID` | DOUBLE | NOT NULL | PK | This column contains a meaningless number that serves the purpose of uniquely identifying a row. |
| 14 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | This column is a foreign key to the order_catalog_synonym table. It identifies the medication that was administered. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFIED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_MED_DETAILS](RAD_MED_DETAILS.md) | `RAD_MED_ID` |

