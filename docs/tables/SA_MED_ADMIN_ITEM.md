# SA_MED_ADMIN_ITEM

> SA Medication Admin Items - Child of SA_Medication_Admin table.

**Description:** SA Medication Admin items  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_AMOUNT` | DOUBLE |  |  | Admin Amount value |
| 6 | `ADMIN_DOSAGE` | DOUBLE |  |  | Admin Dosage value |
| 7 | `ADMIN_START_DT_TM` | DATETIME |  |  | Start Date and Time |
| 8 | `ADMIN_STOP_DT_TM` | DATETIME |  |  | Stop Date and Time |
| 9 | `DOSING_INFUSION_RATE` | DOUBLE |  |  | The dosing infusion rate |
| 10 | `PUMP_INFUSION_RATE` | DOUBLE |  |  | The Pump Infusion Rate |
| 11 | `SA_MEDICATION_ADMIN_ID` | DOUBLE | NOT NULL | FK→ | SA Medication Admin ID - foreign key |
| 12 | `SA_MED_ADMIN_ITEM_ID` | DOUBLE | NOT NULL |  | SA Medication Admin Item ID - Primary Key |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `WEIGHT_BASED_DOSE` | DOUBLE |  |  | Dose based on Weight |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_MEDICATION_ADMIN_ID` | [SA_MEDICATION_ADMIN](SA_MEDICATION_ADMIN.md) | `SA_MEDICATION_ADMIN_ID` |

